""" Author : Marinos Marios(dai17147)
    Deterministic finite automation, non Deterministic finite automation
    and NFA with e transitions due to the course of automation theory 7th semester.
"""
import sys
from collections import defaultdict

class NFA:
    current_state = None;
    def __init__(self, states, transition_function, start_state, accept_states):
        self.states = states;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        return;

    def transition_to_state_with_input(self, input_value):
        # if DFA detect a letter that is not supposed to be in our alphabet,
        # it will set the current state to None. Otherwise if current state and
        # input value are in the dictionary move to the next state.
        temp = self.current_state
        print('curr_state',temp)
        x = set()
        for i in temp:
            """if ((i, input_value) not in self.transition_function.keys()):
                i = None;
                return;
            """
            x = x|self.transition_function[(i, input_value)] # intersection
            print(i,input_value,"->",x)
        self.current_state = x

    def in_accept_state(self):
        # if current_state(last letter) is in accpet states then return True otherwise false.
        for i in self.current_state:
            if (i in accept_states):
                return True;
    

    def go_to_initial_state(self):
        # set the initial state.
        self.current_state = self.start_state;
        return;

    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        for inp in input_list: # for each letter go to the next state.
            self.transition_to_state_with_input(inp);
        return self.in_accept_state();
    pass;

class DFA:
    current_state = None;
    def __init__(self, states, transition_function, start_state, accept_states):
        self.states = states;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        return;

    def transition_to_state_with_input(self, input_value):
        # if DFA detect a letter that is not supposed to be in our alphabet,
        # it will set the current state to None. Otherwise if current state and
        # input value are in the dictionary move to the next state.
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None;
            return;
        self.current_state = self.transition_function[(self.current_state, input_value)];
        return;


    def in_accept_state(self):
        # if current_state(last letter) is in accpet states then return True otherwise false.
        return self.current_state in accept_states;

    def go_to_initial_state(self):
        # set the initial state.
        self.current_state = self.start_state;
        return;

    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        for inp in input_list: # for each letter go to the next state.
            self.transition_to_state_with_input(inp);
        return self.in_accept_state();
    pass;

def readFile(fname, falgorithm):
    with open(fname) as f:
        if (falgorithm == 'DFA'):
            transitions_dictionary = dict();
        elif (falgorithm == 'NFA'):
            transitions_dictionary = defaultdict(set); # transitions
        states= set() # all states
        final_list = set() # final_states in list.
        for line in f:
            split = line.split(' ')
            if (split[0].startswith('states')):
                for i in range(int(split[1])):
                    states.add(i+1)
            elif (split[0].startswith('initial')):
                initial = int(split[1])
                if (falgorithm == 'NFA'):
                    temp = set()
                    temp.add(initial)
                    initial = temp
            elif (split[0].startswith('final')):
                final = int(split[1])
            elif (split[0].startswith('f_states')):
                for i in range(1,final+1):
                    final_list.add(int(split[i]))
            elif (split[0].startswith('transitions')):
                transitions = int(split[1])
            else:
                if (falgorithm == 'DFA'):
                    transitions_dictionary[(int(split[0]),split[1])] = int(split[2]);
                else :
                    transitions_dictionary[(int(split[0]),split[1])].add(int(split[2]));

    print ([ (k,v) for k,v in transitions_dictionary.items()])

    return states, initial, final_list, transitions_dictionary



if __name__ == "__main__":
    fname = sys.argv[1] # waiting for the user to give the name.
    falgorithm = sys.argv[2] # tell what kind of problem is. (DFA,NFA,NFA-e)
    states, initial,accept_states,transitions = readFile(fname,falgorithm)
    d = NFA(states,transitions,initial,accept_states)
    inp_program = list('0101');
    print (d.run_with_input_list(inp_program));
