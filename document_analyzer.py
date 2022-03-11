file1 = open('document.txt', encoding='utf8')

sentence_list = file1.read()

rm_period = sentence_list.replace(".","")

sentence_list = rm_period.split()

unique_words = []
for word in sentence_list:
    if word not in unique_words:
        unique_words.append(word)

unique_words.sort()

value = []
for i in range(len(unique_words)):
    value.append(sentence_list.count(unique_words[i]))

dictionary_sen = {}

for i in range(len(unique_words)):
    dictionary_sen [unique_words[i]] = value[i]


dictionary_sorted = sorted(dictionary_sen , key=dictionary_sen.get, reverse=True)[:5]

for i in range(len(dictionary_sorted)):

    print(str(dictionary_sorted[i]) + ": " + str(dictionary_sen[dictionary_sorted[i]]))
