import random

professores = ["Brunno Wagner",
"Geovany Fernandes",
"Emanoel Barreiros",
"Renato Silvestre",
"Ivaldir Honório",
"Adauto Trigueiro",
"Elvis Melo",
"Cleverton Silva",
"Ewerton Mendonça",
"Milton Perceus",
"Helaine Barreiros",
"Cleiton Martins",
"Elisson Rocha",
"Marcello Mendonça",
"Eraylson Galdino",
"Ariane Nunes",
"Victor Santos",
"Felipe Barreto",
"Aêda Monalliza",
"Janaína Barros",
"Mariana Maia"]

#Definindo a disponibilidade dos professores

num_periodos = 4 # Só vão existir 4 períodos por semestre. Exemplo 1: 1°, 3°, 5° e 7°; Exemplo 2: 2°, 4°, 6° e 8° - Só tem essas 2 opções e o usuário que vai escolher qual ele quer.
num_dias_da_semana = 5
slots_por_dia = 10  # 6 de Manhã e 4 de Tarde, e cada aula durá 50 minutos. As aulas pela manhã vão de 7h30 até 12h30, e pela tarde de 13h30 até 17h30
total_cadeiras_por_periodo = [7, 7, 7, 7, 7, 7, 7, 6]  # Número de cadeiras por período
dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
horarios_manha = ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40"]
horarios_tarde = ["13h30", "14h30", "15h30", "16h30"]


professores_horario = {
    "Adauto Trigueiro": {
        "Segunda": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    },
    "Aêda Monalliza": {
        "Segunda": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40"],
        "Quarta": [],
        "Quinta": [],
        "Sexta": [],
    },
    "Ariane Nunes": {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": ["13h30", "14h30", "15h30", "16h30"],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"]
    },
    "Brunno Wagner": {
        "Segunda": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": [],
        "Sexta": [],
    },
    "Cleiton Martins": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": [],
        "Sexta": [],
    },
    "Cleverton Silva": {
        "Segunda": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40"],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40"],
        "Quarta": [],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40"],
        "Sexta": []
    },
    "Emanoel Francisco": {
        "Segunda": [],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40"],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40"]
    },
    "Ewerton Mendonça": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": []
    },
    "Felipe Barreto": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h50"],
        "Quarta": ["13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["13h30", "14h30", "15h30", "16h30"],
        "Sexta": []
    },
    "Helaine Barreiros": {
        "Segunda": [],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"]
    },
    "Ivaldir Honório": {
        "Segunda": [],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": []
    },
    "Victor Santos": {
        "Segunda": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": [],
        "Sexta": []
    },
    "Milton Perceus": {
        "Segunda": [],
        "Terça": ["9h10", "10h00", "10h50", "11h40"],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    },
    "Geovany Fernandes": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h00"],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    },
    "Renato Silvestre": {
        "Segunda": [],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h00"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00"],
        "Sexta": []
    },
    "Elvis Melo": {
        "Segunda": [],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"]
    },
    "Elisson Rocha": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": []
    },
    "Marcello Mendonça": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": [],
        "Sexta": []
    },
    "Eraylson Galdino": {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"]
    },
    "Janaína Barros": {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": [],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", ]
    },
    "Mariana Maia": {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"]
    }
}

disciplina_por_periodo = {
    1:[
    {"nome": "Geometria Analítica", "lab": False},
    {"nome": "Programação I", "lab": True},
    {"nome": "Computação Ética e Sociedade", "lab": False},
    {"nome": "Empreendedorismo e Inovação", "lab": False},
    {"nome": "Cálculo I", "lab": False},
    {"nome": "Introdução à Computação", "lab": True},
    {"nome": "Disciplina Curricular de Extensão 1", "lab": True}
],
    2:[
    {"nome": "Processos de Software", "lab": False},
    {"nome": "Álgebra Linear", "lab": False},
    {"nome": "Programação II", "lab": True},
    {"nome": "Matemática Discreta", "lab": True},
    {"nome": "Metodologia Científica", "lab": False},
    {"nome": "Cálculo II", "lab": False},
    {"nome": "Disciplina Curricular de Extensão 2", "lab": True}
],
    3:[
    {"nome": "Programação III", "lab": True},
    {"nome": "Engenharia de Requisitos", "lab": False},
    {"nome": "Projeto de Software", "lab": False},
    {"nome": "Estatística I", "lab": False},
    {"nome": "Banco de Dados", "lab": True},
    {"nome": "Algoritmos e Estruturas de Dados", "lab": True},
    {"nome": "Disciplina Curricular de Extensão 3", "lab": True}
],
    4:[
    {"nome": "Gerência de Configuração", "lab": True},
    {"nome": "Programação para Web", "lab": True},
    {"nome": "Padrões de Projeto", "lab": True},
    {"nome": "Estatística II", "lab": False},
    {"nome": "Organização e Arquitetura de Computadores", "lab": False},
    {"nome": "Teoria da Computação", "lab": False},
    {"nome": "Disciplina Curricular de Extensão 4", "lab": False}
],
    5: [
    {"nome": "Gerência de Projetos", "lab": False},
    {"nome": "Programação para Dispositivos Móveis", "lab": True},
    {"nome": "Verificação e Validação de Sistemas", "lab": False},
    {"nome": "Projeto I", "lab": True},
    {"nome": "Paradigmas de Linguagens de Programação", "lab": False},
    {"nome": "Redes de Computadores", "lab": False},
    {"nome": "Disciplina Curricular de Extensão 5", "lab": False}
],
    6: [
    {"nome": "Arquitetura de Software", "lab": True},
    {"nome": "Engenharia de Software Experimental", "lab": False},
    {"nome": "Integração de Sistemas", "lab": False},
    {"nome": "Inteligência Artificial", "lab": True},
    {"nome": "Interação Humano-Computador", "lab": False},
    {"nome": "Sistemas Operacionais", "lab": False},
    {"nome": "Disciplina Curricular de Extensão 6", "lab": False}
],
    7:[
    {"nome": "Qualidade de Software", "lab": False},
    {"nome": "Segurança de Sistemas", "lab": False},
    {"nome": "Projeto II", "lab": True},
    {"nome": "Seminário em Engenharia de Software I", "lab": False},
    {"nome": "Cadeira Eletiva", "lab": False},
    {"nome": "Cadeira Eletiva", "lab": False},
    {"nome": "Disciplina Curricular de Extensão 7", "lab": False}
],
    8:[
    {"nome": "Manutenção e Evolução de Software", "lab": True},
    {"nome": "Seminário em Engenharia de Software II", "lab": False},
    {"nome": "Computação Gráfica e Sistemas Multimídia", "lab": True},
    {"nome": "Cadeira Eletiva", "lab": False},
    {"nome": "Cadeira Eletiva", "lab": False},
    {"nome": "Cadeira Eletiva", "lab": False},
    {"nome": "Cadeira Eletiva", "lab": False},
    {"nome": "Disciplina Curricular de Extensão 8", "lab": False}
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
    8: [60, 30, 60, 60, 60, 60, 60, 30],
}


disciplinas_eletivas = [ "Libras", "Educação das Relações Étnico-Raciais", "Educação Ambiental", "Aprendizagem de Máquina e Reconhecimento de Padrões", "Tópicos Avançados em Computação Inteligente",
                         "Tópicos Avançados em Computação Teórica", "Tópicos Avançados em Engenharia de Software e Sistemas I", "Tópicos Avançados em Engenharia de Software e Sistemas II",
                         "Tópicos Avançados em Engenharia de Software e Sistemas III", "Tópicos Avançados em Engenharia de Software e Sistemas IV", "Tópicos Avançados em Gerenciamento de Dados e Informação",
                         "Engenharia de Software Educativo", "Tecnologias Assistivas"]


cursos = ["Engenharia de software", "Licenciatura de Computação", "Matemática"]

responsabilidade_professores = {
    "Geometria Analítica": ["Renato Silvestre"],
    "Programação I": ["Adauto Trigueiro", "Elisson Rocha"],
    "Computação Ética e Sociedade": ["Ariane Nunes", "Cleverton Silva"],
    "Empreendedorismo e Inovação": ["Marcello Mendonça", "Ivaldir Honório"],
    "Cálculo I": ["Janaína Barros"],
    "Introdução à Computação": ["Cleverton Silva", "Elvis Melo"],
    "Disciplina Curricular de Extensão 1": ["Cleverton Silva", "Elvis Melo", "Ariane Nunes"],
    "Processos de Software": ["Brunno Wagner", "Ewerton Mendonça"],
    "Álgebra Linear": ["Renato Silvestre"],
    "Programação II": ["Emanoel Francisco", "Aêda Monalliza", "Elisson Rocha"],
    "Matemática Discreta": ["Geovany Fernandes"],
    "Metodologia Científica": ["Ivaldir Honório", "Elvis Melo", "Marcello Mendonça"],
    "Cálculo II": ["Felipe Barreto", "Paulo Júnior"],
    "Disciplina Curricular de Extensão 2": ["Cleverton Silva", "Adauto Trigueiro", "Elisson Rocha", "Ivaldir Honório"],
    "Programação III": ["Emanoel Francisco"],
    "Engenharia de Requisitos": ["Mariana Maia"],
    "Projeto de Software": ["Ewerton Mendonça"],
    "Estatística I": ["Milton Perceus"],
    "Banco de Dados": ["Victor Santos", "Elisson Rocha"],
    "Algoritmos e Estruturas de Dados": ["Victor Santos", "Elisson Rocha", "Eraylson Galdino"],
    "Disciplina Curricular de Extensão 3": ["Cleverton Silva", "Adauto Trigueiro", "Elisson Rocha", "Ivaldir Honório"],
    "Gerência de Configuração": ["Ewerton Mendonça"],
    "Programação para Web": ["Helaine Barreiros", "Elisson Rocha", "Ewerton Mendonça"],
    "Padrões de Projeto": ["Ewerton Mendonça", "Brunno Wagner"],
    "Estatística II": ["Milton Perceus"],
    "Organização e Arquitetura de Computadores": ["Cleiton Martins"],
    "Teoria da Computação": ["Brunno Wagner"],
    "Disciplina Curricular de Extensão 4": ["Brunno Wagner", "Cleiton Martins", "Ewerton Mendonça", "Elvis Melo"],
    "Gerência de Projetos": ["Aêda Monalliza", "Helaine Barreiros"],
    "Programação para Dispositivos Móveis": ["Elisson Rocha", "Ewerton Mendonça"],
    "Verificação e Validação de Sistemas": ["Brunno Wagner"],
    "Projeto I": ["Marcello Mendonça", "Helaine Barreiros"],
    "Paradigmas de Linguagens de Programação": ["Emanoel Francisco", "Eraylson Galdino"],
    "Redes de Computadores": ["Cleiton Martins"],
    "Disciplina Curricular de Extensão 5": ["Cleverton Silva", "Brunno Wagner", "Cleiton Martins", "Ewerton Mendonça", "Elvis Melo"],
    "Arquitetura de Software": ["Brunno Wagner"],
    "Engenharia de Software Experimental": ["Adauto Trigueiro"],
    "Integração de Sistemas": ["Elisson Rocha"],
    "Inteligência Artificial": ["Victor Santos", "Elisson Rocha", "Eraylson Galdino"],
    "Interação Humano-Computador": ["Ariane Nunes"],
    "Sistemas Operacionais": ["Cleiton Martins"],
    "Disciplina Curricular de Extensão 6": ["Cleverton Silva", "Brunno Wagner", "Cleiton Martins", "Ewerton Mendonça", "Elvis Melo"],
    "Qualidade de Software": ["Brunno Wagner"],
    "Segurança de Sistemas": ["Cleiton Martins"],
    "Projeto II": ["Mariana Maia", "Marcello Mendonça"],
    "Seminário em Engenharia de Software I": ["Marcello Mendonça", "Elvis Melo", "Victor Ferreira"],
    "Disciplina Curricular de Extensão 7": ["Cleverton Silva", "Brunno Wagner", "Cleiton Martins", "Ewerton Mendonça", "Elvis Melo"],
    "Cadeira Eletiva": ["Victor Santos", "Elisson Rocha", "Eraylson Galdino"],
    "Manutenção e Evolução de Software": ["Victor Santos"],
    "Seminário em Engenharia de Software II": ["Marcello Mendonça", "Elvis Melo", "Victor Ferreira"],
    "Computação Gráfica e Sistemas Multimídia": ["Ewerton Mendonça"],
    "Disciplina Curricular de Extensão 8": ["Cleverton Silva", "Brunno Wagner", "Cleiton Martins", "Ewerton Mendonça", "Elvis Melo"],
}

professores_info = {
    "Brunno Wagner": {"tipo": "normal", "max_horas": 16},
    "Cleverton Silva": {"tipo": "normal", "max_horas": 16},
    "Victor Santos": {"tipo": "normal", "max_horas": 16},
    "Elisson Rocha": {"tipo": "normal", "max_horas": 16},
    "Ewerton Mendonça": {"tipo": "normal", "max_horas": 16},
    "Ariane Nunes": {"tipo": "gestao", "max_horas": 16},
    "Aêda Monalliza": {"tipo": "gestao", "max_horas": 16},
    "Adauto Trigueiro": {"tipo": "gestao", "max_horas": 16},
    "Emanoel Francisco": {"tipo": "gestao", "max_horas": 16},
    "Cleiton Martins": {"tipo": "normal", "max_horas": 16},
    "Eraylson Galdino": {"tipo": "gestao", "max_horas": 16},
    "Helaine Barreiros": {"tipo": "afastamento", "max_horas": 16},
    "Ivaldir Honório": {"tipo": "gestao", "max_horas": 16},
    "Mariana Maia": {"tipo": "normal", "max_horas": 16},
    "Elvis Melo": {"tipo": "normal", "max_horas": 16},
    "Felipe Anchieta": {"tipo": "normal", "max_horas": 16},
    "Renato Silvestre": {"tipo": "normal", "max_horas": 16},
    "Marcello Mendonça": {"tipo": "normal", "max_horas": 16},
    "Janaína Barros": {"tipo": "normal", "max_horas": 16},
    "Milton Perceus": {"tipo": "normal", "max_horas": 16},
    "Geovany Fernandes": {"tipo": "normal", "max_horas": 16}, 
    "Felipe Barreto": {"tipo": "normal", "max_horas": 16},
    "Paulo Júnior":{"tipo": "normal", "max_horas": 16}
}

