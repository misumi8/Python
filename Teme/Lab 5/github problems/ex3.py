# 3 --------------------------------------------------
import time
from pprint import pprint

start_time = time.time()
with open("input.txt", "r") as f:
    data = f.read()
    words = [word.strip(".,\n ") for word in data.split()]
    words_dict = {}
    for i in range(0, len(words)):
        if(words[i] not in words_dict):
            words_dict[words[i]] = [i]
        else:
            words_dict[words[i]].append(i)
    # for k in words_dict:
    #     print(k)

with open("words.txt", "r") as f:
    word = f.readline().strip(".,\n ")
    words_interval = []
    while(word):
        if(word in words_dict):
            words_interval.append((word, words_dict[word][0], words_dict[word][-1]))
        word = f.readline().strip(".,\n ")
end_time = time.time()

pprint(words_interval)
print("Execution time:", round(end_time - start_time, 2), "s.")