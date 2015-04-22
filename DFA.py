#! /usr/bin/python
from ast import literal_eval
from sys import exit


def main():
    #filename = "DFA.txt" #FOR TESTING
    again = True
    
    while (again):
        filename = str(raw_input("What is the name of the file(ex:file.txt): "))
        dfa = load(filename)
        display_dfa(dfa)
        string = get_input_string()
        if (recognized_by_language(dfa[1], string)):
            if (eval_input_string(dfa, string)):
                print "The string '{0}' was accepted!".format(string)
            else:
                print "The string '{0}' was not accepted!".format(string)
        else:
            exit()
        again = go_again()

def load(filename):
    with open(filename, "r") as file:
        automata = [literal_eval(each.lstrip("QEdSF:\n")) for each in file]
    automata = [list(set(each)) if isinstance(each, tuple) 
                else each for each in automata]
    return automata

def display_dfa(dfa):
    print ("Here is your DFA:\nStates: {0}\nLanguage: {1}\n" +
            "Transitions: {2}\nStart State: {3}\nAccept States: " + 
            "{4}").format(dfa[0], dfa[1], dfa[2], dfa[3], dfa[4])

def recognized_by_language(language, string):
    for each in string:
        if each not in language or each is ' ':
            print ("The input string '{0}' is not recognized by the language"
                    "{1}.").format(string, language)
            return False
    return True

def get_input_string():
    return str(raw_input("What is the input string you would like to check" +
        " against the DFA: " ))

def eval_input_string(dfa, string):
    current = dfa[3] #Sets current to the start state
    print "Starting state: {0}".format(current)
    for each in string:
        current, previous = dfa[2][(current, each)], current
        print "({0},{1}) --> {2}".format(previous, each, current)
    print "Final state: {0}".format(current)
    if current in dfa[4]:
        return True
    return False

def go_again():
    response = str(raw_input("Would you like to go again (Y\N)? "))
    return "Y" == response.upper()

if __name__ == '__main__':
    main()
