import os
import string

wordCount = 0 
wordList = []
avgSentenceLength = 0 
avgWordLength = 0

textpath = os.path.join("/Users/alex/Desktop/test.txt")

with open(textpath, 'r') as txtfile:   
    for line in txtfile:
        #count each instance of punctuation ending a sentence
        sentenceCount = (line.count(".")) + (line.count("?")) + (line.count("!"))
        
        #append the text to a list and change to a string to count words 
        wordList.append(line)
        wordList = str(wordList)

        #count each space to total words and add one because there is no space at the end of the string
        wordCount = (wordList.count(" "))
        wordCount = wordCount + 1
        
        avgSentenceLength = (wordCount/sentenceCount)


        #replace all spaces and punctuation from the string to count letters
        newList = wordList.replace(" ", "").replace("[", "").replace("]","").replace("(","").replace(")","").replace(",","").replace(".","").replace("!","").replace("?","").replace(";","").replace(":","").replace('"',"").replace("-","")
        #count the length of the list to get the letterCount, subtracting two for the pararentheses around the string
        letterCount = (float(len(newList) - 2))

    avgWordLength = letterCount/wordCount

    print ("Paragraph Analysis")
    print ("------------------")        
    print ("Approximate Word Count: " + str(wordCount))
    print ("Approximate Sentence Count: " + str(sentenceCount))
    print ("Average Letter Count: " + str(avgWordLength))
    print ("Average Sentence Length: " + str(avgSentenceLength))

   

