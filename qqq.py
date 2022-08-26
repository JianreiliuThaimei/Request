# import requests
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
# print(r)
# print(r.content)


import requests
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print(r.url)
print(r.status_code)