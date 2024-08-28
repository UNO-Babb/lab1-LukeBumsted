#MadLib.py
#Name:luke
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("enter a noun: ")
plural_noun1 = input("enter a plural noun: ")
verb_ending_in_ing = input("enter a verb ending in ing: ")
plural_noun2 = input("enter a plurl noun: ")
city1 = input("enter a city: ")
plural_noun3 = input("enter a plural noun: ")
adjective1 = input("enter a adjective: ")
verb1 = input("enter a verb: ")
verb2 = input("enter a verb: ")
plural_noun4 = input("enter a plural noun: ")
verb_ending_in_ing2 = input("enter a verb ending in ing: ")
number1 = input("enter a number: ")
adverb1 = input("enter an adverb: ")
noun2 = input("enter a noun: ")
adjective2 = input("enter a adjective: ")

  #Print the story with the user supplied words.

print("In 1981, the U.S. launched the first real space" ,(noun1) ,". It was named columbia and was piloted by two brave" ,(plural_noun1),
      ". They had practiced" ,(verb_ending_in_ing), "for two years and were expert" ,(plural_noun2), ". columbia took off from " ,(city1), "using its powerful first-stage" ,(plural_noun3),
      "and soared off into the" ,(adjective1), "blue" ,(noun2), ". At an altitude of" ,(number1), "feet, it went into orbit around the" ,(noun2), ". For people watching from earth, it was a/an" ,(adjective2), "sight to" ,(verb1), "!"
      "Who could really" ,(verb2), "that there were two" ,(plural_noun4), "in space? It was minf" ,(verb_ending_in_ing2), ". "
      "after" ,(number1), "orbits, the shuttle landed" ,(adverb1), "at an air force" ,(noun2), "it was a/an" ,(adjective2), "day for ther U.S. program.")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
