import re
import nltk

nltk.download('punkt')

file = open('/corpus.txt',
            encoding="utf8")
data = file.read()
data = re.sub('[^\s ء-ي]', '', data)
tokens = nltk.word_tokenize(data)

probability = {}
ngram = {}


def ngramFunction(sentenceSize):
    count = 0
    for i in range(len(tokens) - sentenceSize):
        sequence = ' '.join(tokens[i:i + sentenceSize])
        if sequence not in ngram.keys():
            count += 1
            ngram[sequence] = 1
        else:
            count += 1
            ngram[sequence] += 1
        probability[sequence] = ngram[sequence] / count


def search(choice, input):
    inputSplitedWords = input.split(" ")

    sentenceSize = choice

    if (sentenceSize <= len(inputSplitedWords)):
        print("====================================================================================")
        print(str(sentenceSize) + " gram can't be used as the input sentence size is larger than the trigram function")
        sentenceSize = len(inputSplitedWords) + 1
        print(str(sentenceSize) + " gram will be used instead")
        print("====================================================================================")

    ngramFunction(sentenceSize)
    output_list = []
    for i in probability.keys():
        if input in i:

            flag = False
            for j in range(len(inputSplitedWords)):
                if i.split(" ")[j] != inputSplitedWords[j]:
                    flag = True

            if flag:
                continue

            output_list.append((i, probability[i]))

    output_list.sort(key=lambda temp: temp[1], reverse=True)

    print("    ", input)
    ouputSize = 5
    for i in range(ouputSize if len(output_list) > ouputSize else len(output_list)):
        print(output_list[i][0].split(" ")[output_list[i][0].find(input) + len(inputSplitedWords)])


search(int(input('write the number of desired grams : ')), input('Search : '))
