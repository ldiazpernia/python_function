import requests
dest_url = "https://www.google.com/"
d = {"tbm": "violins",}
resp = requests.get(dest_url, params = d)
print(resp.url)
print(resp.text[:14400])

#https://www.google.com/search?tbm=isch&q=%22violins+and+guitars%22