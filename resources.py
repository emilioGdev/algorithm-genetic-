# Defina os dados iniciais
import random


professores = ["Adauto Trigueiro", "Aêda Monalliza", "Ariane Nunes", "Brunno Wagner", "Cleiton Soares", "Cleyton Mário",
               "Cleverton Anderson", "Emanoel Francisco", "Erton Wagner", "Ewerton Menezes", "Fellipe Anchiêta", "Helaine Solange",
               "Higor Ricardo", "Ivaldir Honório", "Victor Afonso", "Maurício Costa", "Milton Perceus", "Paulo Cavalcante", "Dâmocles Aurélio"]

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
        "Segunda": ["7h30", "8h20", "9h10"],
        "Terça": [],
        "Quarta": ["14h30", "15h30", "16h30"],
        "Quinta": ["14h30", "15h30", "16h30"],
        "Sexta": []
    },
    "Aêda Monalliza": {
        "Segunda": ["7h30", "8h20", "9h10"],
        "Terça": [],
        "Quarta": ["7h30", "8h20"],
        "Quinta": [],
        "Sexta": ["10h50", "11h40"],
    },
    "Ariane Nunes": {
        "Segunda": ["9h10", "10h00"],
        "Terça": ["14h30", "15h30", "16h30"],
        "Quarta": [],
        "Quinta": ["7h30", "8h20", "9h10", "10h50"],
        "Sexta": []
    },
    "Brunno Wagner": {
        "Segunda": ["7h30", "8h20", "9h10"],
        "Terça": [],
        "Quarta": ["10h50", "11h40"],
        "Quinta": [],
        "Sexta": ["10h50", "11h40"],
    },
    "Cleiton Soares": {
        "Segunda": ["8h20"],
        "Terça": [],
        "Quarta": ["14h30"],
        "Quinta": [],
        "Sexta": ["7h30", "8h20", "9h10", "10h50"],
    },
    "Cleyton Mário": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h50"],
        "Quarta": [],
        "Quinta": ["7h30", "8h20", "9h10", "10h50"],
        "Sexta": []
    },
    "Cleverton Anderson": {
        "Segunda": ["7h30", "8h20", "9h10", "10h50"],
        "Terça": ["7h30", "8h20", "9h10", "10h50"],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    },
    "Emanoel Francisco": {
        "Segunda": [],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h50"],
        "Quinta": [],
        "Sexta": ["7h30", "8h20", "9h10", "10h50"]
    },
    "Erton Wagner": {
        "Segunda": ["7h30", "8h20", "9h10"],
        "Terça": [],
        "Quarta": [],
        "Quinta": [],
        "Sexta": ["7h30", "8h20", "9h10", "10h50"]
    },
    "Ewerton Menezes": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h50"],
        "Quarta": ["7h30", "8h20", "9h10", "10h50"],
        "Quinta": [],
        "Sexta": []
    },
    "Fellipe Anchiêta": {
        "Segunda": [],
        "Terça": ["7h30", "8h20", "9h10", "10h50"],
        "Quarta": ["14h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h50"],
        "Sexta": ["16h30"]
    },
    "Helaine Solange": {
        "Segunda": ["7h30", "8h20", "9h10", "10h50"],
        "Terça": ["8h20"],
        "Quarta": ["7h30", "8h20", "9h10", "10h50"],
        "Quinta": ["10h00"],
        "Sexta": []
    },
    "Higor Ricardo": {
        "Segunda": ["15h30"],
        "Terça": ["7h30", "8h20", "9h10", "10h50"],
        "Quarta": ["7h30"],
        "Quinta": ["7h30", "8h20", "9h10", "10h50"],
        "Sexta": []
    },
    "Ivaldir Honório": {
        "Segunda": ["7h30", "8h20", "9h10"],
        "Terça": ["7h30", "8h20", "9h10", "10h50"],
        "Quarta": [],
        "Quinta": ["8h20"],
        "Sexta": ["9h10"]
    },
    "Victor Afonso": {
        "Segunda": ["7h30", "8h20", "9h10", "10h50"],
        "Terça": [],
        "Quarta": ["7h30", "8h20", "9h10", "10h50"],
        "Quinta": ["7h30"],
        "Sexta": []
    },
    "Maurício Costa": {
        "Segunda": ["13h30"],
        "Terça": ["7h30", "8h20", "9h10", "10h50"],
        "Quarta": ["7h30", "8h20", "9h10", "10h50"],
        "Quinta": [],
        "Sexta": ["10h50"]
    },
    "Milton Perceus": {
        "Segunda": [],
        "Terça": ["16h30"],
        "Quarta": [],
        "Quinta": [],
        "Sexta": []
    },
    "Paulo Cavalcante": {
        "Segunda": ["7h30", "8h20", "9h10"],
        "Terça": [],
        "Quarta": ["10h00"],
        "Quinta": [],
        "Sexta": ["15h30"]
    },
    "Dâmocles Aurélio": {
        "Segunda": ["9h10"],
        "Terça": [],
        "Quarta": ["8h20"],
        "Quinta": [],
        "Sexta": ["7h30"]
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
    "Programação II": ["Adauto Trigueiro", "Paulo Cavalcante", "Emanoel Francisco", "Cleiton Soares"],
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