listy = [] ##create empty list
for i in range(1,6):
    listy.append(int(input(f"Enter number {i}: "))) #pull in 5 values
print(f"Sum: {sum(listy)}") #print sum
print(f"Largest: {max(listy)}") #print max
print(f"Smallest: {min(listy)}") #print min
print(f"Average: {sum(listy)/len(listy)}") #print average