
# coding: utf-8
import random

global count # Count is just used for default state naming.
count = 1
class State:
    def __init__(self, transitions = [], accepting = False, name = None):
        global count
        
        self.transitions = transitions
        self.accepting = accepting
        
        if name == None:
            self.name = "s"+str(count)
        count+=1
    
    def transition(self,character):
        for t in self.transitions:
            if t.character == character:
                return t.state
        return None
class Transition:
    def __init__(self,character,state):
        self.state = state
        self.character = character
        
class DFA:
    # Constructor for the DFA class.  
    # Class doesn't define set of F states, since string conformation
    # can be done by checking the state's "accepting" boolean.
    # Likewise delta is omitted since transitions are stored
    # with respect to the states themselves.
    def __init__(self,Q,sigma = ['0','1'],start = None):
        global count
        count = 0
        alphabet = sigma
        self.Q = Q
        if(start == None):
            start = self.Q[0]
        self.start = start
        
    # basic function for generating strings for testing purposes
    def randomStrings(self, count = 32, length = 8, seed = None):
        
        strs = []
        if seed != None:
            random.seed = seed
        for i in range(0,count):
            s = ""
            for j in range(0,length):
                k=random.randint(0,len(alphabet)-1)
                s+=str(self.sigma[k])
            print(s)
            strs.append(s)
        return strs
            
    # Function that processes a list of strings through the DFA
    def run(self,strings, verbose = True):
        results = []
        if type(strings) == list:
            for s in strings:
                current = self.start
                if verbose:
                    print(s,end=": ")
                for c in s:
                    xf = current.transition
                    current = xf(c)
                if current.accepting == True:
                    if verbose:
                        print("Accept\n")
                    results.append(True)
                else: 
                    if verbose:
                        print("Deny\n")
                    results.append(False)
                    
        elif type(strings)==str:
            if verbose:
                print(strings,end=": ")
            current = self.start
            for c in strings:
                xf = current.transition
                current = xf(c)
            if current.accepting == True:
                if verbose:
                    print("Accept\n")
            else:
                if verbose:
                    print("Deny3\n")
        
        return results
    
    # for some pair of lists of booleans representing the success of a string at position i
    # check if each item is equal.  This lets us a. Test whether our results match what we should
    # expect (manual input) b. check if 2 dfa's are (probably) identical.
    def test(self, results, known):
        if len(known)!=len(results):
            print("Length mismatch!")
            return
        
        table = []
        for i in range(0,len(results)):
            if results[i]!=known[i]:
                print("Test failed at position "+str(i))
                print("Param 1 has: " + str(results[i])+" but Param 2 has: "+str(known[i]))
                return table
            table.append(results[i])
        print("All strings successfully matched")
        return table

def Sample():   
    # Example: Accepts binary strings with the substring '00'

    # Counter must be reset cuz jupy stores variables from other cells
    # Used to name states when name is left ommited.
    count = 1

    # Create the states.  We can't pass in any Transitions yet, as Transitions depend on the
    # States created.  You can name the states as well with name = string
    s1 = State()
    s2 = State()
    s3 = State(accepting = True)

    # Set the transitions on paramater 1, to state parameter 2.  You can use the alphabet
    # for this as well with line 1: global alphabet line 2: alphabet[0]
    s1t0 = Transition('0',s2)
    s1t1 = Transition('1',s1)
    s2t0 = Transition('0',s3)
    s2t1 = Transition('1',s1)
    s3t0 = Transition('0',s3)
    s3t1 = Transition('1',s3)

    # Set transitions.  Order doesn't matter (Is not relevant to how alphabet is defined)
    s1.transitions = [s1t0,s1t1]
    s2.transitions = [s2t0,s2t1]
    s3.transitions = [s3t0,s3t1]

    # Define a DFA with a list of states.  If no start state is defined, it assume the first
    # in the list is the start state
    m = DFA([s1,s2,s3])

    # Strings to test
    strings = ['111','1100','1101','01101','011101','010','0110','101101','10001011','1011101']

    # User known list of whether each string is accepted or not
    known = [False,True,False,False,False,False,False,False,True,False]

    # Get the results of the test as a bool array.  Can be used in-line with m.test.  Note: Verbose is
    # whether or not run will print each string and it's success along the way.  Defaults to True.

    print("######### Successful Test #########")
    results = m.run(strings, verbose = False)

    # Compares the input "Known", as the set of booleans marking whether this input strings
    # are accepted or denied.  This is optional.  All it does is checks if your interpretation
    # of whether or not the strings should be accepted matches the input.

    print(m.test(results, known))

    print("\n######### Failed Test #########")
    # Third known changed to True with no modifications to results
    # to show an example of a failed expectation
    known = [False,True,True,False,False,False,False,False,True,False]

    testResults = m.test(results,known)
    print(testResults,end = "\n\n")
    # Note: print returns array of successes til the point a mismatch is found.  We can do a
    # check here to get the exact string tested.  We test the length of testResults to be less than
    # that of strings to make sure we don't get a bizzare size that comes with an indexing exception
    print("######### Get Failed String #########")
    if len(testResults)!=len(strings):
        if len(testResults) < len(strings) :
            print("Failed string is: " + strings[len(testResults)])
        else: print("Test results larger than strings for some reason")

    # If you were to change testResults to be like so:
    sample = strings.copy()
    sample.append('x')
    testResults = sample

    # and run the test again you'd get an indexing error.  Though it will never be the case 
    # that test returns something larger than strings, it's a good error check for if you
    # accidentally do something wrong like changing testResults to be too large, or strings
    # to be too small.  See:

    print("\n######### Results too Large #########")
    if len(testResults)!= len(strings):
        if len(testResults) < len(strings):
            print("Failed string is: " + strings[len(testResults)])
        else: print("Test results larger than strings for some reason")
