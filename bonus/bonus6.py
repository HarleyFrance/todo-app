# contents = ["The wind whispered secrets through the tall grass.", "A single drop of rain landed on her hand, cold and unexpected.", "He laughed quietly, unsure if he was supposed to."]
# filenames = ["doc.txt", "report.txt", "presentation.txt"]
#
#
# for content, filename in zip(contents, filenames):
#     file = open(f"../files/{filename}", 'w')
#     file.write(content)

# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
#
#
#
# for country in countries:
#     file = open(f"../files/{country}.txt", 'w')
#     file.write(country)
#     file.close()

# prompt = input("Enter a new member: ")
# file = open("../files/members.txt", 'a')
# file.write(prompt + "\n")
# print(f"{prompt} has been added to the file")
# file.close()


# filenames = ['doc.txt', 'report.txt','presentation.txt']
#
#
# for filename in filenames:
#     file =  open(f"../files/{filename}", 'w')
#     file.write("Hello")
#     file.close()

# filenames = ['a.txt', 'b.txt', 'c.txt']
#
# for filename in filenames:
#     file = open(f"../files/{filename}", 'r')
#     content = file.read()
#     file.close()
#     print(content)

filename = 'data.txt'


file = open(f"../files/{filename}", 'w')

file.write("100.12" + "\n")
file.write("101.12" + "\n")

file.close()