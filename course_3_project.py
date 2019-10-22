#import statements
#import requests_with_caching
# import requests
# import json
#import webbrowser
#apikey = "348077-test-OVT035K1"

# def get_movies_from_tastedive (movie_string):
#     baseurl = "https://tastedive.com/api/similar"
#     parameters = {}
#     parameters["q"] = movie_string
#     parameters["type"] = "movies"
#     parameters["limit"] = "5"
#     parameters["k"] = "348077-test-OVT035K1"
    
#     api_resp = requests.get(baseurl, params = parameters)
#     #api_resp = requests_with_caching.get(baseurl, params = parameters, permanent_cache_file = "permanent_cache.txt") #code 
#     print(api_resp.url) # Paste the result into the browser to check it out...
#     movies_info = api_resp.json() 
#     return movies_info


# def extract_movie_titles(d):
#    return [m['Name'] for m in d['Similar']['Results']]


# def get_related_titles(list_movie_titles):
#     moves_related = []
#     for movie in list_movie_titles:
#         temp_list_json = get_movies_from_tastedive(movie)
#         movies_name = extract_movie_titles(temp_list_json)
#         for name in movies_name:
#             if name not in moves_related:
#                 moves_related.append(name)

#     return moves_related




# movie="Black Panther" 
# movies_json =  get_movies_from_tastedive(movie) 
# #print (json.dumps(movies_json,indent=2) )
# print ('---------Lista de pelis --------------------------')
# lst_movie_titles = extract_movie_titles(movies_json)
# print (lst_movie_titles)
# print ('---------Json de todas las pelis -------------------------------------')
# json_related_titles = get_related_titles(lst_movie_titles)
# print(json_related_titles)




###########################################################################
#total 
###########################################################################

import requests_with_caching
import json

def get_movies_from_tastedive (movie_string):
    baseurl = "https://tastedive.com/api/similar"
    parameters = {}
    parameters["q"] = movie_string
    parameters["type"] = "movies"
    parameters["limit"] = "5"
    api_resp = requests_with_caching.get(baseurl, params = parameters, permanent_cache_file = "permanent_cache.txt") #code 
    return api_resp.json()


def extract_movie_titles(d):
   return [m['Name'] for m in d['Similar']['Results']]

def get_related_titles(list_movie_titles):
    moves_related = []
    for movie in list_movie_titles:
        temp_list_json = get_movies_from_tastedive(movie)
        movies_name = extract_movie_titles(temp_list_json)
       
        for name in movies_name:
            if name not in moves_related:
                moves_related.append(name)

    return moves_related

movie="Black Panther" 
movies_json =  get_movies_from_tastedive(movie) 
print (json.dumps(movies_json,indent=2) )
print ('----------------------------------------------')
lst_movie_titles = extract_movie_titles(movies_json)
print (lst_movie_titles)
print ('----------------------------------------------')
json_related_titles = get_related_titles(lst_movie_titles)
print(json.dumps(json_related_titles,indent=2))


###########################################################################
#total 
###########################################################################



import requests_with_caching
import json

def get_movies_from_tastedive (movie_string):
    baseurl = "https://tastedive.com/api/similar"
    parameters = {}
    parameters["q"] = movie_string
    parameters["type"] = "movies"
    parameters["limit"] = "5"
    api_resp = requests_with_caching.get(baseurl, params = parameters, permanent_cache_file = "permanent_cache.txt") #code 
    return api_resp.json()

def extract_movie_titles(d):
   return [m['Name'] for m in d['Similar']['Results']]


def get_related_titles(list_movie_titles):
    moves_related = []
    for movie in list_movie_titles:
        temp_list_json = get_movies_from_tastedive(movie)
        movies_name = extract_movie_titles(temp_list_json)
       
        for name in movies_name:
            if name not in moves_related:
                moves_related.append(name)

    return moves_related

def get_movie_data (movie_string):
    baseurl = "http://www.omdbapi.com/"
    parameters = {}
    parameters["t"] = movie_string
    parameters["r"] = "json"
    api_resp = requests_with_caching.get(baseurl, params = parameters, permanent_cache_file = "permanent_cache.txt") #code 
    return api_resp.json() 

def get_movie_rating (json_movie_data):
    rtn=0
    for rating in json_movie_data['Ratings']:
        if rating['Source'] == "Rotten Tomatoes":
            print(int((rating['Value'][:2])))
            rtn = (int((rating['Value'][:2])))
    return rtn

def get_sorted_recommendations(movie_list):
    get_recommendations = get_related_titles(movie_list)
    #print (get_recommendations)
    
    
    #rec_sort = sorted(get_recommendations,reverse=True)
    order = sorted(get_recommendations, key=lambda move:(get_movie_rating(get_movie_data(move)), move), reverse=True)
   
    return order

movie  = "Deadpool 2"
print (get_movie_data(movie))
#print (get_movie_rating(get_movie_data(movie)))


