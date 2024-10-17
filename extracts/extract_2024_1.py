import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from validation.penalities import calcular_fitness


horario1 = {
    1: {
        'Segunda': [
            [], [], [('Computação Ética e Sociedade', 'Cleverton Silva', None)],
             [('Computação Ética e Sociedade', 'Cleverton Silva', None)], 
            [('Programação I', 'Adauto Trigueiro', 'windows')],
             [('Programação I', 'Adauto Trigueiro', 'windows')], 
            [], [], [], [],   
        ],
        'Terça': [
            [], [], [('Introdução à Computação', 'Cleverton Silva', None)],
            [('Introdução à Computação', 'Cleverton Silva', None)],
            [('Introdução à Computação', 'Cleverton Silva', None)],
            [('Introdução à Computação', 'Cleverton Silva', None)],
            [], [], [], [],  
        ],
        'Quarta': [
            [], [], [('Empreendedorismo e Inovação', 'Ivaldir Honório', None)],
            [('Empreendedorismo e Inovação', 'Ivaldir Honório', None)],
            [('Empreendedorismo e Inovação', 'Ivaldir Honório', None)],
            [('Empreendedorismo e Inovação', 'Ivaldir Honório', None)],
            [('Geometria Analítica', 'Renato Silvestre', None)],
            [('Geometria Analítica', 'Renato Silvestre', None)],
            [('Geometria Analítica', 'Renato Silvestre', None)],
            [('Geometria Analítica', 'Renato Silvestre', None)],

        ],
        'Quinta': [
            [], [],  [('Programação I', 'Adauto Trigueiro', 'windows')],
            [('Programação I', 'Adauto Trigueiro', 'windows')],
            [('Programação I', 'Adauto Trigueiro', 'windows')],
            [('Programação I', 'Adauto Trigueiro', 'windows')],
            [], [], [], [], 
        ],
        'Sexta': [
            [('Cálculo I', 'Janaína Barros', None)],
            [('Cálculo I', 'Janaína Barros', None)],
            [('Cálculo I', 'Janaína Barros', None)],
            [('Cálculo I', 'Janaína Barros', None)],
            [('Disciplina Curricular de Extensão 1', 'Mariana Maia', None)],
            [('Disciplina Curricular de Extensão 1', 'Mariana Maia', None)], [], [], [], [],
        ]
    },
    3: {
        'Segunda': [
            [], [], [('Algoritmos e Estruturas de Dados', 'Emanoel Francisco', 'linux')],
            [('Algoritmos e Estruturas de Dados', 'Emanoel Francisco', 'linux')],
            [('Algoritmos e Estruturas de Dados', 'Emanoel Francisco', 'linux')],
            [('Algoritmos e Estruturas de Dados', 'Emanoel Francisco', 'linux')], [], [], [], []
        ],
        'Terça': [
            [], [], [('Banco de Dados', 'Victor Santos', 'linux')],
            [('Banco de Dados', 'Victor Santos', 'linux')],
            [('Banco de Dados', 'Victor Santos', 'linux')],
            [('Banco de Dados', 'Victor Santos', 'linux')],
            [], [], [], [], 
        ],
        'Quarta': [
            [('Disciplina Curricular de Extensão 3', 'Victor Santos', None)],
            [('Disciplina Curricular de Extensão 3', 'Victor Santos', None)],
            [('Programação III', 'Emanoel Francisco', 'linux')],
            [('Programação III', 'Emanoel Francisco', 'linux')],
            [('Programação III', 'Emanoel Francisco', 'linux')],
            [('Programação III', 'Emanoel Francisco', 'linux')],
            [('Estatística I', 'Milton Perceus', None)],
            [('Estatística I', 'Milton Perceus', None)],
            [('Estatística I', 'Milton Perceus', None)],
            [('Estatística I', 'Milton Perceus', None)],

        ],
        'Quinta': [
            [('Projeto de Software', 'Ewerton Mendonça', None)],
            [('Projeto de Software', 'Ewerton Mendonça', None)],
            [('Projeto de Software', 'Ewerton Mendonça', None)],
            [('Projeto de Software', 'Ewerton Mendonça', None)],
            [('Programação III', 'Emanoel Francisco', 'linux')],
            [('Programação III', 'Emanoel Francisco', 'linux')], [], [], [], [],
        ],
        'Sexta': [
            [], [],
            [('Engenharia de Requisitos', 'Mariana Maia', None)],
            [('Engenharia de Requisitos', 'Mariana Maia', None)],
            [('Engenharia de Requisitos', 'Mariana Maia', None)],
            [('Engenharia de Requisitos', 'Mariana Maia', None)],
             [], [], [], [], 
        ]
    },
    5: {
        'Segunda': [
            [('Disciplina Curricular de Extensão 5', 'Cleverton Silva', None)],
            [('Disciplina Curricular de Extensão 5', 'Cleverton Silva', None)],
            [('Verificação e Validação de Sistemas', 'Brunno Wagner', None)],
            [('Verificação e Validação de Sistemas', 'Brunno Wagner', None)],
            [('Verificação e Validação de Sistemas', 'Brunno Wagner', None)],
            [('Verificação e Validação de Sistemas', 'Brunno Wagner', None)], [], [], [], [],
        ],
        'Terça': [
            [], [],
            [('Gerência de Projetos', 'Aêda Monalliza', None)],
            [('Gerência de Projetos', 'Aêda Monalliza', None)],
            [('Gerência de Projetos', 'Aêda Monalliza', None)],
            [('Gerência de Projetos', 'Aêda Monalliza', None)],
            [('Redes de Computadores', 'Cleiton Martins', 'windows')],
            [('Redes de Computadores', 'Cleiton Martins', 'windows')],
            [('Redes de Computadores', 'Cleiton Martins', 'windows')],
            [('Redes de Computadores', 'Cleiton Martins', 'windows')]
        ],
        'Quarta': [
            [('Programação para Dispositivos Móveis', 'Elisson Rocha', 'windows')],
            [('Programação para Dispositivos Móveis', 'Elisson Rocha', 'windows')],
            [('Programação para Dispositivos Móveis', 'Elisson Rocha', 'windows')],
            [('Programação para Dispositivos Móveis', 'Elisson Rocha', 'windows')],
            [], [], [], [], [], []
        ],
        'Quinta': [
            [('Projeto I', 'Marcello Mendonça', None)],
            [('Projeto I', 'Marcello Mendonça', None)],
            [('Projeto I', 'Marcello Mendonça', None)],
            [('Projeto I', 'Marcello Mendonça', None)],
            [], [], [], [], [], [], 
        ],
        'Sexta': [
            [('Paradigmas de Linguagens de Programação', 'Eraylson Galdino', 'windows')],
            [('Paradigmas de Linguagens de Programação', 'Eraylson Galdino', 'windows')],
            [('Paradigmas de Linguagens de Programação', 'Eraylson Galdino', 'windows')],
            [('Paradigmas de Linguagens de Programação', 'Eraylson Galdino', 'windows')],
            [], [], [], [], [], []
        ]
    },
    7: {
        'Segunda': [
            [('Segurança de Sistemas', 'Cleiton Martins', 'windows')],
            [('Segurança de Sistemas', 'Cleiton Martins', 'windows')],
            [('Segurança de Sistemas', 'Cleiton Martins', 'windows')],
            [('Segurança de Sistemas', 'Cleiton Martins', 'windows')],
            [('Disciplina Curricular de Extensão 7', 'Cleverton Silva', 'windows')],
            [('Disciplina Curricular de Extensão 7', 'Cleverton Silva', 'windows')],

            [], [], [], [], 
        ],
        'Terça': [
            [('Qualidade de Software', 'Brunno Wagner', None)],
            [('Qualidade de Software', 'Brunno Wagner', None)],
            [('Qualidade de Software', 'Brunno Wagner', None)],
            [('Qualidade de Software', 'Brunno Wagner', None)],
            [], [], [], [], [], [], 
        ],
        'Quarta': [
            [], [],
            [('Cadeira Eletiva', 'Ewerton Mendonça', None)],
            [('Cadeira Eletiva', 'Ewerton Mendonça', None)],
            [('Cadeira Eletiva', 'Ewerton Mendonça', None)],
            [('Cadeira Eletiva', 'Ewerton Mendonça', None)], [], [], [], [],
        ],
        'Quinta': [
            [('Seminário em Engenharia de Software I', 'Marcello Mendonça', None)],
            [('Seminário em Engenharia de Software I', 'Marcello Mendonça', None)],
            [('Projeto II', 'Mariana Maia', 'windows')],
            [('Projeto II', 'Mariana Maia', 'windows')],
            [('Projeto II', 'Mariana Maia', 'windows')],
            [('Projeto II', 'Mariana Maia', 'windows')], [], [], [], [],
        ],
        'Sexta': [
            [], [],
            [('Cadeira Eletiva', 'Ariane Nunes', 'linux')],
            [('Cadeira Eletiva', 'Ariane Nunes', 'linux')],
            [('Cadeira Eletiva', 'Ariane Nunes', 'linux')],
            [('Cadeira Eletiva', 'Ariane Nunes', 'linux')],
            [], [], [], [], 
        ]
    }
}


fitness_1 = calcular_fitness(horario1)
print(fitness_1)
