#!/usr/bin/env python3
from ast import literal_eval
import os.path


def main():
    again = True
    switch = {0: "The string '{0}' is not recognized by the language {1}.",
            1: "The string '{0}' is accepted!",
            2: "The string '{0}' was not accepted."}
    
    while (again):
        dfa = False
        while not dfa:
            dfa = load_file()
        display_dfa(dfa)
        string = (str(input("What is the input string you would like to " 
            "check against the DFA: " )))
        eval_input_string(dfa, string)
        again = go_again()


def load_file():

    try:
        filename = str(input("What is the name of the file(ex: file.txt): "))
        with open(filename, "r") as file:
            automata = [literal_eval(each.lstrip("QEdSF:\n")) for each in file]
        automata = [list(set(each)) if isinstance(each, tuple) 
                else each for each in automata]
        return automata
    except IOError as e:
        print ("That file does not exist!")
        return False


def display_dfa(dfa):
    print ("Here is your DFA:\nStates: {0}\nLanguage: {1}\n" 
            "Transitions: {2}\nStart State: {3}\nAccept State(s): " 
            "{4}".format(dfa[0], dfa[1], dfa[2], dfa[3], dfa[4]))


def recognized_by_language(language, string):
    for each in string:
        if each not in language and each is not " ":
            print ("The input string '{0}' is not recognized by the language"
                    "{1}.".format(string, language))
            return True
    return True


def eval_input_string(dfa, string):
    current = dfa[3] #Sets current to the start state
    print ("Starting state: {0}".format(current))
    for each in string:
        if each is " ":
            current, previous = current, current
        else:
            current, previous = dfa[2].get((current, each), None), current
            print ("({0}, '{1}') --> {2}".format(previous, each, current))
            if current is None and each in dfa[1]:
                print ("The string '{0}' was not accepted!".format(string))
                return
            elif current is None and each not in dfa[1]:
                print ("The character '{0}' is not accepted by the language "
                        "{1}!".format(each, dfa[1]))
                return
    print ("Final state: {0}".format(current))
    if current in dfa[4]:
        print ("The string '{0}' was accepted!".format(string))
        return
    print ("The string '{0}' was not accepted!".format(string))


def go_again():
    response = str(input("Would you like to go again (Y/N)? "))
    return "Y" == response.upper()


if __name__ == '__main__':
    main()
