# #compare userid and password
# userid = "abc@gmail.com"
# password ="abc#123"
#
# uid = input("Enter user id : ")
# pwd = input("Enter password : ")
#
# print("Login Successful : ", uid == userid and pwd == password)

# input a character and check whether it is in upper case or lower case

char = input("Enter a character : ")

print(f"{char} is in upper case : {char>='A' and char<='Z'}")#  'A' <= char <= 'Z'
print(f"{char} is in lower case : {char>='a' and char<='z'}")#  'a' <= char <= 'z'


# check whether a character is an alphabet or not
print(f"{char} is an alphabet : {('A' <= char <= 'Z') or ('a' <= char <= 'z')}")


print(f"{char} is a vowel : {char in 'aeiouAEIOU'}")
print(f"{char} is a consonant : {char not in 'aeiouAEIOU'}")

# check if a character is a vowel or not using or operator