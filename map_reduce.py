
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing  = list(map(lambda st : "Fruit: "+st , lst_check))
print (map_testing)



countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = list(filter( lambda word : "B" in word , countries))
print (b_countries)


people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names  = [x2 for x1 , x2 in people ]
print (first_names)



lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2   = [x1*2 for x1  in lst ]
print (lst2 )

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [name for name , grade in students if grade >= 70 ]
print(passed)



l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = [(x1,x2) for (x1, x2) in list(zip(l1, l2)) if len(x1) > 3]
print(opposites)



species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = [ (x1,x2) for (x1, x2) in list(zip(species, population))   ]
#endangered = list(filter( lambda x : x[1]<=2500 , pop_info))
endangered = [ (x1) for (x1, x2) in list(filter( lambda x : x[1]<=2500 , pop_info))]


print (endangered)


