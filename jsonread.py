# =========================================================================================
import json
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}
 
# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.

if 'data' in nested.keys():
    data = True
else:
    data = False


# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.

if 24 in nested.values():
    twentyfour = True
else:
    twentyfour = False

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
 
for item in nested['window']:
   
    if 'whole' ==  item:
        whole = False
        break
    else:
        whole = True
 
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
if 'physics' in nested.keys():
    physics = True
else:
    physics = False



#=========================================================================================

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = nested_d['London']['Great Britain'] 
 
#=========================================================================================
import json
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}
print (json.dumps(sports,indent=2))
# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]
print(v1)
# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]
print(v2)
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women'] 
print (v3)
# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][3]
print (v4)









