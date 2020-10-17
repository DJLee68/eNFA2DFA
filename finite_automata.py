class FA(): #{
    def __init__(self): #{
        self.states = []
        self.input_symbol = []
        self.start_state = []
        self.final_states = []       
        self.transition_function = [] 
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

    def 
#}

class ENFA(FA): #{
    def __init__(self): #{
        super().__init__()
    #}
#}

class NFA(FA): #{
    def __init__(self): #{
        super().__init__()
    #
#}

class DFA(FA): #{
    def __init__(self): #{
        super().__init__()
    #}
#}