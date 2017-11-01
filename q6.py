


def countWords(sentence):
    split_sentence = sentence.split(" ")
    return len(split_sentence)


s = "This is a sentence with words in it"

print(countWords(s))  # displays 8