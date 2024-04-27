import random
import os.path

def getWords(fn):

    while not os.path.isfile(fn):
        fn = input("Enter EXISTING filename: ")

    with open(fn, 'r') as inf:

        words = inf.read()

        return tuple(list(words.split()))

articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()


def main():
    """Allows the user to input the number of sentences
    to generate."""

    number = int(input("\nEnter the number of sentences (0 to quit): "))

    while number != 0:

        for count in range(number):
            print(sentence())

        number = int(input("\nEnter the number of sentences (0 to quit): "))

    
# The entry point for program execution
if __name__ == "__main__":
    main()