import random
from resources import professores_horario, professores_info, responsabilidade_professores, dias_da_semana, horarios_manha, horarios_tarde, disciplina_por_periodo, carga_horaria_por_periodo



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