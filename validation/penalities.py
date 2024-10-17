from resources import dias_da_semana, horarios_manha, horarios_tarde, disciplina_por_periodo, professores_info

PENALIDADE_HARD = 100
PENALIDADE_SOFT = 1

def somar_horas_professores(*dicionarios):
    total_horas = {}

    for dicionario in dicionarios:
        for professor, horas in dicionario.items():
            if professor in total_horas:
                total_horas[professor] += horas
            else:
                total_horas[professor] = horas

    return total_horas

def calcular_penalidades(cromossomo):
    penalidades = 0
    professores_alocados = set()
    horas_professores = {professor: 0 for professor in professores_info.keys()}
    horas_por_periodo = []
    mensagens = []  # Lista para armazenar as mensagens

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

                    horas_professores[professor] += 1

                    if lab_tipo and labs_utilizados[dia][slot][lab_tipo]:
                        penalidades += PENALIDADE_HARD
                        mensagem = (f"Conflito de laboratório detectado: {lab_tipo} já está em uso no período {periodo}, dia {dia}, slot {slot}")
                        mensagens.append(mensagem)
                    
                    if lab_tipo:
                        labs_utilizados[dia][slot][lab_tipo] = True

                professores_no_slot = [aula[1] for aula in aulas]
                if len(professores_no_slot) != len(set(professores_no_slot)):
                    penalidades += PENALIDADE_HARD
                    mensagem = (f"Conflito de professor detectado: Professor {professor} já está alocado no período {periodo}, dia {dia}, slot {slot}")
                    mensagens.append(mensagem)

        disciplinas_nao_ofertadas = disciplinas_periodo - disciplinas_alocadas
        if disciplinas_nao_ofertadas:
            penalidades += PENALIDADE_HARD * len(disciplinas_nao_ofertadas)
            mensagem = f"Disciplinas não ofertadas no período {periodo}: {disciplinas_nao_ofertadas}"
            mensagens.append(mensagem)

        horas_por_periodo.append(horas_professores.copy())
        total_horas = somar_horas_professores(*horas_por_periodo)

        for professor, horas in total_horas.items():
            max_horas = professores_info[professor]['max_horas']
            if horas > max_horas: 
                penalidades += PENALIDADE_HARD
                mensagem = (f"Professor {professor} excedeu o máximo de horas permitidas: {horas} > {max_horas}")
                mensagens.append(mensagem)

    return penalidades, mensagens  

def calcular_fitness(cromossomo):
    penalidades, mensagens = calcular_penalidades(cromossomo) 
    fitness = 100 / (100 + penalidades)
    return fitness, mensagens  