#!/usr/bin/env python3

"""Ricky Valencia, CS300, Spring 2015
This program reads a .txt file which contains a deterministic finitie automata
in the correct format, then lets the user input a string that compares it
to the automata. If the string is accepted by the DFA, then an accept message
is printed, otherwise a rejected message is printed. If the user inputs a string
with characters that are not apart of the language, then the string is not 
accepted by the DFA."""

from ast import literal_eval
import os.path


def main():

    again = True #Stores whether the user wants to continue running the program
    while (again):
        #Repeats until a correct file is loaded
        dfa = False #Stores the DFA once it's loaded in
        while not dfa:
            dfa = load_file()
        display_dfa(dfa)
        string = (str(input("What is the input string you would like to " 
            "check against the DFA: " )))
        eval_input_string(dfa, string)
        again = go_again()


def load_file():
    """This function loads in a DFA from a text file, parses it, then returns
    the list of items read in. If the file does not exist, then an error is
    thrown and it returns false, otherwise it returns true."""

    try:
        filename = str(input("What is the name of the file(ex: file.txt): "))
        with open(filename, "r") as file:
            #Strips it of unneccessary characters that keep it from being
            #evaluated to a data structure that python recognizes.
            automata = [literal_eval(each.lstrip("QEdSF:\n")) for each in file]
        #Removes repeated entries in each item of the list
        automata = [list(set(each)) if isinstance(each, tuple) 
                else each for each in automata]
        return automata
    except IOError as e:
        print ("That file does not exist!")
        return False


def display_dfa(dfa):
    """This function displays the DFA in a neat way."""

    print ("Here is your DFA:\nStates: {0}\nLanguage: {1}\n" 
            "Transitions: {2}\nStart State: {3}\nAccept State(s): " 
            "{4}".format(dfa[0], dfa[1], dfa[2], dfa[3], dfa[4]))


def eval_input_string(dfa, string):
    """This function evaluates the in input string by the user and compares it 
    to DFA to see if it is accepted, rejected, or recognized by the language. If
    The string contains characters from the input string that aren't in the
    language, then the string is not recognized by the language and it returns.
    If the input string has all the proper characters recognized by the input
    string, then it accepts if the final state is also an accept state, 
    otherwise it is rejected. It returns out of the function in both cases."""

    current = dfa[3] #Sets current to the start state of the DFA
    print ("Starting state: {0}".format(current))
    for each in string:
        #Do not moves states if the character is empty
        if each is " ":
            current, previous = current, current
        else:
            current, previous = dfa[2].get((current, each), None), current
            print ("({0}, '{1}') --> {2}".format(previous, each, current))
            #Used to check if the DFA has transitions for each character in the
            #language for each state
            if current is None and each in dfa[1]:
                print ("The string '{0}' was not accepted!".format(string)
                return
            #Checks if the character is recognized by the language
            elif current is None and each not in dfa[1]:
                print ("The character '{0}' is not recognized by the language "
                        "{1}!".format(each, dfa[1]))
                return
    print ("Final state: {0}".format(current))
    #Compares the final state to the accept states
    if current in dfa[4]:
        print ("The string '{0}' was accepted!".format(string))
        return
    print ("The string '{0}' was not accepted!".format(string))


def go_again():
    """This function prompts the user if they would like to continue a task more
    than once. If they answer with 'y' or 'Y', then it returns true, otherwise
    false. """

    response = str(input("Would you like to go again (Y/N)? "))
    return "Y" == response.upper()


if __name__ == '__main__':
    main()
