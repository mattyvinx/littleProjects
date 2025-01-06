sentence = input("Enter a sentence: ") ##ask for input sentence
listy = sentence.split() ##split input into a list of words
dicty = {} ##init empty dictionary
for i in listy: ## iterate through list 
    if i in dicty: ## check if new word, increment if so
        dicty[i] += 1
    else: ##add if new word
        dicty[i] = 1
print("Word frequencies: ") 
for word in dicty: #iterate through dictionary and print item count
    print(f"{word}: {dicty[word]}")



'''
Enter a sentence: hello world hello python world
Word frequencies:
hello: 2  
world: 2  
python: 1
'''