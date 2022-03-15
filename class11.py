word = 'itcbootcamp123course3445'
numbers = []
letters = []
for i in word:
    if i.isdigit():
        numbers.append(int(i))
    else:
        letters.append(i)
print(numbers)
print(''.join(letters))
        
