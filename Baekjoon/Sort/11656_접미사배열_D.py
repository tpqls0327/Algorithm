word = input()
print(*sorted([word[i:] for i in range(len(word))]), sep='\n')
