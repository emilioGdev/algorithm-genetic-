# Defina os dados iniciais
professores = ["Adauto Trigueiro", "Aêda Monalliza", "Ariane Nunes", "Brunno Wagner", "Cleiton Soares", "Cleyton Mário",
               "Cleverton Anderson", "Emanoel Francisco", "Erton Wagner", "Ewerton Menezes", "Fellipe Anchiêta", "Helaine Solange",
               "Higor Ricardo", "Ivaldir Honório", "Victor Afonso", "Maurício Costa", "Milton Perceus", "Paulo Cavalcante", "Dâmocles Aurélio"]

#Definindo a disponibilidade dos professores
professores_horario = {
    "Adauto Trigueiro": [1, 2, 3],
    "Aêda Monalliza": [1, 2, 3],
    "Ariane Nunes": [1, 2, 3],
    "Brunno Wagner": [1, 2, 3],
    "Cleiton Soares": [1, 2, 3],
    "Cleyton Mário": [1, 2, 3],
    "Cleverton Anderson": [1, 2, 3],
    "Emanoel Francisco": [1, 2, 3],
    "Erton Wagner": [1, 2, 3],
    "Ewerton Menezes": [1, 2, 3],
    "Fellipe Anchiêta": [1, 2, 3],
    "Helaine Solange": [1, 2, 3],
    "Higor Ricardo": [1, 2, 3],
    "Ivaldir Honório": [1, 2, 3],
    "Victor Afonso": [1, 2, 3],
    "Maurício Costa": [1, 2, 3],
    "Milton Perceus": [1, 2, 3],
    "Paulo Cavalcante": [1, 2, 3],
    "Dâmocles Aurélio": [1, 2, 3]
}

num_periodos = 4 # Só vão existir 4 períodos por semestre. Exemplo 1: 1°, 3°, 5° e 7°; Exemplo 2: 2°, 4°, 6° e 8° - Só tem essas 2 opções e o usuário que vai escolher qual ele quer.
num_dias_da_semana = 5
slots_por_dia = 10  # 6 de Manhã e 4 de Tarde, e cada aula durá 50 minutos. As aulas pela manhã vão de 7h30 até 12h30, e pela tarde de 13h30 até 17h30
total_cadeiras_por_periodo = [7, 7, 7, 7, 7, 7, 7, 6]  # Número de cadeiras por período
dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
horarios_manha = ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40"]
horarios_tarde = ["13h30", "14h30", "15h30", "16h30"]

disciplina_por_periodo = {
    1:[
    "Geometria Analítica",
    "Programação I",
    "Computação Ética e Sociedade",
    "Empreendedorismo e Inovação",
    "Cálculo I",
    "Introdução à Computação",
    "Disciplina Curricular de Extensão 1"
],
    2:[
    "Processos de Software",
    "Álgebra Linear",
    "Programação II",
    "Matemática Discreta",
    "Metodologia Científica",
    "Cálculo II",
    "Disciplina Curricular de Extensão 2"
],
    3:[
    "Programação III",
    "Engenharia de Requisitos",
    "Projeto de Software",
    "Estatística I",
    "Banco de Dados",
    "Algoritmos e Estruturas de Dados",
    "Disciplina Curricular de Extensão 3"
],
    4:[
    "Gerência de Configuração",
    "Programação para Web",
    "Padrões de Projeto",
    "Estatística II",
    "Organização e Arquitetura de Computadores",
    "Teoria da Computação",
    "Disciplina Curricular de Extensão 4"
],
    5: [
    "Gerência de Projetos",
    "Programação para Dispositivos Móveis",
    "Verificação e Validação de Sistemas",
    "Projeto I",
    "Paradigmas de Linguagens de Programação",
    "Redes de Computadores",
    "Disciplina Curricular de Extensão 5"
],
    6: [
    "Arquitetura de Software",
    "Engenharia de Software Experimental",
    "Integração de Sistemas",
    "Inteligência Artificial",
    "Interação Humano-Computador",
    "Sistemas Operacionais",
    "Disciplina Curricular de Extensão 6"
],
    7:[
    "Qualidade de Software",
    "Segurança de Sistemas",
    "Projeto II",
    "Seminário em Engenharia de Software I",
    "Cadeira Eletiva",
    "Cadeira Eletiva",
    "Disciplina Curricular de Extensão 7"
],
    8:[
    "Manutenção e Evolução de Software",
    "Seminário em Engenharia de Software II",
    "Computação Gráfica e Sistemas Multimídia",
    "Cadeira Eletiva",
    "Cadeira Eletiva",
    "Disciplina Curricular de Extensão 8"
]
}

carga_horaria_por_periodo = {
    1: [60, 90, 30, 60, 60, 60, 45],
    2: [60, 60, 90, 60, 60, 60, 45],
    3: [90, 60, 60, 60, 60, 60, 45],
    4: [60, 60, 60, 60, 60, 60, 45],
    5: [60, 60, 60, 60, 60, 60, 45],
    6: [60, 60, 60, 60, 60, 60, 45],
    7: [60, 60, 60, 30, 60, 60, 45],
    8: [60, 30, 60, 60, 60, 30],
}

disciplinas_eletivas = [ "Libras", "Educação das Relações Étnico-Raciais", "Educação Ambiental", "Aprendizagem de Máquina e Reconhecimento de Padrões", "Tópicos Avançados em Computação Inteligente",
                         "Tópicos Avançados em Computação Teórica", "Tópicos Avançados em Engenharia de Software e Sistemas I", "Tópicos Avançados em Engenharia de Software e Sistemas II",
                         "Tópicos Avançados em Engenharia de Software e Sistemas III", "Tópicos Avançados em Engenharia de Software e Sistemas IV", "Tópicos Avançados em Gerenciamento de Dados e Informação",
                         "Engenharia de Software Educativo", "Tecnologias Assistivas"]


cursos = ["Engenharia de software", "Licenciatura de Computação", "Matemática"]


responsabilidade_professores = {
    "Geometria Analítica": ["Adauto Trigueiro", "Emanoel Francisco"],
    "Programação I": ["Adauto Trigueiro", "Emanoel Francisco"],
    "Computação Ética e Sociedade": ["Paulo Cavalcante", "Ariane Nunes"],
    "Empreendedorismo e Inovação": ["Emanoel Francisco", "Cleiton Soares"],
    "Cálculo I": ["Adauto Trigueiro", "Paulo Cavalcante"],
    "Introdução à Computação": ["Ariane Nunes", "Cleiton Soares"],
    "Disciplina Curricular de Extensão 1": ["Ariane Nunes", "Dâmocles Aurélio"],
    "Processos de Software": ["Dâmocles Aurélio", "Cleyton Mário"],
    "Álgebra Linear": ["Ariane Nunes", "Cleiton Soares"],
    "Programação II": ["Adauto Trigueiro", "Paulo Cavalcante"],
    "Matemática Discreta": ["Dâmocles Aurélio", "Cleiton Soares"],
    "Metodologia Científica": ["Emanoel Francisco", "Ariane Nunes"],
    "Cálculo II": ["Dâmocles Aurélio", "Cleyton Mário"],
    "Disciplina Curricular de Extensão 2": ["Cleyton Mário", "Ariane Nunes"],
    "Programação III": ["Adauto Trigueiro", "Paulo Cavalcante"],
    "Engenharia de Requisitos": ["Cleiton Soares", "Emanoel Francisco"],
    "Projeto de Software": ["Paulo Cavalcante", "Dâmocles Aurélio"],
    "Estatística I": ["Dâmocles Aurélio", "Cleiton Soares"],
    "Banco de Dados": ["Cleyton Mário", "Emanoel Francisco"],
    "Algoritmos e Estruturas de Dados": ["Adauto Trigueiro", "Ariane Nunes"],
    "Disciplina Curricular de Extensão 3": ["Cleiton Soares", "Paulo Cavalcante"],
    "Gerência de Configuração": ["Ariane Nunes", "Cleyton Mário"],
    "Programação para Web": ["Cleiton Soares", "Dâmocles Aurélio"],
    "Padrões de Projeto": ["Dâmocles Aurélio", "Ariane Nunes"],
    "Estatística II": ["Cleyton Mário", "Paulo Cavalcante"],
    "Organização e Arquitetura de Computadores": ["Ariane Nunes", "Cleiton Soares"],
    "Teoria da Computação": ["Adauto Trigueiro", "Dâmocles Aurélio"],
    "Disciplina Curricular de Extensão 4": ["Emanoel Francisco", "Cleiton Soares"],
    "Gerência de Projetos": ["Paulo Cavalcante", "Ariane Nunes"],
    "Programação para Dispositivos Móveis": ["Dâmocles Aurélio", "Cleiton Soares"],
    "Verificação e Validação de Sistemas": ["Cleiton Soares", "Dâmocles Aurélio"],
    "Projeto I": ["Adauto Trigueiro", "Emanoel Francisco"],
    "Paradigmas de Linguagens de Programação": ["Emanoel Francisco", "Paulo Cavalcante"],
    "Redes de Computadores": ["Paulo Cavalcante", "Adauto Trigueiro"],
    "Disciplina Curricular de Extensão 5": ["Cleiton Soares", "Dâmocles Aurélio"],
    "Arquitetura de Software": ["Dâmocles Aurélio", "Ariane Nunes"],
    "Engenharia de Software Experimental": ["Emanoel Francisco", "Cleiton Soares"],
    "Integração de Sistemas": ["Cleyton Mário", "Adauto Trigueiro"],
    "Inteligência Artificial": ["Paulo Cavalcante", "Emanoel Francisco"],
    "Interação Humano-Computador": ["Ariane Nunes", "Cleiton Soares"],
    "Sistemas Operacionais": ["Adauto Trigueiro", "Cleyton Mário"],
    "Disciplina Curricular de Extensão 6": ["Cleiton Soares", "Dâmocles Aurélio"],
    "Qualidade de Software": ["Dâmocles Aurélio", "Paulo Cavalcante"],
    "Segurança de Sistemas": ["Paulo Cavalcante", "Ariane Nunes"],
    "Projeto II": ["Ariane Nunes", "Cleyton Mário"],
    "Seminário em Engenharia de Software I": ["Cleyton Mário", "Dâmocles Aurélio"],
    "Disciplina Curricular de Extensão 7": ["Dâmocles Aurélio", "Cleiton Soares"],
    "Cadeira Eletiva": ["Paulo Cavalcante", "Emanoel Francisco"],
    "Manutenção e Evolução de Software": ["Adauto Trigueiro", "Emanoel Francisco"],
    "Seminário em Engenharia de Software II": ["Emanoel Francisco", "Cleyton Mário"],
    "Computação Gráfica e Sistemas Multimídia": ["Cleiton Soares", "Dâmocles Aurélio"],
    "Disciplina Curricular de Extensão 8": ["Paulo Cavalcante", "Ariane Nunes"]
}