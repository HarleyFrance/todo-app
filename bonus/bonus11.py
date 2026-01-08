# def get_average():
#     with open("files/data.txt", "r") as file:
#         data = file.readlines()
#     values = data[1:]
#     values =[float(i) for i in values]
#
#     average = sum(values) / len(values)
#
#     return average
#
# average_total = get_average()
# print(average_total)
def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)