""" Author : Marinos Marios(dai17147)
    Deterministic finite automation, non Deterministic finite automation
    and NFA with e transitions due to the course of automation theory 7th semester.
"""
import sys
from collections import defaultdict
import time

class NFAe:
    current_state = None;
    def __init__(self, states, transition_function, start_state, accept_states,transitions):
        self.states = states;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        self.transitions = transitions;
        self.alphabet = set();
        return;

    def transition_to_state_with_input(self, input_value):
        # if DFA detect a letter that is not supposed to be in our alphabet,
        # it will set the current state to None. Otherwise if current state and
        # input value are in the dictionary move to the next state.
        #print('curr_state',self.current_state)
        next_states = set()
        # iterate each next state in current states.
        for state in self.current_state:
            e_closure_statesFinal = set()
            # takes the initial state + all the e-transition states.
            # tommorow.
            e_closure_statesFinal.add(state)
            last_set = set()
            elems = e_closure_statesFinal - last_set
            while (len(elems) != 0):
                elems = e_closure_statesFinal - last_set
                # break if no more elements to test.
                if (len(elems) == 0):
                    break
                last_set = e_closure_statesFinal.copy()
                #print('elems', elems)
                for nextstate in elems:
                    for y in range(1):
                        if ((nextstate, '@') in self.transition_function.keys()):
                            e_closure_statesFinal  = e_closure_statesFinal |self.transition_function[(nextstate, '@')]
                        else :
                            break
                #print('final',e_closure_statesFinal)

            for state in e_closure_statesFinal:
                next_states = next_states|self.transition_function[(state, input_value)]# intersection
            #print('next_states', next_states)
            # if the input is the empty word and it is acceptable by any of e-transitions
            # or the initial state accept it.
            if (input_value == ' '):
                self.current_state = e_closure_statesFinal
                return
            # if there are no other next_states break. It means that there are no
            # transitions with the letter that was inputed.
            if (len(next_states) == 0):
                print('There are no current states to keep going. False')
                exit()
            # set the current_state the next states.
            self.current_state = next_states


    def in_accept_state(self):
        # if current_state(last letter) is in accpet states then return True otherwise false.
        for i in self.current_state:
            if (i in self.accept_states):
                return True;
        return False;


    def go_to_initial_state(self):
        # set the initial state.
        self.current_state = self.start_state;
        return;

    def calc_alphabet(self):
        #alphabet = set()
        temp = self.transition_function.keys()
        # for each key value export the second number which is the letter
        # to make up the alphabet.
        # add the empty word on alphabet.
        self.alphabet.add(' ')
        for y in temp:
            if (y[1] not in self.alphabet):
                self.alphabet.add(y[1])
            #self.transition_function[()]

    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        self.calc_alphabet();
        for inp in input_list: # for each letter go to the next state.
        # if the inp isn't on alphabet exit the program.
            if (inp not in self.alphabet):
                print("The letter (",inp,") doesn't exist on your alphabet.")
                exit()
            self.transition_to_state_with_input(inp);
        return self.in_accept_state();


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
        next_states = set()
        # iterate each next state in current states.
        for i in temp:
            # if input letter doesn't exist set it None and break.
            if ((i, input_value) not in self.transition_function.keys()):
                i = None;
            next_states = next_states|self.transition_function[(i, input_value)] # intersection
            print(i,input_value,"->",next_states)
        if len(next_states) == 0 : # if set is empty it means that the letter
            #which has been inserted isn't on the alphabet.
            print("False")
            exit()
        else:
            self.current_state = next_states


    def in_accept_state(self):
        # if current_state(last letter) is in accpet states then return True otherwise false.
        for i in self.current_state:
            if (i in accept_states):
                return True;
        return False;


    def go_to_initial_state(self):
        # set the initial state.
        self.current_state = self.start_state;
        return;

    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        for inp in input_list: # for each letter go to the next state.
            self.transition_to_state_with_input(inp);
        return self.in_accept_state();

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
                for i in range(1,len(split)):
                    final_list.add(int(split[i]))
            elif (split[0].startswith('transitions')):
                transitions = int(split[1])
            else:
                if (falgorithm == 'DFA'):
                    transitions_dictionary[(int(split[0]),split[1])] = int(split[2]);
                else :
                    transitions_dictionary[(int(split[0]),split[1])].add(int(split[2]));

    print ([ (k,v) for k,v in transitions_dictionary.items()])

    return states, initial, final_list, transitions_dictionary, transitions



if __name__ == "__main__":
    fname = sys.argv[1] # waiting for the user to give the name.
    falgorithm = sys.argv[2] # tell what kind of problem is. (DFA,NFA,NFA-e)
    states, initial,accept_states,transitions,transitions_num = readFile(fname,falgorithm)
    d = NFAe(states,transitions,initial,accept_states,transitions_num)
    inp_program = list('910');
    print(d.run_with_input_list(inp_program));
