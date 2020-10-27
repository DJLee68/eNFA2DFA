from finite_automata import FA, DFA, ENFA, NFA

# f_name = input('Enter file name: ')
f = open('enfa1.txt', 'r')
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

fa = ENFA()
fa.init_fa(states, input_symbol, start_state, final_state, transition_function)
print('initial fa\n')
fa.print_fa()
fa.subset_construct()
print('subset constructed fa\n')
fa.print_fa()

test_input = input("테스트 하고 싶은 문자열을 입력하세요: ")
fa.check_input(test_input)
