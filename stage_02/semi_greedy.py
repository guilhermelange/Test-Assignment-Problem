
import random
import sys
sys.path.insert(1, '../')
from utils import read_instance, objetive_function, correct_solution_v2, viable_solution
import config


# Algoritmo semi-guloso e amostragem gulosa conforme http://mauricio.resende.info/doc/sgrasp-pt.pdf e ... 
# https://digitalis-dsp.uc.pt/bitstream/10316.2/30057/3/10-Manual%20de%20Computa%C3%A7%C3%A3o%20Evolutiva%20e%20Metaheur%C3%ADstica%20%282012%29.pdf
def semi_greedy(alpha, correct_size):
    desks, tests, empty = config.desks, config.tests, config.empty
    desks_count = len(desks)
    tests_count = len(tests)
    desks_with_tests = desks_count
    if correct_size:
        desks_with_tests -= empty
    
    s_ = [0 for i in range(desks_count)] # Solucao
    C = [i for i in range(1, tests_count)] # Possibilidades
    g = [] # Objetivo para cada possibilidade
    value_ = 0
    count = 0

    while count < desks_with_tests:
        # Escolher carteira manipulada.
        list_index = [i for i in range(desks_count) if s_[i] <= 0]
        index = random.choice(list_index)
        g = []

        # Gerar melhoria mínima e máxima e criar array com melhorias
        s = s_.copy()
        g_min = 0
        g_max = 0
        g.append(0)
        for c in C:
            s[index] = c
            g_current = objetive_function(s) - value_
            if c == 1: 
                g_min = g_current 
                g_max = g_current

            if g_current < g_min:
                g_min = g_current

            if g_current > g_max:
                g_max = g_current

            g.append(g_current)

        # Executar formula para selecionar LRC(C) conforme alpha
        LRC = []
        for i in range(1, tests_count):
            # print(g_min,  g[i], g_max, alpha)
            if g_min <= g[i] <= (g_min + (alpha * (g_max - g_min))):
                LRC.append(i)

        # Sortear alpha e prosseguir
        index_test = random.choice(LRC) - 1
        s[index] = C[index_test]
        s_ = s
        value_ = objetive_function(s_)
        count += 1

    return s_, value_
        

if __name__ == '__main__':
    file_name = sys.argv[1]
    alpha = float(sys.argv[2])
    read_instance(file_name)

    s_, value_ = semi_greedy(alpha, True)
    print(s_)
    print(value_)