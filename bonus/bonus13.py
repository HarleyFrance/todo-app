from bonus.convert13 import convert
from bonus.parser13 import parse

feet_inches = input("Enter feat and inches: ")

f, i = parse(feet_inches)
print("feet", f, i)
result = convert(f, i)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use slide")
#
# def get_nr_items(user_input):
#     split_user_input = user_input.split(",")
#     word_count = len(split_user_input)
#     return word_count
#
# print(get_nr_items("Hello,World"))
# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
#
#
# time = calculate_time(100)
# print(time)
# def get_area(x=10):
#     return x * 2
#
#
# area = get_area(x=1)
# print(area)