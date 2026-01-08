#Requirements
#password must be 8 characters or longer
#must contain at least 1 digit
#must contain at least 1 uppercase

#if all requirements are met it returns "Strong Password" otherwise "Weak Password"


# user_password = input("Enter your password: ")
#
#
#
# if len(user_password) >= 8 and any (digit.isdigit() for digit in user_password) and  any (letter.isupper() for letter in user_password):
#     print("Strong Password")
# else:
#     print("Weak Password")

# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)

# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)

# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
#
# perimeter = (length + width) * 2
# area = length * width
#
# print("Perimeter is", perimeter)
# print("Area is", area)
#
# if perimeter < 14 and area < 8:
#     print("OK")
# else:
#     print("NOT OK")
x = 0

if len("Hello") == 5:
    x = x + 1
elif len("Hello") > 5:
    x = x + 2
else:
    x = x + 3