# Exercise 41 of "Learn Python3 the Hard Way"
# Learning to Speak Object-Oriented
#
# class X(Y): “Make a class named X that is-a Y.”
# class X(object): def __init__(self, J) “class X has-a __init__ that takes self and J parameters.”
# class X(object): def M(self, J) “class X has-a function named M that takes self and J parameters.”
# foo = X(): “Set foo to an instance of class X.”
# foo.M(J): “From foo, get the M function, and call it with parameters self, J.”
# foo.K = Q: “From foo, get the K attribute, and set it to Q.”

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASE = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ that takes self and *** params",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function *** that takes self and @@@ params",
    "*** = %%%()": "Set *** to an instance of class %%%",
    "***.***(@@@)": "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'": "Frin *** get the *** syytibute and set it to '***'",
}

# do they want to drill phrase first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(", ".join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake othe names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep foint until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASE.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASE[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("nBye")
