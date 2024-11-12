import random
from alocation.alocations import distribuir_aulas_por_periodo
from save.save_html import gerar_tabela_html_do_cromossomo, salvar_html
from operation.operations import cruzamento, mutacao
from resources_2024_2 import dias_da_semana, horarios_manha, horarios_tarde, disciplina_por_periodo, carga_horaria_por_periodo
import matplotlib.pyplot as plt
import numpy as np
from validation.penalities import calcular_fitness, cromossomo_valido

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

def melhores_pais(populacao):
    lista_fitness = []
    
    for i, individuo in enumerate(populacao):
        fitness = calcular_fitness(individuo)
        lista_fitness.append((i, fitness))
    lista_fitness.sort(key=lambda x: x[1], reverse=True)
    
    return lista_fitness[0][0], lista_fitness[1][0]


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


caso = 2
tam_populacao = 1000
geracoes = 20
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

html_tabela = gerar_tabela_html_do_cromossomo(melhor_individuo, caso)
fitness_1 = calcular_fitness(melhor_individuo)

nome_arquivo = "cronograma_ultimo_individuo.html"

salvar_html(html_tabela, nome_arquivo)


if cromossomo_valido(melhor_individuo):
    print("O cromossomo é válido (sem penalidades hard).")
else:
    print("O cromossomo é inválido (com penalidades hard).")