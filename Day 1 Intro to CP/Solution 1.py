# Question is provided in the Question text file.
n=int(input())
for i in range(n):
    word=input()
    if len(word)==3:
        if ('o' in word and 'e' in word) or ('o' in word and 'n' in word) or ('n' in word and 'e' in word):
            print(1)
        else:
            print(2)
    else:
        print(3)