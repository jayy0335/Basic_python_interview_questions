# Question 1: Write a Python program to check if a string is a palindrome. 



#  def is_palindrome(string):
#     reversed_string = string[-1:]  <-- #yahan me ghalti kr raha tha
#     return string == reversed_string
#
# #test the function
#
# word = "civic"
# if is_palindrome(word):
#     print(f"{word} is palindrome")
# else:
#     print(f"{word} isn't palindrome")


# check=["mansoor","ali","Khan"]
# h=check[::-1] # increment -1,-2,-3,-4,-5
# print(h)


def is_palindrome(string):
    reversed_string=string[::-1]
    return  string==reversed_string

# check the function
word="maham"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")