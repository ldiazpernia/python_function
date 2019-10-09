lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

def doubled (st):
    return 2*st

def doubledStuff(a_list):
    new_seq = map(doubled, a_list)
    return list(new_seq)


greeting_doubled  =   doubledStuff(lst)
print (greeting_doubled)
 

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
def f(st):
    return st.upper()
#abbrevs_upper  = map(f, abbrevs)
abbrevs_upper  = map(lambda st: st.upper(), abbrevs)
 
print (list(abbrevs_upper))


lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled = list(map(lambda doubles : doubles * 2 , lst))
print (greeting_doubled)

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
abbrevs_upper  = list(map(lambda st : st.upper() , abbrevs))
print (abbrevs_upper )

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing = filter( lambda word : "w" in word , lst_check)
print (list(filter_testing))

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2 = filter( lambda word : "o" in word , lst)
print (list(lst2))


L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [item*2 for item in L  if item > 10 ]
print (lst2)


tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
tester_inner=  tester['info']
import json
compri  = [item['name'] for item in tester_inner ]
print (compri)