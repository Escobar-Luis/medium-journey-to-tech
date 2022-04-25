# Given a start word, an end word and a list of dictionary words. Determine the minimum number of steps to go from the start word to the end word using only words from the dictionary.

from collections import deque
from string import ascii_letters
from typing import List

def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    # using set allows for constant work when looking for record
    words = set(word_list) # make a set because existence query is O(1) vs O(N) for list
    # initialize queue with beginning word
    queue = deque([begin])
    # Distance to keep track of the steps being took
    distance = 0
    while len(queue) > 0:
        # using n to keep track of layers since, every layer can have multiple words in queue
        n = len(queue)
        distance += 1
        for _ in range(n):
            word = queue.popleft()
            for i in range(len(word)):
                # filtering to lower case and upper case letters
                # replace every word[i] with every ascii leter 
                for c in ascii_letters:
                    # return everything before index
                    first=word[:i]
                    second=c
                    # return everything after index, including index
                    thrid=word[i + 1:]
                    next_word = word[:i] + c + word[i + 1:]
                    # if the next word is not in our words set, it means it has been visited so continue
                    if next_word not in words:
                        continue
                    # if next_word is equal to end word, then return distance
                    if next_word == end:
                        return distance
                    # if it is in our set, then add the word to queue and remove it from our set to mark as visited
                    queue.append(next_word)
                    words.remove(next_word) # removing from the set is equivalent as marking the word visited
    return 0
start = "COLD"
end = "WARM"
word_list = ["COLD", "GOLD", "CORD", "SOLD", "CARD", "WARD", "WARM", "TARD"]
word_ladder(start,end,word_list)