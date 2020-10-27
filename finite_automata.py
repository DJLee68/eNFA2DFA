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
    #}

    def print_fa(self): #{
        print(f'states: {self.states}')
        print(f'input symbol: {self.input_symbol}')
        print(f'transition function: {self.transition_function}')
        print(f'start state: {self.start_state}')
        print(f'final states: {self.final_states}')
    #}

    def check_input(self, input): #{
        state = self.start_state[0]
        for i in input: #{
            if i not in self.input_symbol:#{
                print('Rejected1!')
                return
            #}
            for func in self.transition_function: #{
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
            print('Rejected2!')
            return
        #}
    #}

    def get_closure(self, state): #{
        temp = [state]
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

    # NFA to DFA
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
                    if len(tmp) != 0: #{
                        if list(tmp) not in marked: unmarked.append(list(tmp))
                        for final_state in self.final_states: #{
                            if final_state in list(tmp): #{
                                if list(tmp) not in final: final.append(list(tmp))       
                            #}
                        #}
                        tmp_transition.append([u, i, list(tmp)])
                        if list(tmp) not in marked: marked.append(list(tmp))
                    #}
                #}
                unmarked.remove(u)
            #}
        #}

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