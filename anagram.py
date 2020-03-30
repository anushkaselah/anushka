from collections import Counter
def maxAnagramSize(input):
    input=input.split(" ")
    for i in range(0,len(input)):
        input[1]=''.join(sorted(input[1]))
    print("sorted:",str(input))
    freqDict=Counter(input)
    print(type(freqDict))
    print(max(freqDict.values()))
if __name__=="__main__":
    input = 'ant magenta magnate tan gnanate'
    maxAnagramSize(input)       