class FA(): #{
    def __init__(self): #{
        self.states = []
        self.input_symbol = []
        self.start_state = []
        self.final_states = []       
        self.transition_function = [] 
        self.closure = []
    #}
    def init_fa(self, states, input_symbol, start_state, final_states, transition_function): #{
        self.states = states
        self.input_symbol = input_symbol
        self.start_state = start_state
        self.final_states = final_states
        self.transition_function = transition_function

        # delete epsilon from input symbol
        if 'ep' in self.input_symbol: self.input_symbol.remove('ep')
    #}

    def print_fa(self): #{
        print(f'states: {self.states}')
        print(f'input symbol: {self.input_symbol}')
        print(f'transition function:')
        for func in self.transition_function: #{
            print(func)
        #}
        print(f'start state: {self.start_state}')
        print(f'final states: {self.final_states}')
    #}

    # check input sentence
    def check_input(self, input): #{
        state = self.start_state
        # for every character in sentence
        for i in input: #{
            if i not in self.input_symbol:#{
                print('Rejected1! 이런 입력은 입력 심볼에 존재하지 않음')
                return
            #}
            # check every transition function
            for func in self.transition_function: #{
                # print(f'state: {state}, func0: {func[0]}, func1: {func[1]}, i: {i}, func2: {func[2]}')
                if func[0] == state and func[1] == i: #{
                    state = func[2]
                    break
                #}
            #}
        #}
        if state in self.final_states: #{
            print('Accepted!')
            return
        #}
        else: #{
            print('Rejected2! Final state에 도달하지 못함')
            return
        #}
    #}

    # get closure of state
    def get_closure(self, state): #{
        temp = []
        temp.append(state)
        # print(f'state: {state}')
        # search every transition function
        for func in self.transition_function: #{
            if state == func[0] and 'ep' == func[1]: #{
                for output in func[2:]: #{
                    temp.extend(self.get_closure(output))
                #}
            #}
        #}
        return temp
    #}

    # NFA(eNFA) to DFA
    def subset_construct(self): #{
        unmarked = []
        marked = []
        tmp_transition = []
        final = []
        unmarked.append(self.get_closure(self.start_state[0]))
        marked.append(list(self.get_closure(self.start_state[0])))

        while(unmarked): #{
            # check unmarked
            for u in unmarked: #{
                # check each input symbol
                for i in self.input_symbol: #{
                    tmp = set()
                    # check each transition function
                    for func in self.transition_function: #{
                        # if they are in transition function
                        if func[0] in u and i == func[1] and i != 'ep': #{
                            # put each output's closure
                            for output in func[2:]: #{
                                tmp.update(tuple(self.get_closure(output)))
                            #}
                        #}
                    #}
                    # if we were able to get next state
                    if len(tmp) != 0: #{
                        tmp = list(tmp)
                        tmp.sort()
                        # if that is new one
                        if list(tmp) not in marked: unmarked.append(list(tmp))
                        # check if it is in final states
                        for final_state in self.final_states: #{
                            if final_state in list(tmp): #{
                                if list(tmp) not in final: final.append(list(tmp))       
                            #}
                        #}
                        # add to transition function
                        tmp_transition.append([u, i, list(tmp)])
                        # mark
                        if list(tmp) not in marked: marked.append(list(tmp))
                    #}
                #}
                # remove previous unmarked list
                unmarked.remove(u)
            #}
        #}

        # reassign values
        self.start_state = self.get_closure(self.start_state[0])
        self.final_states = final
        self.transition_function = tmp_transition
        self.states = marked
    #}
#}

class ENFA(FA): #{
    def __init__(self): #{
        super().__init__()
    #}
#}

class NFA(FA): #{
    def __init__(self): #{
        super().__init__()
    #}
#}

class DFA(FA): #{
    def __init__(self): #{
        super().__init__()
    #}
#}