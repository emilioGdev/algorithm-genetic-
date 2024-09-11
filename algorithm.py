import random
from resources import professores_horario, professores_info, responsabilidade_professores, dias_da_semana, horarios_manha, horarios_tarde, disciplina_por_periodo, carga_horaria_por_periodo
import matplotlib.pyplot as plt
import numpy as np

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
    horas_professor = {prof: 0 for prof in professores_info.keys()}

    for disciplina_info, carga_horaria in zip(disciplinas_periodo, carga_horaria_periodo):
        disciplina = disciplina_info['nome']
        lab = disciplina_info['lab']
        lab_tipo = escolher_lab_tipo() if lab else None

        if disciplina in responsabilidade_professores:
            professores_disponiveis = responsabilidade_professores[disciplina]
            professor_escolhido = None

            for professor in professores_disponiveis:
                slots_disponiveis = 0
                for dia in dias_da_semana:
                    slots_disponiveis += len(professores_horario[professor][dia])
                if slots_disponiveis >= carga_horaria // 15 and horas_professor[professor] + carga_horaria // 15 <= professores_info[professor]["max_horas"]:
                    professor_escolhido = professor
                    break

            if not professor_escolhido:
                raise ValueError(f"Não há professor disponível com slots suficientes para a disciplina {disciplina}")

            if carga_horaria == 90:
                aulas_semanais_dia1 = 4
                aulas_semanais_dia2 = 2

                alocar_aulas(aulas_distribuidas, labs_ocupados, disciplina, professor_escolhido, lab, lab_tipo, aulas_semanais_dia1, periodo, carga_horaria)
                horas_professor[professor_escolhido] += aulas_semanais_dia1

                alocar_aulas(aulas_distribuidas, labs_ocupados, disciplina, professor_escolhido, lab, lab_tipo, aulas_semanais_dia2, periodo, carga_horaria)
                horas_professor[professor_escolhido] += aulas_semanais_dia2
            else:
                aulas_semanais = carga_horaria // 15
                alocar_aulas(aulas_distribuidas, labs_ocupados, disciplina, professor_escolhido, lab, lab_tipo, aulas_semanais, periodo, carga_horaria)
                horas_professor[professor_escolhido] += aulas_semanais

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

                aulas_distribuidas = distribuir_aulas_por_periodo(periodo, disciplinas_periodo, carga_horaria_periodo, labs_ocupados, aulas_distribuidas_por_periodo)
                aulas_distribuidas_por_periodo[periodo] = aulas_distribuidas

            return aulas_distribuidas_por_periodo

        except ValueError as e:
            print(f"Erro durante a geração do cromossomo: {e}")
            print("Gerando um novo cromossomo...")
            continue
def calcular_penalidades(cromossomo):
    penalidades = 0
    professores_alocados = set()

    for periodo in cromossomo:
        disciplinas_periodo = set(disciplina_info['nome'] for disciplina_info in disciplina_por_periodo[periodo])
        disciplinas_alocadas = set()
        labs_utilizados = {dia: {slot: {'windows': False, 'linux': False} for slot in range(len(horarios_manha + horarios_tarde))} for dia in dias_da_semana}

        for dia in cromossomo[periodo]:
            for slot, aulas in enumerate(cromossomo[periodo][dia]):
                if slot >= len(horarios_manha) and aulas:
                    penalidades += PENALIDADE_SOFT

                for aula in aulas:
                    disciplina = aula[0]
                    professor = aula[1]
                    lab_tipo = aula[2]
                    disciplinas_alocadas.add(disciplina)
                    professores_alocados.add(professor)

                    if lab_tipo and labs_utilizados[dia][slot][lab_tipo]:
                        penalidades += PENALIDADE_HARD

                    if lab_tipo:
                        labs_utilizados[dia][slot][lab_tipo] = True

                professores_no_slot = [aula[1] for aula in aulas]
                if len(professores_no_slot) != len(set(professores_no_slot)):
                    penalidades += PENALIDADE_HARD

        disciplinas_nao_ofertadas = disciplinas_periodo - disciplinas_alocadas
        if disciplinas_nao_ofertadas:
            penalidades += PENALIDADE_HARD * len(disciplinas_nao_ofertadas)

    return penalidades

def calcular_fitness(cromossomo):
    penalidades = calcular_penalidades(cromossomo)
    fitness = 100 / (100 + penalidades)
    return fitness

def melhores_pais(populacao):
    lista_fitness = []
    
    for i, individuo in enumerate(populacao):
        fitness = calcular_fitness(individuo)
        lista_fitness.append((i, fitness))
    lista_fitness.sort(key=lambda x: x[1], reverse=True)
    
    return lista_fitness[0][0], lista_fitness[1][0]

def cruzamento(individuo_a, individuo_b, porcentagem=0.90, num_cortes=1):
    
    if random.random() < porcentagem:
        cortes_disponiveis = [0.05, 0.10, 0.15, 0.20, 0.25, 
                              0.30, 0.35, 0.40, 0.45, 0.50, 
                              0.55, 0.60, 0.65, 0.70, 0.75,
                              0.80, 0.85, 0.90, 0.95]
        
      
        num_cortes = min(num_cortes, len(cortes_disponiveis))
        
        
        cortes = sorted(random.sample(cortes_disponiveis, num_cortes))
        cortes = [int(len(individuo_a) * corte) for corte in cortes]
        
        
        novo_individuo_a = individuo_a[:]
        novo_individuo_b = individuo_b[:]
        
      
        for i, corte in enumerate(cortes):
            if i % 2 == 0:
               
                novo_individuo_a[corte:], novo_individuo_b[corte:] = individuo_b[corte:], individuo_a[corte:]
    
    else:
       
        novo_individuo_a = individuo_a[:]
        novo_individuo_b = individuo_b[:]
    
    return novo_individuo_a, novo_individuo_b


def mutacao(cromossomo, taxa_mutacao=0.9):
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

    for turma, horarios in cromossomo.items():
        for dia in dias_semana:
            i = 0
            while i < len(horarios[dia]):
                slot = horarios[dia][i]
                
                if random.random() < taxa_mutacao:
                    if slot:  
                        disciplina = slot[0]  
                        
                        if disciplina not in responsabilidade_professores:
                            i += 1
                            continue
                        
                        bloco = [slot]  
                        
                        while i + 1 < len(horarios[dia]) and horarios[dia][i + 1] == slot:
                            bloco.append(horarios[dia][i + 1])
                            i += 1
                        
                        professores = responsabilidade_professores[disciplina]
                        
                        novo_professor = random.choice(professores)
                        
              
                        for novo_dia in dias_semana:
                            if novo_professor in professores_horario and novo_dia in professores_horario[novo_professor]:
                                if all(h == "" for h in horarios[novo_dia][:len(bloco)]):
                                    horarios[novo_dia][:len(bloco)] = bloco
                                    break
                            
                        horarios[dia][:len(bloco)] = [""] * len(bloco)
                i += 1

    return cromossomo
def cromossomo_dict_to_list(cromossomo):
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    lista = []

    for turma in sorted(cromossomo.keys()):
        for dia in dias_semana:
            for slot in cromossomo[turma][dia]:
                lista.append(slot)

    return lista

def cromossomo_list_to_dict(lista, caso):
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    cromossomo = {}
    horarios_por_dia = 10

    num_turmas = len(lista) // (len(dias_semana) * horarios_por_dia)

    for i, turma in enumerate(range(caso, num_turmas*2 + 1, 2)):
        cromossomo[turma] = {}
        for dia_idx, dia in enumerate(dias_semana):
            inicio = ((i+1) - 1) * (len(dias_semana) * horarios_por_dia) + dia_idx * horarios_por_dia
            fim = inicio + horarios_por_dia
            cromossomo[turma][dia] = lista[inicio:fim]
    
    return cromossomo
def ordenar_populacao_por_fitness(populacao):
    populacao_ordenada = sorted(populacao, key=calcular_fitness, reverse=True)
    return populacao_ordenada

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

caso = 1
tam_populacao = 200
geracoes = 10
populacao = []

fitness_medio_por_geracao = []
melhor_fitness_por_geracao = []
desvio_padrao_por_geracao = []

for _ in range(tam_populacao):
    cromossomo = criar_cromossomo(caso)
    populacao.append(cromossomo)


for i in range(geracoes):
    populacao = ordenar_populacao_por_fitness(populacao)

    print(f"População Geração {i + 1}")
    for j in range(min(5, len(populacao))):
        print(calcular_fitness(populacao[j]))

  
    fitness_valores = [calcular_fitness(individuo) for individuo in populacao]
    fitness_medio = sum(fitness_valores) / len(fitness_valores)
    melhor_fitness = max(fitness_valores)
    desvio_padrao = np.std(fitness_valores)

    fitness_medio_por_geracao.append(fitness_medio)
    melhor_fitness_por_geracao.append(melhor_fitness)
    desvio_padrao_por_geracao.append(desvio_padrao)

    print(f"Fitness Médio: {fitness_medio}")
    print(f"Melhor Fitness: {melhor_fitness}")
    print(f"Desvio Padrão do Fitness: {desvio_padrao}")

    nova_populacao = []

    tam_populacao_fixa = int(tam_populacao * 0.2)
    nova_populacao.extend(populacao[:tam_populacao_fixa])

    tam_populacao_gerada = tam_populacao - tam_populacao_fixa
    for _ in range(tam_populacao_gerada // 2):
        populacao_selecionada = random.sample(populacao, 3)
        index_a, index_b = melhores_pais(populacao_selecionada)

        novo_individuo1, novo_individuo2 = cruzamento(
            cromossomo_dict_to_list(populacao_selecionada[index_a]),
            cromossomo_dict_to_list(populacao_selecionada[index_b]),
            porcentagem=0.90
        )

        novo_individuo1 = cromossomo_list_to_dict(novo_individuo1, caso)
        novo_individuo2 = cromossomo_list_to_dict(novo_individuo2, caso)

        novo_individuo1 = mutacao(novo_individuo1, taxa_mutacao=0.01)
        novo_individuo2 = mutacao(novo_individuo2, taxa_mutacao=0.01)

        nova_populacao.append(novo_individuo1)
        nova_populacao.append(novo_individuo2)

    populacao = ordenar_populacao_por_fitness(nova_populacao)


plt.figure(figsize=(10, 6))

plt.plot(range(1, geracoes + 1), fitness_medio_por_geracao, marker='o', linestyle='-', color='b', label='Fitness Médio')

plt.plot(range(1, geracoes + 1), melhor_fitness_por_geracao, marker='x', linestyle='--', color='g', label='Melhor Fitness')

plt.fill_between(range(1, geracoes + 1),
                 [fitness_medio - dp for fitness_medio, dp in zip(fitness_medio_por_geracao, desvio_padrao_por_geracao)],
                 [fitness_medio + dp for fitness_medio, dp in zip(fitness_medio_por_geracao, desvio_padrao_por_geracao)],
                 color='orange', alpha=0.3, label='Desvio Padrão')


plt.title('Convergência do Fitness ao Longo das Gerações')
plt.xlabel('Geração')
plt.ylabel('Fitness')
plt.grid(True)
plt.legend(loc='best')
plt.show()

melhor_individuo = populacao[0]

fitness_melhor_individuo = calcular_fitness(melhor_individuo)
print(f"Fitness do melhor indivíduo: {fitness_melhor_individuo}")
def cromossomo_valido(cromossomo):
    for periodo in cromossomo:
        disciplinas_periodo = set(disciplina_info['nome'] for disciplina_info in disciplina_por_periodo[periodo])
        disciplinas_alocadas = set()
        labs_utilizados = {dia: {slot: {'windows': False, 'linux': False} for slot in range(len(horarios_manha + horarios_tarde))} for dia in dias_da_semana}

        for dia in cromossomo[periodo]:
            for slot, aulas in enumerate(cromossomo[periodo][dia]):
                professores_no_slot = set()

                for aula in aulas:
                    disciplina = aula[0]
                    professor = aula[1]
                    lab_tipo = aula[2]
                    disciplinas_alocadas.add(disciplina)

                    if lab_tipo and labs_utilizados[dia][slot][lab_tipo]:
                        return False  

                    if lab_tipo:
                        labs_utilizados[dia][slot][lab_tipo] = True

                    if professor in professores_no_slot:
                        return False  
                    professores_no_slot.add(professor)

        disciplinas_nao_ofertadas = disciplinas_periodo - disciplinas_alocadas
        if disciplinas_nao_ofertadas:
            return False 

    return True  


if cromossomo_valido(melhor_individuo):
    print("O cromossomo é válido (sem penalidades hard).")
else:
    print("O cromossomo é inválido (com penalidades hard).")


html_tabela = gerar_tabela_html_do_cromossomo(melhor_individuo, caso)
nome_arquivo = "cronograma_ultimo_individuo.html"

salvar_html(html_tabela, nome_arquivo)
