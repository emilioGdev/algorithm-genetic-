import random
from resources import professores_horario, responsabilidade_professores, dias_da_semana, horarios_manha, horarios_tarde, disciplina_por_periodo, carga_horaria_por_periodo

PENALIDADE_HARD = 100
PENALIDADE_SOFT = 1

def escolher_lab_tipo():
    return 'windows' if random.choice([True, False]) else 'linux'
def alocar_aulas(aulas_distribuidas, labs_ocupados, disciplina, professor, lab, lab_tipo, aulas_semanais, periodo, carga_horaria):
    alocado = False
    tentativas = 0

    while not alocado and tentativas < 20:
        tentativas += 1
        dia = random.choice(dias_da_semana)

        slots_disponiveis_manha = []
        slots_disponiveis_tarde = []

        for slot_inicio in range(len(horarios_manha) - aulas_semanais + 1):
            if all(
                len(aulas_distribuidas[dia][slot_inicio + i]) == 0 and 
                (not lab or not labs_ocupados[dia][slot_inicio + i][lab_tipo]) and
                (horarios_manha[slot_inicio + i] in professores_horario[professor][dia]) and
                (not any(professor in aula for aula in aulas_distribuidas[dia][slot_inicio + i]))
                for i in range(aulas_semanais)
            ):
                slots_disponiveis_manha.append(slot_inicio)

        for slot_inicio in range(len(horarios_manha), len(horarios_manha) + len(horarios_tarde) - aulas_semanais + 1):
            if all(
                len(aulas_distribuidas[dia][slot_inicio + i]) == 0 and 
                (not lab or not labs_ocupados[dia][slot_inicio + i][lab_tipo]) and
                (horarios_tarde[slot_inicio - len(horarios_manha) + i] in professores_horario[professor][dia]) and
                (not any(professor in aula for aula in aulas_distribuidas[dia][slot_inicio + i]))
                for i in range(aulas_semanais)
            ):
                slots_disponiveis_tarde.append(slot_inicio)

        if slots_disponiveis_manha:
            slot_escolhido = random.choice(slots_disponiveis_manha)
            for i in range(aulas_semanais):
                aulas_distribuidas[dia][slot_escolhido + i].append((disciplina, professor, lab_tipo))
                if lab:
                    labs_ocupados[dia][slot_escolhido + i][lab_tipo] = True
            alocado = True
        elif slots_disponiveis_tarde:
            slot_escolhido = random.choice(slots_disponiveis_tarde)
            for i in range(aulas_semanais):
                aulas_distribuidas[dia][slot_escolhido + i].append((disciplina, professor, lab_tipo))
                if lab:
                    labs_ocupados[dia][slot_escolhido + i][lab_tipo] = True
            alocado = True

    if not alocado:
        raise ValueError(f"Não foi possível alocar {aulas_semanais} aulas de {disciplina} para o professor {professor}")

def distribuir_aulas_por_periodo(periodo, disciplinas_periodo, carga_horaria_periodo, labs_ocupados, aulas_distribuidas_por_periodo):
    aulas_distribuidas = aulas_distribuidas_por_periodo.get(periodo, {dia: [[] for _ in range(len(horarios_manha + horarios_tarde))] for dia in dias_da_semana})

    for disciplina_info, carga_horaria in zip(disciplinas_periodo, carga_horaria_periodo):
        disciplina = disciplina_info['nome']
        lab = disciplina_info['lab']
        lab_tipo = escolher_lab_tipo() if lab else None

        if disciplina in responsabilidade_professores:
            professores_disponiveis = responsabilidade_professores[disciplina]
            professor_escolhido = None

            for professor in professores_disponiveis:
                # Verifica se o professor tem slots suficientes disponíveis
                slots_disponiveis = 0
                for dia in dias_da_semana:
                    slots_disponiveis += len(professores_horario[professor][dia])
                if slots_disponiveis >= carga_horaria // 15:
                    professor_escolhido = professor
                    break

            if not professor_escolhido:
                raise ValueError(f"Não há professor disponível com slots suficientes para a disciplina {disciplina}")

            if carga_horaria == 90:
                aulas_semanais_dia1 = 4
                aulas_semanais_dia2 = 2

                alocar_aulas(aulas_distribuidas, labs_ocupados, disciplina, professor_escolhido, lab, lab_tipo, aulas_semanais_dia1, periodo, carga_horaria)
                alocar_aulas(aulas_distribuidas, labs_ocupados, disciplina, professor_escolhido, lab, lab_tipo, aulas_semanais_dia2, periodo, carga_horaria)
            else:
                aulas_semanais = carga_horaria // 15
                alocar_aulas(aulas_distribuidas, labs_ocupados, disciplina, professor_escolhido, lab, lab_tipo, aulas_semanais, periodo, carga_horaria)

    return aulas_distribuidas

def criar_cromossomo(caso):
    if caso == 1:
        periodos = [1, 3, 5, 7]
    elif caso == 2:
        periodos = [2, 4, 6, 8]
    else:
        raise ValueError("Caso deve ser 1 ou 2")

    while True:
        try:
            aulas_distribuidas_por_periodo = {}
            labs_ocupados = {dia: {slot: {'windows': False, 'linux': False} for slot in range(len(horarios_manha + horarios_tarde))} for dia in dias_da_semana}

            for periodo in periodos:
                disciplinas_periodo = disciplina_por_periodo[periodo]
                carga_horaria_periodo = carga_horaria_por_periodo[periodo]

                # Chama a função para distribuir aulas para o período atual
                aulas_distribuidas = distribuir_aulas_por_periodo(periodo, disciplinas_periodo, carga_horaria_periodo, labs_ocupados, aulas_distribuidas_por_periodo)
                aulas_distribuidas_por_periodo[periodo] = aulas_distribuidas

            return aulas_distribuidas_por_periodo

        except ValueError as e:
            print(f"Erro durante a geração do cromossomo: {e}")
            print("Gerando um novo cromossomo...")
            continue
def calcular_penalidades(cromossomo):
    penalidades = 0

    for periodo in cromossomo:
        disciplinas_periodo = set(disciplina_info['nome'] for disciplina_info in disciplina_por_periodo[periodo])
        disciplinas_alocadas = set()
        labs_utilizados = {dia: {slot: {'windows': False, 'linux': False} for slot in range(len(horarios_manha + horarios_tarde))} for dia in dias_da_semana}

        for dia in cromossomo[periodo]:
            for slot, aulas in enumerate(cromossomo[periodo][dia]):
                # Penalidade soft: Livrar os horários da tarde ao máximo
                if slot >= len(horarios_manha) and aulas:
                    penalidades += PENALIDADE_SOFT
                    #print(f"Adicionada PENALIDADE_SOFT por ocupação de tarde no período {periodo}, dia {dia}, slot {slot}")

                for aula in aulas:
                    disciplina = aula[0]
                    professor = aula[1]
                    lab_tipo = aula[2]
                    disciplinas_alocadas.add(disciplina)

                    # Verificar conflito de laboratório
                    if lab_tipo and labs_utilizados[dia][slot][lab_tipo]:
                        penalidades += PENALIDADE_HARD
                        #print(f"Adicionada PENALIDADE_HARD por conflito de laboratório no período {periodo}, dia {dia}, slot {slot}. Laboratório: {lab_tipo}")

                    # Marcar laboratório como utilizado
                    if lab_tipo:
                        labs_utilizados[dia][slot][lab_tipo] = True

                # Penalidade hard: Verificar conflitos de professores
                professores_no_slot = [aula[1] for aula in aulas]
                if len(professores_no_slot) != len(set(professores_no_slot)):
                    penalidades += PENALIDADE_HARD
                    #print(f"Adicionada PENALIDADE_HARD por conflito de professores no período {periodo}, dia {dia}, slot {slot}. Professores: {professores_no_slot}")

        # Penalidade hard: Verificar se todas as disciplinas do período estão ofertadas
        disciplinas_nao_ofertadas = disciplinas_periodo - disciplinas_alocadas
        if disciplinas_nao_ofertadas:
            penalidades += PENALIDADE_HARD * len(disciplinas_nao_ofertadas)
            #print(f"Adicionada PENALIDADE_HARD por disciplinas não ofertadas no período {periodo}: {disciplinas_nao_ofertadas}")

    return penalidades


def calcular_fitness(cromossomo):
    penalidades = calcular_penalidades(cromossomo)
    fitness = 100 / (100 + penalidades)
    return fitness


def gerar_tabela_html_do_cromossomo(cromossomo, caso):
    if caso == 1:
        periodos = [1, 3, 5, 7]
    elif caso == 2:
        periodos = [2, 4, 6, 8]
    else:
        raise ValueError("Caso deve ser 1 ou 2")

    html = ""

    for periodo in periodos:
        html += f"<h2>Período {periodo}</h2>\n"
        html += "<table border='1'>\n<tr><th>Horário</th>"
        for dia in dias_da_semana:
            html += f"<th>{dia}</th>"
        html += "</tr>\n"

        for slot in range(len(horarios_manha + horarios_tarde)):
            horario = horarios_manha[slot] if slot < len(horarios_manha) else horarios_tarde[slot - len(horarios_manha)]
            html += f"<tr><td>{horario}</td>"

            for dia in dias_da_semana:
                aulas = cromossomo[periodo][dia][slot]
                aula_str = "<br>".join(
                    f"{disciplina}<br>{professor}" + (f"<br><b>Lab: {lab_tipo}</b>" if lab_tipo else "")
                    for disciplina, professor, lab_tipo in aulas
                )
                html += f"<td>{aula_str}</td>"

            html += "</tr>\n"

        html += "</table>\n"

    return html
def salvar_html(html, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write(html)
    print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")

def melhores_pais(populacao):
    lista_fitness = []
    
    for i, individuo in enumerate(populacao):
        fitness = calcular_fitness(individuo)
        lista_fitness.append((i, fitness))
    lista_fitness.sort(key=lambda x: x[1], reverse=True)
    
    return lista_fitness[0][0], lista_fitness[1][0]

def cruzamento(individuo_a, individuo_b, porcentagem=0.25):
    corte = int(len(individuo_a) * porcentagem)

    novo_individuo_a = individuo_a[:corte] + individuo_b[corte:]
    novo_individuo_b = individuo_b[:corte] + individuo_a[corte:]
    
    return novo_individuo_a, novo_individuo_b


def cromossomo_dict_to_list(cromossomo):
    # Mapeia dias da semana para seus índices
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    lista = []

    # Percorre as turmas e ordena por dias e horários
    for turma in sorted(cromossomo.keys()):
        for dia in dias_semana:
            lista.extend(cromossomo[turma][dia])
    
    return lista

def cromossomo_list_to_dict(lista, caso):
    # Mapeia índices para dias da semana
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    cromossomo = {}
    horarios_por_dia = 10

    # Número de turmas (deduzido do comprimento da lista)
    num_turmas = len(lista) // (len(dias_semana) * horarios_por_dia)

    # Reconstrói o dicionário do cromossomo
    for i, turma in enumerate(range(caso, num_turmas*2 + 1, 2)):
        cromossomo[turma] = {}
        for dia_idx, dia in enumerate(dias_semana):
            inicio = ((i+1) - 1) * (len(dias_semana) * horarios_por_dia) + dia_idx * horarios_por_dia
            fim = inicio + horarios_por_dia
            cromossomo[turma][dia] = lista[inicio:fim]
    
    return cromossomo

def ordenar_populacao_por_fitness(populacao):
    # Ordena a população pela chave fitness, do maior para o menor
    populacao_ordenada = sorted(populacao, key=calcular_fitness, reverse=True)
    return populacao_ordenada

# Exemplo de uso:
caso = 1  # Defina o caso que você quer gerar (1 ou 2)
tam_populacao = 100
geracoes = 5
populacao = []

for i in range(tam_populacao):
    cromossomo = criar_cromossomo(caso)
    populacao.append(cromossomo)

for i in range(geracoes):

    populacao = ordenar_populacao_por_fitness(populacao)

    print(f"Populacao Geracao {i+1}")
    for i in range(5):    
        print(calcular_fitness(populacao[i]))

    nova_populacao = []

    tam_populacao_fixa = int(tam_populacao * 0.2)
    tam_populacao_gerada = tam_populacao - tam_populacao_fixa

    nova_populacao = populacao[:tam_populacao_fixa]

    for i in range(tam_populacao_gerada//2):
        populacao_selecionada = random.sample(populacao, 3)
        index_a, index_b = melhores_pais(populacao_selecionada)
        novo_individuo1, novo_individuo2 = cruzamento(cromossomo_dict_to_list(populacao_selecionada[index_a]), cromossomo_dict_to_list(populacao_selecionada[index_b]), porcentagem=0.5)
        
        novo_individuo1 = cromossomo_list_to_dict(novo_individuo1, caso)
        novo_individuo2 = cromossomo_list_to_dict(novo_individuo2, caso)
        
        nova_populacao.append(novo_individuo1)
        nova_populacao.append(novo_individuo2)

    populacao = ordenar_populacao_por_fitness(nova_populacao)


# horarios_por_periodo = criar_cromossomo(caso)
# horarios_por_periodo_2 = criar_cromossomo(caso)
# horarios_por_periodo_3 = criar_cromossomo(caso)

# # Calcular fitness do cromossomo gerado
# fitness = calcular_fitness(horarios_por_periodo)
# fitness_2 = calcular_fitness(horarios_por_periodo_2)
# fitness_3 = calcular_fitness(horarios_por_periodo_3)
# print(f"Fitness do cromossomo: {fitness}, {fitness_2} e {fitness_3}")
# # print("Primeiro cromossomo:")
# # print(horarios_por_periodo)
# # print("Segundo cromossomo:")
# # print(horarios_por_periodo_2)
# # print("Terceiro cromossomo:")
# # print(horarios_por_periodo_3)

# populacao_selecionada = [horarios_por_periodo, horarios_por_periodo_2, horarios_por_periodo_3]

# index_a, index_b = melhores_pais(populacao_selecionada)

# novo_individuo1, novo_individuo2 = cruzamento(cromossomo_dict_to_list(populacao_selecionada[index_a]), cromossomo_dict_to_list(populacao_selecionada[index_b]), porcentagem=0.5)

# novo_individuo1 = cromossomo_list_to_dict(novo_individuo1, caso)
# novo_individuo2 = cromossomo_list_to_dict(novo_individuo2, caso)
# fitness_4 = calcular_fitness(novo_individuo1)
# fitness_5 = calcular_fitness(novo_individuo2)
# print(f"Fitness do cromossomo: {fitness_4} e {fitness_5}")

# # Gerar tabela HTML
# html_tabela = gerar_tabela_html_do_cromossomo(horarios_por_periodo, caso)
# nome_arquivo = "cronograma.html"

# # Imprimir ou salvar o HTML gerado
# salvar_html(html_tabela, nome_arquivo)
