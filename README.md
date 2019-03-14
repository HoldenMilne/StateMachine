# StateMachine
A small State Machine file made in python (Jupyter-Notebook) for creating and processing DFAs

Ignoring the extra explanation commands, like separators and examples the process is:
## Step 1
Create States with no transitions.  Accepting states and Starting states should be defined here.
## Step 2
Create and Assign Transitions.  Can be done either explicitly or in terms of alphabets as global alphabet; alphabet[0] for the first character.  Assigning transitions can be done in line with state.transitions = [Transition('0',s2),Transitions('1'),s3] or like above with variables for each transition.
## Step 3
Create the state machine using DFA(state list).  
## Step 4
Create the strings to test.  DFA.randomStrings(count,length) can be used to generate count number of strings each of size length.  Default is 32 and 8.  The next optional step cannot be done with randomStrings unless you assign a seed and check each option for that seed.
## Step 5 
#### (Optional) 
Use DFA.test(results, known) to check if all of the accepting/failing strings match with some other expected input or another DFA.  This requires creating a list with the boolean values for each string in the tested strings with the indicies matching their associated strings
