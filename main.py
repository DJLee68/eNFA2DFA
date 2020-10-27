from finite_automata import FA, DFA, ENFA, NFA

# read fa input
f_name = input('Enter FA file name(ex, dfa1.txt, nfa1.txt): ')
f = open(f_name, 'r')
lines = f.readlines()
f.close

fa_type = ''
if 'dfa' in f_name: fa_type = 'dfa'
elif 'enfa' in f_name: fa_type = 'enfa'
else: fa_type = 'nfa'

# parse finite automata
states  = list(lines[0].strip().split())
input_symbol = list(lines[1].strip().split())
start_state = list(lines[2].strip().split())
final_state = list(lines[3].strip().split())
transition_function = []
for line in lines[4:]: #{
    transition_function.append(line.strip('\n').split())
#}

fa = FA()
fa.init_fa(states, input_symbol, start_state, final_state, transition_function) # assign fa values
print('\ninitial fa:\n')
fa.print_fa()
fa.subset_construct() # 자료형을 맞춰주기 위해 FA 경우에도 subset_construct를 해줍니다. 자료형만 변경하고 내용은 달라지지 않습니다.

if fa_type != 'dfa': #{
    print('\nsubset constructed fa:\n')
    fa.print_fa()
#}



test_input = input("\n테스트 하고 싶은 문자열을 입력하세요: ")
fa.check_input(test_input)
