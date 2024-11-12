import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from validation.penalities import calcular_fitness


horario_2 = {
    2: { 
        'Segunda': [
            [],  [], 
            [('Processos de Software', 'Brunno Wagner', None)],
            [('Processos de Software', 'Brunno Wagner', None)],
            [('Processos de Software', 'Brunno Wagner', None)],
            [('Processos de Software', 'Brunno Wagner', None)],  
            [], [], [],  [],
        ],
        'Terça': [
            [('Cálculo II', 'Paulo Júnior', None)],
            [('Cálculo II', 'Paulo Júnior', None)],
            [('Cálculo II', 'Paulo Júnior', None)],
            [('Cálculo II', 'Paulo Júnior', None)], 
            [('Programação II', 'Emanoel Francisco', 'linux')],
            [('Programação II', 'Emanoel Francisco','linux')],   
            [], [],  [],  [],   
        ],
        'Quarta': [
            [('Álgebra Linear', 'Renato Silvestre', None)],
            [('Álgebra Linear', 'Renato Silvestre', None)],  
            [('Metodologia Científica', 'Ivaldir Honório', None)],
            [('Metodologia Científica', 'Ivaldir Honório', None)],
            [('Metodologia Científica', 'Ivaldir Honório', None)],
            [('Metodologia Científica', 'Ivaldir Honório', None)], 
            [('Disciplina Curricular de Extensão 2', 'Ivaldir Honório', None)],
            [('Disciplina Curricular de Extensão 2', 'Ivaldir Honório', None)],
            [], [], 
        ],
        'Quinta': [
            [('Álgebra Linear', 'Renato Silvestre', None)],
            [('Álgebra Linear', 'Renato Silvestre', None)], 
            [('Matemática Discreta', 'Geovany Fernandes', None)],
            [('Matemática Discreta', 'Geovany Fernandes', None)], 
            [('Matemática Discreta', 'Geovany Fernandes', None)], 
            [('Matemática Discreta', 'Geovany Fernandes', None)],  
            [], [], [], [],
        ],
        'Sexta': [
            [],  [],  
            [('Programação II', 'Emanoel Francisco', None)],
            [('Programação II', 'Emanoel Francisco', None)],
            [('Programação II', 'Emanoel Francisco', None)],
            [('Programação II', 'Emanoel Francisco', None)],  
            [],  [],  [],  [],  
        ]
    },
    4: {  
        'Segunda': [
            [], [], 
            [('Organização e Arquitetura de Computadores', 'Cleiton Martins', None)],
            [('Organização e Arquitetura de Computadores', 'Cleiton Martins', None)],
            [('Organização e Arquitetura de Computadores', 'Cleiton Martins', None)],
            [('Organização e Arquitetura de Computadores', 'Cleiton Martins', None)],  
            [], [], [], [], 
        ],
        'Terça': [
            [('Teoria da Computação', 'Brunno Wagner', None)],
            [('Teoria da Computação', 'Brunno Wagner', None)],
            [('Teoria da Computação', 'Brunno Wagner', None)],
            [('Teoria da Computação', 'Brunno Wagner', None)],  
            [('Disciplina Curricular de Extensão 4', 'Cleverton Silva', None)],
            [('Disciplina Curricular de Extensão 4', 'Cleverton Silva', None)],    
            [('Gerência de Configuração', 'Ewerton Mendonça', None)],
            [('Gerência de Configuração', 'Ewerton Mendonça', None)],
            [('Gerência de Configuração', 'Ewerton Mendonça', None)],
            [('Gerência de Configuração', 'Ewerton Mendonça', None)],  
        ],
        'Quarta': [
            [('Padrões de Projeto', 'Ewerton Mendonça', None)],
            [('Padrões de Projeto', 'Ewerton Mendonça', None)],
            [('Padrões de Projeto', 'Ewerton Mendonça', None)],
            [('Padrões de Projeto', 'Ewerton Mendonça', None)], 
            [], [],  
            [('Estatística II', 'Milton Perceus', None)],
            [('Estatística II', 'Milton Perceus', None)],
            [('Estatística II', 'Milton Perceus', None)],
            [('Estatística II', 'Milton Perceus', None)],  
        ],
        'Quinta': [
            [], [], [], [], [], [],
            [('Programação para Web', 'Elisson Rocha', None)],
            [('Programação para Web', 'Elisson Rocha', None)],
            [('Programação para Web', 'Elisson Rocha', None)],
            [('Programação para Web', 'Elisson Rocha', None)],  
        ],
        'Sexta': [
            [],  [],  [],  [],  [],  [],  [],  [],  [],   [], 
            
        ]
    },
    6: {  
        'Segunda': [
            [], [],  
            [('Engenharia de Software Experimental', 'Adauto Trigueiro', None)],
            [('Engenharia de Software Experimental', 'Adauto Trigueiro', None)],
            [('Engenharia de Software Experimental', 'Adauto Trigueiro', None)],
            [('Engenharia de Software Experimental', 'Adauto Trigueiro', None)],  
            [('Arquitetura de Software', 'Brunno Wagner', None)],
            [('Arquitetura de Software', 'Brunno Wagner', None)],
            [('Arquitetura de Software', 'Brunno Wagner', None)],
            [('Arquitetura de Software', 'Brunno Wagner', None)], 
        ],
        'Terça': [
            [], [], 
            [('Sistemas Operacionais', 'Cleiton Martins', None)],
            [('Sistemas Operacionais', 'Cleiton Martins', None)],
            [('Sistemas Operacionais', 'Cleiton Martins', None)],
            [('Sistemas Operacionais', 'Cleiton Martins', None)],  
            [],  [],  [],  [],  
        ],
        'Quarta': [
            [('Inteligência Artificial', 'Eraylson Galdino', None)],
            [('Inteligência Artificial', 'Eraylson Galdino', None)],
            [('Inteligência Artificial', 'Eraylson Galdino', None)],
            [('Inteligência Artificial', 'Eraylson Galdino', None)],  
            [('Disciplina Curricular de Extensão 6', 'Eraylson Galdino', None)],
            [('Disciplina Curricular de Extensão 6', 'Eraylson Galdino', None)], 
            [],  [],  [],  [],  
        ],
        'Quinta': [
            [('Integração de Sistemas', 'Elisson Rocha', None)],
            [('Integração de Sistemas', 'Elisson Rocha', None)],
            [('Integração de Sistemas', 'Elisson Rocha', None)],
            [('Integração de Sistemas', 'Elisson Rocha', None)],  
            [], [], [], [], [], [],  
        ],
        'Sexta': [
            [], [], 
            [('Interação Humano-Computador', 'Ariane Nunes', None)],
            [('Interação Humano-Computador', 'Ariane Nunes', None)],
            [('Interação Humano-Computador', 'Ariane Nunes', None)],
            [('Interação Humano-Computador', 'Ariane Nunes', None)], 
            [], [], [], [], 
        ]
    },
    8: {  
        'Segunda': [
            [],  [], 
            [('Manutenção e Evolução de Software', 'Victor Santos', None)],
            [('Manutenção e Evolução de Software', 'Victor Santos', None)],
            [('Manutenção e Evolução de Software', 'Victor Santos', None)],
            [('Manutenção e Evolução de Software', 'Victor Santos', None)],  
            [], [], [], [], 
        ],
        'Terça': [
            [], [],
            [('Computação Gráfica e Sistemas Multimídia', 'Ewerton Mendonça', None)],
            [('Computação Gráfica e Sistemas Multimídia', 'Ewerton Mendonça', None)],
            [('Computação Gráfica e Sistemas Multimídia', 'Ewerton Mendonça', None)],
            [('Computação Gráfica e Sistemas Multimídia', 'Ewerton Mendonça', None)],  
            [('Aprendizagem de Máquina e Reconhecimento de Padrões', 'Victor Santos', None)],
            [('Aprendizagem de Máquina e Reconhecimento de Padrões', 'Victor Santos', None)],
            [('Aprendizagem de Máquina e Reconhecimento de Padrões', 'Victor Santos', None)],
            [('Aprendizagem de Máquina e Reconhecimento de Padrões', 'Victor Santos', None)],  
        ],
        'Quarta': [
            [], [],
            [('Tópicos Avançados em Engenharia de Software e Sistemas I', 'Victor Santos', None)],
            [('Tópicos Avançados em Engenharia de Software e Sistemas I', 'Victor Santos', None)],
            [('Tópicos Avançados em Engenharia de Software e Sistemas I', 'Victor Santos', None)],
            [('Tópicos Avançados em Engenharia de Software e Sistemas I', 'Victor Santos', None)],
            [('Tópicos Avançados em Computação Inteligente', 'Elisson Rocha', None)],
            [('Tópicos Avançados em Computação Inteligente', 'Elisson Rocha', None)],
            [('Tópicos Avançados em Computação Inteligente', 'Elisson Rocha', None)],
            [('Tópicos Avançados em Computação Inteligente', 'Elisson Rocha', None)],  
        ],
        'Quinta': [
            [('Disciplina Curricular de Extensão 8', 'Mariana Maia', None)],
            [('Disciplina Curricular de Extensão 8', 'Mariana Maia', None)],
            [],  [],  [], 
            [('Seminário em Engenharia de Software II', 'Marcello Mendonça', None)],
            [('Seminário em Engenharia de Software II', 'Marcello Mendonça', None)],
            [],  [], 
        ],
        'Sexta': [
            [], [],
            [('Tópicos Avançados em Engenharia de Software e Sistemas IV', 'Mariana Maia', None)],
            [('Tópicos Avançados em Engenharia de Software e Sistemas IV', 'Mariana Maia', None)],
            [('Tópicos Avançados em Engenharia de Software e Sistemas IV', 'Mariana Maia', None)],
            [('Tópicos Avançados em Engenharia de Software e Sistemas IV', 'Mariana Maia', None)],
            [], [], [], [],  
        ]
    }
}


fitness_1 = calcular_fitness(horario_2)
print(fitness_1)