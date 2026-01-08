# feat_inches = input("Enter feat and inches: ")
#
#
# def convert(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
# result = convert(feat_inches)
#
# if result < 1:
#     print("Kid is too small")
# else:
#     print("Kid can use slide")

# def strength(password):
#     result = None
#
#     if len(password) >= 8 and any(digit.isdigit() for digit in password) and any(
#             letter.isupper() for letter in password):
#         result = "Strong Password"
#     else:
#         result = "Weak Password"
#
#     return result
#
# user_password = input("Enter your password: ")
# print(strength(user_password))
#
#
# average = sum(numbers) / len(numbers)

# def speed(distance, time):
#     return distance / time
#
#
# print(speed(200, 4))
#
# def speed(distance, time):
#     return distance / time
#
#
# print(speed(300, 5))

def prepare(text):
    text = text.title()
    text = text.strip()
    return text


print(prepare("hello    "))