# try:
#     width = float(input("Enter rectangle width: "))
#     length = float(input("Enter rectangle length: "))
#     if width == length:
#         exit("width and must not be equal to length")
#
#     area = (length * width)
#     print("The area of the rectangle is " + str(area))
#     print("width and must not be equal to length")
#
# except ValueError:
#     print("Please enter a number")

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#
#     percentage = (value / total_value * 100)
#     print(f"That is {percentage}%")
#
# except ValueError:
#     print("You need to enter a number. Run the program again.")
# except ZeroDivisionError:
#     print("Your total value cannot be zero.")

# waiting_list = ["john", "marry"]
# name = input("Enter name: ")
#
# try:
#     number = waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
# except ValueError:
#     print(f"Sorry, {name} is not in the list")

try:
    "a" + 2
except TypeError:
    print("Cannot add number to string.")