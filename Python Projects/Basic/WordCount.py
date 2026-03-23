# def word_count(sentence):
#     count_dict = {}
#     words = sentence.split()
#     for word in words:
#         count_dict[word] = count_dict.get(word, 0) + 1
    
#     return count_dict

def word_count(sentence):
    count_dict = {}
    word = sentence.split()
    return {word: 1 for word in word if word not in count_dict}

string = "the cat sat on the math the cat"
print(word_count(sentence=string))

