import codecs
import sys

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    counts_sorted = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return counts_sorted

if len(sys.argv) != 3:
    raise ValueError('Arg1: input in the form of a text file;   Arg2: number of top-items')

input_file_name = sys.argv[1]
top = int(sys.argv[2])

file = codecs.open(input_file_name, "r", "utf8")
returned = word_count(file.read())

count = 0
for a in returned:
    print(a)
    count += 1
    if count >= top:
        break
