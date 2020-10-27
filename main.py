from finite_automata import FA, DFA, ENFA, NFA

# f_name = input('Enter file name: ')
f = open('nfa2.txt', 'r')
lines = f.readlines()
f.close

# parse finite automata
states  = list(lines[0].strip().split())
input_symbol = list(lines[1].strip().split())
start_state = list(lines[2].strip().split())
final_state = list(lines[3].strip().split())
transition_function = []
for line in lines[4:]: #{
    transition_function.append(line.strip('\n').split())
#}


inp = ['1','1']

fa = ENFA()
fa.init_fa(states, input_symbol, start_state, final_state, transition_function)
fa.print_fa()
print('\n')
fa.subset_construct()
print('\n')
fa.print_fa()
