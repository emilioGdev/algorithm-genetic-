from resources_2024_1 import dias_da_semana, horarios_manha, horarios_tarde, disciplina_por_periodo

PENALIDADE_HARD = 100
PENALIDADE_SOFT = 1


def calcular_penalidades(cromossomo):
    penalidades = 0
    professores_alocados = set()

    for periodo in cromossomo:
        disciplinas_periodo = set(disciplina_info['nome'] for disciplina_info in disciplina_por_periodo[periodo])
        disciplinas_alocadas = set()
        labs_utilizados = {dia: {slot: {'windows': False, 'linux': False} for slot in range(len(horarios_manha + horarios_tarde))} for dia in dias_da_semana}

        for dia in cromossomo[periodo]:
            for slot, aulas in enumerate(cromossomo[periodo][dia]):
                # Penalidade soft: Livrar os horários da tarde ao máximo
                if slot >= len(horarios_manha) and aulas:
                    penalidades += PENALIDADE_SOFT
                #    print(f"Adicionada PENALIDADE_SOFT por ocupação de tarde no período {periodo}, dia {dia}, slot {slot}")

                for aula in aulas:
                    disciplina = aula[0]
                    professor = aula[1]
                    lab_tipo = aula[2]
                    disciplinas_alocadas.add(disciplina)
                    professores_alocados.add(professor)



                    # Verificar conflito de laboratório
                    if lab_tipo and labs_utilizados[dia][slot][lab_tipo]:
                        penalidades += PENALIDADE_HARD
                  #      print(f"Adicionada PENALIDADE_HARD por conflito de laboratório no período {periodo}, dia {dia}, slot {slot}. Laboratório: {lab_tipo}")

                    # Marcar laboratório como utilizado
                    if lab_tipo:
                        labs_utilizados[dia][slot][lab_tipo] = True

                # Penalidade hard: Verificar conflitos de professores
                professores_no_slot = [aula[1] for aula in aulas]
                if len(professores_no_slot) != len(set(professores_no_slot)):
                    penalidades += PENALIDADE_HARD
               #     print(f"Adicionada PENALIDADE_HARD por conflito de professores no período {periodo}, dia {dia}, slot {slot}. Professores: {professores_no_slot}")

        # Penalidade hard: Verificar se todas as disciplinas do período estão ofertadas
        disciplinas_nao_ofertadas = disciplinas_periodo - disciplinas_alocadas
        if disciplinas_nao_ofertadas:
            penalidades += PENALIDADE_HARD * len(disciplinas_nao_ofertadas)
         #   print(f"Adicionada PENALIDADE_HARD por disciplinas não ofertadas no período {periodo}: {disciplinas_nao_ofertadas}")

    return penalidades

def calcular_fitness(cromossomo):
    penalidades = calcular_penalidades(cromossomo)
    fitness = 100 / (100 + penalidades)
    return fitness

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

                    # Verifica conflito de laboratório
                    if lab_tipo and labs_utilizados[dia][slot][lab_tipo]:
                     #   print(f"Penalidade: Conflito de laboratório no dia {dia}, slot {slot}, laboratório {lab_tipo}")
                        return False  # Penalidade hard: conflito de laboratório

                    if lab_tipo:
                        labs_utilizados[dia][slot][lab_tipo] = True

                    # Verifica conflito de professor
                    if professor in professores_no_slot:
                     #   print(f"Penalidade: Conflito de professor '{professor}' no dia {dia}, slot {slot}")
                        return False  # Penalidade hard: conflito de professores

                    professores_no_slot.add(professor)

        # Verifica disciplinas não ofertadas
        disciplinas_nao_ofertadas = disciplinas_periodo - disciplinas_alocadas
        if disciplinas_nao_ofertadas:
           # print(f"Penalidade: Disciplinas não ofertadas no período {periodo}: {disciplinas_nao_ofertadas}")
            return False  # Penalidade hard: disciplinas não ofertadas

    print("O cromossomo é válido (sem penalidades hard).")
    return True  