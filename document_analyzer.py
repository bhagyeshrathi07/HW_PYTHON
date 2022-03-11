file = open('document.txt', encoding='utf8')

sentence_list = file.read()

rm_period = sentence_list.replace(".","")

sent_list = rm_period.split()

unique_words = []
for word in sent_list:
    if word not in unique_words:
        unique_words.append(word)

unique_words.sort()

value = []
for i in range(len(unique_words)):
    value.append(sent_list.count(unique_words[i]))

elements = {}

for i in range(len(unique_words)):
    elements [unique_words[i]] = value[i]


dictionary_sorted = sorted(elements , key = elements.get, reverse = True)[:5]

print("\r")
for i in range(len(dictionary_sorted)):

    print(str(dictionary_sorted[i]) + ": " + str(elements[dictionary_sorted[i]]))
