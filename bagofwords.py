import string
import os
from nltk.tokenize import word_tokenize

# performs bag of words analysis on provided dataframe and writes results to a file
# bag of words program taken from https://spotintelligence.com/2022/12/20/bag-of-words-python/
def bagOfWords(tngData, pairs):
    # empty list to hold the strings that contain Data's speech from each season
    speech = []

    # create the vocabulary
    vocab = set()

    # create the bag-of-words model and an index reference for printing
    bow_model = []
    index = 0

    # check if output file already exists. If so, delete it
    outputFile = 'output.txt'
    if os.path.exists(outputFile):
        os.remove(outputFile)
        print("Reset output file.")

    print("Writing output to file for verification...")
    for x, y in pairs:
        # add text block to speech list
        speech.append(combineText(tngData, x, y))

        # create a dictionary to store the word counts
        wordCounts = {}
                
        # tokenize the text
        tokens = word_tokenize(speech[index])
                
        # update the vocabulary
        vocab.update(tokens)
                
        # count the occurrences of each word
        for word in tokens:
            if word in wordCounts:
                wordCounts[word] += 1
            else:
                wordCounts[word] = 1
            
        # add the word counts to the bag-of-words model
        bow_model.append(wordCounts)

        # print output to file with a seasons/episode header for checking
        outFile = open(outputFile, "a")
        printToFile(x, y, outFile, wordCounts)

        # move index forward for print referencing
        index += 1

    # close output file and return bag of words model
    outFile.close()
    print("Closed output file.")
    print()

    return bow_model

# combine lines of text into a text block
def combineText(data, x, y):
    textBlock = ''
    for line in data.loc[(data['Season'] == x) & (data['Episode'] == y), 'text']:
        # add line of text to the string
        textBlock += line

        # remove punctuation and numbers
        textBlock = textBlock.replace("...", " ")
        textBlock = textBlock.translate(str.maketrans('', '', string.punctuation))
        textBlock = ''.join([i for i in textBlock if not i.isdigit()])
    return textBlock

# prints bag of words model information to a file with a header and word count
def printToFile(season, episode, outFile, words):
    print("Season", season, "Episode", episode, file=outFile)
    print(words, file=outFile)
    print("Number of Words Used:", len(words),file=outFile)
    print(file=outFile)