s = "tree"

from collections import Counter
def frequencySort(self, s):
        fre=Counter(s)
        de = sorted(fre.keys(), key=lambda x: fre[x], reverse=True)
        return ''.join(char * fre[char] for char in de)
print(frequencySort(s))