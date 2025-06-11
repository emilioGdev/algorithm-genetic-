📝 Contexto do Projeto:
Este repositório contém o código-fonte do Trabalho de Conclusão de Curso (TCC) em Engenharia de Software, desenvolvido na Universidade de Pernambuco (UPE) - Campus Garanhuns.

O objetivo principal foi desenvolver uma solução automatizada e personalizada, baseada em Algoritmos Genéticos, para a complexa tarefa de gerar as grades de horários do curso de Engenharia de Software. 


🎯 O Problema:
A criação da grade de horários em uma universidade é um problema de otimização combinatória classificado como NP-difícil.  O processo envolve a alocação de disciplinas, professores e salas, respeitando um conjunto rigoroso de restrições para evitar conflitos.  Quando realizado manualmente, esse processo consome muito tempo e esforço, e nem sempre leva a um resultado ótimo. 



A questão central do trabalho foi: Como algoritmos genéticos podem auxiliar os coordenadores do curso de Engenharia de Software da UPE-Campus Garanhuns na organização de uma grade de horários? 

💡 A Solução: Algoritmo Genético
Para resolver este desafio, foi projetado e implementado um Algoritmo Genético (AG) em Python. A solução simula o processo de evolução natural para explorar um vasto espaço de busca e encontrar grades de horários de alta qualidade.  O algoritmo evolui uma população de horários ao longo de várias gerações, aplicando operadores genéticos para aprimorar continuamente as soluções. 


Detalhes do Algoritmo Genético:
A implementação foi personalizada para atender às regras específicas da UPE Garanhuns:

Representação do Cromossomo: Cada "indivíduo" (uma grade de horário completa) é representado por uma estrutura de dados complexa. Cada "gene" contém informações essenciais para uma alocação de aula: Disciplina, Professor, Período, Horário e uso de Laboratório. 

Função de Aptidão (Fitness): A qualidade de cada horário é medida por uma função de aptidão que busca maximizar uma pontuação, partindo de 1. Penalidades são aplicadas para cada violação de restrição, com pesos diferentes para regras obrigatórias e preferências:

Restrições Hard (Obrigatórias): Penalidade de 100 pontos. Ex: professor em dois lugares ao mesmo tempo, conflito de uso de laboratório. 
Restrições Soft (Flexíveis): Penalidade de 1 ponto. Ex: alocar aulas no período da tarde. 


Operadores Genéticos:

Seleção por Torneio: Grupos de 3 indivíduos são sorteados, e os 2 com maior fitness são selecionados como pais para a próxima geração. 
Cruzamento de Múltiplos Pontos (K-Pontos): Para gerar diversidade, os cromossomos dos pais trocam segmentos de genes a partir de pontos de corte. 
Mutação de Substituição (Adaptada): Esta foi uma contribuição chave do trabalho. Em vez de uma simples troca aleatória de genes (que geraria muitos horários inválidos), este operador realiza um remanejamento inteligente. Ao tentar alterar uma aula, ele verifica a disponibilidade de professores e o impacto na grade como um todo, garantindo que as restrições hard nunca sejam violadas pela mutação. 


População Inicial de Qualidade: Diferente de uma abordagem totalmente aleatória, a população inicial já é criada respeitando as restrições hard, garantindo um ponto de partida de alta qualidade para o processo evolutivo. 


📊 Resultados e Comparação
O algoritmo foi testado com dados reais dos semestres 2024.1 e 2024.2 do curso, e os resultados foram comparados com as grades geradas manualmente pelos coordenadores. Os resultados demonstram que o AG foi capaz de produzir grades de altíssima qualidade, com valores de fitness muito próximos aos obtidos manualmente. A grande vantagem é a drástica redução de tempo e esforço: um processo que pode levar semanas de trabalho manual pode ser executado pelo algoritmo em segundos. 


🛠️ Tecnologias Utilizadas
Python 3
NumPy: Para manipulação de dados. 
Matplotlib: Para a visualização dos gráficos de convergência. 
O algoritmo foi desenvolvido puramente em Python, sem o uso de bibliotecas de AG de terceiros (como DEAP), para permitir um controle total sobre a estrutura complexa do cromossomo e dos operadores genéticos. 
