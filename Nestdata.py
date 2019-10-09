#=========================================================================================
import json 
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
US_count = []
US_count.append(nested_d['Beijing']['USA'] )
US_count.append(nested_d['London']['USA']  )
US_count.append(nested_d['Rio']['USA'] )

print(US_count) 
# #US_count = int(nested_d['Beijing']['USA'])+ int(nested_d['London']['USA']) + int(nested_d['Rio']['USA'])
# print (US_count)
# print(nested_d.keys())

 

#=========================================================================================
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third= []  

for list_item in l_of_l:
    count = 0 
    for item in list_item:
        if  (count == 2):
            third.append(item)
        count += 1

 
#=========================================================================================


athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = []
other = []
for athlete_lst in athletes:
    for name in athlete_lst:
        if  ('t' in  name):
            t.append(name)
        else:
            other.append(name)
print (t)
print (other)
