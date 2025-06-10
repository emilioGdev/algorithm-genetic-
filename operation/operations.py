import random
from resources import professores_horario, responsabilidade_professores

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


def mutacao(cromossomo, taxa_mutacao=0.01):
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