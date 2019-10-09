# =========================================================================================
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]
#print (output)
# =========================================================================================
# 
# 
        
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
for il1 in lst:
    if 'yellow' in il1:
        yellow= True 
#print (yellow)
#Test to see if 4 is in the second list of lst. Save to variable ``four``
four = ''
for item in lst[1]:
   #print(item)
    if item == 4:
        four = True 
    else:
        four = False 

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
for il1 in lst:
  
    if 'orange' in il1:
        orange = True
        break
    else:
        orange = False
#print (orange)
# =========================================================================================


L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
for ln in L:
    for item in ln:
        if item == 'hola':
            test1 = True
        else:
            test1=  False
 
# Test if [5, 8, 7] is in the list L. Save to variable name test2
Equal = [5, 8, 7]
for ln in L:
   
    if (Equal == ln):
        test2 = True
        break
    else:
        test2=  False
   

# Test if 6.6 is in the third element of list L. Save to variable name test3

for ln in L[2]:
    if 6.6 == ln:
        test3 = True
        break
    else:
        test3=  False
 





        
 
     
 


 
