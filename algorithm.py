import random
from resources import responsabilidade_professores, dias_da_semana, horarios_manha, horarios_tarde, disciplina_por_periodo, carga_horaria_por_periodo

PENALIDADE_HARD = 100
PENALIDADE_SOFT = 10

# Função para escolher o tipo de laboratório aleatoriamente
def escolher_lab_tipo():
    return 'windows' if random.choice([True, False]) else 'linux'

def criar_cromossomo(caso):
    if caso == 1:
        periodos = [1, 3, 5, 7]
    elif caso == 2:
        periodos = [2, 4, 6, 8]
    else:
        raise ValueError("Caso deve ser 1 ou 2")

    aulas_distribuidas_por_periodo = {}
    labs_ocupados = {dia: {slot: {'windows': False, 'linux': False} for slot in range(len(horarios_manha + horarios_tarde))} for dia in dias_da_semana}

    for periodo in periodos:
        disciplinas_periodo = disciplina_por_periodo[periodo]
        carga_horaria_periodo = carga_horaria_por_periodo[periodo]

        aulas_distribuidas = {dia: [[] for _ in range(len(horarios_manha + horarios_tarde))] for dia in dias_da_semana}

        for disciplina_info, carga_horaria in zip(disciplinas_periodo, carga_horaria_periodo):
            disciplina = disciplina_info['nome']
            lab = disciplina_info['lab']
            lab_tipo = escolher_lab_tipo() if lab else None

            if disciplina in responsabilidade_professores:
                professores_disponiveis = responsabilidade_professores[disciplina]
                professor_escolhido = random.choice(professores_disponiveis)

                if carga_horaria == 90:
                    aulas_semanais_dia1 = 4
                    aulas_semanais_dia2 = 2

                    alocado_dia1 = False
                    alocado_dia2 = False
                    tentativas = 0

                    while not (alocado_dia1 and alocado_dia2) and tentativas < 20:
                        tentativas += 1
                        dia = random.choice(dias_da_semana)

                        slots_disponiveis_manha = []
                        slots_disponiveis_tarde = []

                        for slot_inicio in range(len(horarios_manha) - aulas_semanais_dia1 + 1):
                            if all(len(aulas_distribuidas[dia][slot_inicio + i]) == 0 and (not lab or not labs_ocupados[dia][slot_inicio + i][lab_tipo]) for i in range(aulas_semanais_dia1)):
                                slots_disponiveis_manha.append(slot_inicio)
                        for slot_inicio in range(len(horarios_manha), len(horarios_manha) + len(horarios_tarde) - aulas_semanais_dia2 + 1):
                            if all(len(aulas_distribuidas[dia][slot_inicio + i]) == 0 and (not lab or not labs_ocupados[dia][slot_inicio + i][lab_tipo]) for i in range(aulas_semanais_dia2)):
                                slots_disponiveis_tarde.append(slot_inicio)

                        if not alocado_dia1 and slots_disponiveis_manha:
                            slot_escolhido = random.choice(slots_disponiveis_manha)
                            for i in range(aulas_semanais_dia1):
                                aulas_distribuidas[dia][slot_escolhido + i].append((disciplina, professor_escolhido, lab_tipo))
                                if lab:
                                    labs_ocupados[dia][slot_escolhido + i][lab_tipo] = True
                            alocado_dia1 = True
                        elif not alocado_dia2 and slots_disponiveis_tarde:
                            slot_escolhido = random.choice(slots_disponiveis_tarde)
                            for i in range(aulas_semanais_dia2):
                                aulas_distribuidas[dia][slot_escolhido + i].append((disciplina, professor_escolhido, lab_tipo))
                                if lab:
                                    labs_ocupados[dia][slot_escolhido + i][lab_tipo] = True
                            alocado_dia2 = True

                    if not (alocado_dia1 and alocado_dia2):
                        raise ValueError(f"Não foi possível alocar a carga horária de 90 horas da disciplina {disciplina}")

                else:
                    aulas_semanais = carga_horaria // 15  # 60 horas -> 4 aulas, 45 horas -> 3 aulas, 30 horas -> 2 aulas

                    alocado = False
                    tentativas = 0

                    while not alocado and tentativas < 20:
                        tentativas += 1
                        dia = random.choice(dias_da_semana)

                        slots_disponiveis_manha = []
                        slots_disponiveis_tarde = []

                        for slot_inicio in range(len(horarios_manha) - aulas_semanais + 1):
                            if all(len(aulas_distribuidas[dia][slot_inicio + i]) == 0 and (not lab or not labs_ocupados[dia][slot_inicio + i][lab_tipo]) for i in range(aulas_semanais)):
                                slots_disponiveis_manha.append(slot_inicio)
                        for slot_inicio in range(len(horarios_manha), len(horarios_manha) + len(horarios_tarde) - aulas_semanais + 1):
                            if all(len(aulas_distribuidas[dia][slot_inicio + i]) == 0 and (not lab or not labs_ocupados[dia][slot_inicio + i][lab_tipo]) for i in range(aulas_semanais)):
                                slots_disponiveis_tarde.append(slot_inicio)

                        if slots_disponiveis_manha:
                            slot_escolhido = random.choice(slots_disponiveis_manha)
                            for i in range(aulas_semanais):
                                aulas_distribuidas[dia][slot_escolhido + i].append((disciplina, professor_escolhido, lab_tipo))
                                if lab:
                                    labs_ocupados[dia][slot_escolhido + i][lab_tipo] = True
                            alocado = True
                        elif slots_disponiveis_tarde:
                            slot_escolhido = random.choice(slots_disponiveis_tarde)
                            for i in range(aulas_semanais):
                                aulas_distribuidas[dia][slot_escolhido + i].append((disciplina, professor_escolhido, lab_tipo))
                                if lab:
                                    labs_ocupados[dia][slot_escolhido + i][lab_tipo] = True
                            alocado = True

                    if not alocado:
                        raise ValueError(f"Não foi possível alocar {aulas_semanais} aulas de {disciplina} para o professor {professor_escolhido}")

        aulas_distribuidas_por_periodo[periodo] = aulas_distribuidas

    return aulas_distribuidas_por_periodo
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
                    print(f"Adicionada PENALIDADE_SOFT por ocupação de tarde no período {periodo}, dia {dia}, slot {slot}")

                for aula in aulas:
                    disciplina = aula[0]
                    professor = aula[1]
                    lab_tipo = aula[2]
                    disciplinas_alocadas.add(disciplina)

                    # Verificar conflito de laboratório
                    if lab_tipo and labs_utilizados[dia][slot][lab_tipo]:
                        penalidades += PENALIDADE_HARD
                        print(f"Adicionada PENALIDADE_HARD por conflito de laboratório no período {periodo}, dia {dia}, slot {slot}. Laboratório: {lab_tipo}")

                    # Marcar laboratório como utilizado
                    if lab_tipo:
                        labs_utilizados[dia][slot][lab_tipo] = True

                # Penalidade hard: Verificar conflitos de professores
                professores_no_slot = [aula[1] for aula in aulas]
                if len(professores_no_slot) != len(set(professores_no_slot)):
                    penalidades += PENALIDADE_HARD
                    print(f"Adicionada PENALIDADE_HARD por conflito de professores no período {periodo}, dia {dia}, slot {slot}. Professores: {professores_no_slot}")

        # Penalidade hard: Verificar se todas as disciplinas do período estão ofertadas
        disciplinas_nao_ofertadas = disciplinas_periodo - disciplinas_alocadas
        if disciplinas_nao_ofertadas:
            penalidades += PENALIDADE_HARD * len(disciplinas_nao_ofertadas)
            print(f"Adicionada PENALIDADE_HARD por disciplinas não ofertadas no período {periodo}: {disciplinas_nao_ofertadas}")

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
        html += "<table border='1'>\n"

        html += "<tr><th>Horário</th>"
        for dia in dias_da_semana:
            html += f"<th>{dia}</th>"
        html += "</tr>\n"

        horario_semanal = {dia: {horario: [] for horario in horarios_manha + horarios_tarde} for dia in dias_da_semana}

        for dia in dias_da_semana:
            for slot, aulas in enumerate(cromossomo[periodo][dia]):
                for disciplina, professor, lab_tipo in aulas:
                    horario = horarios_manha[slot] if slot < len(horarios_manha) else horarios_tarde[slot - len(horarios_manha)]
                    if lab_tipo:
                        horario_semanal[dia][horario].append(f"{disciplina} - Prof. {professor} - <strong>Lab {lab_tipo}</strong>")
                    else:
                        horario_semanal[dia][horario].append(f"{disciplina} - Prof. {professor}")

        for horario in horarios_manha + horarios_tarde:
            html += "<tr>"
            html += f"<td>{horario}</td>"
            for dia in dias_da_semana:
                aulas = horario_semanal[dia][horario]
                if aulas:
                    html += f"<td>{'<br>'.join(aulas)}</td>"
                else:
                    html += "<td>-</td>"
            html += "</tr>\n"

        html += "</table>\n"

    return html

def salvar_html(html, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write(html)
    print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")

# Exemplo de uso:
caso = 1  # Defina o caso que você quer gerar (1 ou 2)
horarios_por_periodo = criar_cromossomo(caso)

# Calcular fitness do cromossomo gerado
fitness = calcular_fitness(horarios_por_periodo)
print(f"Fitness do cromossomo: {fitness}")

# Gerar tabela HTML
html_tabela = gerar_tabela_html_do_cromossomo(horarios_por_periodo, caso)
nome_arquivo = "cronograma.html"

# Imprimir ou salvar o HTML gerado
salvar_html(html_tabela, nome_arquivo)
