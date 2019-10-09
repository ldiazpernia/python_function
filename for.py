L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings = []

for line in L:
    for word in line: 
      
        if "b" in word :
            b_strings.append(word)
print (b_strings)