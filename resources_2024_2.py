
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
        "Terça": [],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    },
    "Aêda Monalliza": {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": [],
        "Sexta": [],
    },
    "Ariane Nunes": {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": [],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"]
    },
    "Brunno Wagner": {
        "Segunda": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": [],
        "Quinta": [],
        "Sexta": [],
    },
    "Cleiton Martins": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": [],
    },
    "Cleverton Silva": {
        "Segunda": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    },
    "Emanoel Francisco": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": [],
        "Quinta": [],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"]
    },
    "Ewerton Mendonça": {
        "Segunda": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": [],
        "Sexta": []
    },
    "Felipe Barreto": {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    },
    "Helaine Barreiros": {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    },
    "Ivaldir Honório": {
        "Segunda": [],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": [],
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
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": [],
        "Sexta": []
    },
    "Geovany Fernandes": {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": []
    },
    "Renato Silvestre": {
        "Segunda": [],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": []
    },
    "Elvis Melo": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": []
    },
    "Elisson Rocha": {
        "Segunda": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": [],
        "Sexta": []
    },
    "Marcello Mendonça": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": []
    },
    "Eraylson Galdino": {
        "Segunda": [],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"]
    },
    "Janaína Barros": {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    },
    "Mariana Maia": {
        "Segunda": [],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Sexta": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"]
    },
    "Paulo Júnior": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h00", "10h50", "11h40", "13h30", "14h30", "15h30", "16h30"],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    }
}




responsabilidade_professores = {

    "Processos de Software": ["Brunno Wagner","Cleverton Silva"],
    "Álgebra Linear": ["Renato Silvestre"],
    "Programação II": ["Emanoel Francisco"],
    "Matemática Discreta": ["Geovany Fernandes","Renato Silvestre"],
    "Metodologia Científica": ["Ivaldir Honório"],
    "Cálculo II": ["Paulo Júnior"],
    "Disciplina Curricular de Extensão 2": ["Ivaldir Honório"],

    "Gerência de Configuração": ["Ewerton Mendonça"],
    "Programação para Web": ["Elisson Rocha","Emanoel Francisco"],
    "Padrões de Projeto": ["Ewerton Mendonça"],
    "Estatística II": ["Milton Perceus","Paulo Júnior"],
    "Organização e Arquitetura de Computadores": ["Cleiton Martins"],
    "Teoria da Computação": ["Brunno Wagner", "Milton Perceus"],
    "Disciplina Curricular de Extensão 4": ["Cleverton Silva"],

    "Arquitetura de Software": ["Brunno Wagner", "Adauto Trigueiro"],
    "Engenharia de Software Experimental": ["Adauto Trigueiro"],
    "Integração de Sistemas": ["Elisson Rocha","Adauto Trigueiro"],
    "Inteligência Artificial": ["Eraylson Galdino"],
    "Interação Humano-Computador": ["Ariane Nunes"],
    "Sistemas Operacionais": ["Cleiton Martins", "Adauto Trigueiro"],
    "Disciplina Curricular de Extensão 6": ["Eraylson Galdino"],

    "Manutenção e Evolução de Software": ["Victor Santos","Mariana Maia"],
    "Seminário em Engenharia de Software II": ["Marcello Mendonça"],
    "Computação Gráfica e Sistemas Multimídia": ["Ewerton Mendonça","Eraylson Galdino"],
    "Tópicos Avançados em Engenharia de Software e Sistemas I": ["Victor Santos","Marcello Mendonça"],
    "Tópicos Avançados em Engenharia de Software e Sistemas IV": ["Mariana Maia"],
    "Aprendizagem de Máquina e Reconhecimento de Padrões": ["Victor Santos"],
    "Tópicos Avançados em Computação Inteligente": ["Elisson Rocha", "Ariane Nunes"],
    "Disciplina Curricular de Extensão 8": ["Mariana Maia","Renato Silvestre"],
}


disciplina_por_periodo = {
    2:[
    {"nome": "Processos de Software", "lab": False},
    {"nome": "Álgebra Linear", "lab": False},
    {"nome": "Programação II", "lab": True},
    {"nome": "Matemática Discreta", "lab": True},
    {"nome": "Metodologia Científica", "lab": False},
    {"nome": "Cálculo II", "lab": False},
    {"nome": "Disciplina Curricular de Extensão 2", "lab": True}
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
    8:[
    {"nome": "Manutenção e Evolução de Software", "lab": True},
    {"nome": "Seminário em Engenharia de Software II", "lab": False},
    {"nome": "Computação Gráfica e Sistemas Multimídia", "lab": True},
    {"nome": "Tópicos Avançados em Engenharia de Software e Sistemas I", "lab": False},
    {"nome": "Tópicos Avançados em Engenharia de Software e Sistemas IV", "lab": False},
    {"nome": "Aprendizagem de Máquina e Reconhecimento de Padrões", "lab": True},
    {"nome": "Tópicos Avançados em Computação Inteligente", "lab": True},
    {"nome": "Disciplina Curricular de Extensão 8", "lab": False}
]
}

carga_horaria_por_periodo = {
    2: [60, 60, 90, 60, 60, 60, 45],
    4: [60, 60, 60, 60, 60, 60, 45],
    6: [60, 60, 60, 60, 60, 60, 45],
    8: [60, 30, 60, 60, 60, 60, 60, 45],
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

