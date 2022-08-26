# import requests
# x = requests.get
# print(x.text)

# import json

# def post(self,request):
#    if request.is_ajax():
#      if request.method == 'POST':
#         json_data = json.loads(str(request.body, encoding='utf-8'))
#         print(json_data)
#    return HttpResponse('OK!')

# passward=input("enter the passward :")
# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_chr = "!@#$%^&*()-+"
# a,b,c,d=0,0,0,0
# i=0
# while i<len(password):
#     if password[i] in numbers:
#         a+=1
#     if password[i] in lower_case:
#         b+=1
#     if password[i] in upper_case:
#         c+=1
#     if password[i] in special_chr:
#         d+=1
#         i=i+1
# if p>=6:
#     if a>=1 and b>=1 and c>=1 and d>=1 :
#         print("strong password")
#     else:
#         print("invilade")
# else:
#     print("no")



# password=0

# numbers="123456789"
# lower_case="abcdefghijklmnopqrst"
# upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_chr="@#$%&!"
# if len(passward)>=6:
#     if numbers in password:
#         if lower_case in passward:
#             if upper_case in passward:
#                 if special_chr in  passward:
#                     print("strong passward")
#                 else: 
#                     print("enter valid chr")
#             else:
#                 print("enter the valid upper case")
#         else:
#             print("enter the valid lower case")
#     else:
#         print("enter valid number")
# else:
#     print("error")     




# a=int(input("enter the room no:"))
# b=int(input("enter the girls:"))
# c=int(input("enter the beds:"))
# if a=="pm room":
#     if a=="no girls":
#         print("no beds")
#     else:
#         print("go to anther room")
# if a=="cm room":
#     if a=="no girls":
#         print("no beds")
#     else:
#         print("go to anther room")     
# if a=="103":
#     if a=="10 girls":
#         print("5beds")
#     else:
#         print("go to anther room") 
# else:
#     print("go to anther room")        
        
    
        
# a=int(input("enter the number"))   
# if a%7==0:
#     print("it is divisible")  
# else:
#     print("not")

# a=1
# b=2
# c=a
# print(a is c)


# a=("mango","apple")
# b=("grapes","zam")
# print("mango" in a)

# s=("reenu","umma")
# r=("reenu","umma")
# print( "reenu" in s)


import requests
word=input("what word would you like to translate :")
url="https://christianthompson.com/dictionary.py"
params={"word":word}
response=requests.get(url,params)
print(f"status code:{response.status_code}")
print(response.text)


