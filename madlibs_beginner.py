#start with paragraph that will have specific replacements; this will make it easier to determine placements and what types are needed for funny/good results. 
print(" Give An Adjective: ") #prompts user to give an adjective.
adj = input() #stores user input into an adj variable.
print("Give A Person's Name: ")
noun_person = input()
print("Give A Verb (present tense, negative action): ")
verb = input()
print("Give A Verb (present tense, positve action): ")
verb2 = input()
print("Give An Adjective: ")
adj2 = input()
print("Learning to code makes all of us " + adj + ".")
print("Ignore the impending AI takeover which will lead to " + noun_person + " being a slave at mcdonald's serving the AI overlords.") #allows for better readability of code.
print(noun_person + " makes JAVASCRIPT frappes for the robots. He is not good at programming in Javascript so the robots " + verb + " him.")
print(noun_person + " also makes PYTHON fries. He is very good at programming in python so the robots " + verb2 + " him.")
print("Overall, " + noun_person + " makes the robots " + adj2 + ", so " + noun_person + " lives to see another day, maybe.")
#issue during run @ 4/4/2023 @ 12:24AM : need to add a prompt so user knows when and what to type.
#issue during run @ 4/4/2023 @ 12:41AM : used the wrong adj variable.
#issue during run @ 4/4/2023 @ 12:46AM : forgot space before "Learning" string.