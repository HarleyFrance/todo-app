# date = input("Enter today's date: ")
# mood = input("How do you rate your mood today from 1 to 10?: ")
# journal_entry = input("Let your thoughts flow: ")
#
# with open(f"../journal/{date}.txt", "w") as file:
#     file.write(f"Mood: {mood}\n")
#     file.write(f"Entry: {journal_entry}")

# languages = ['English', 'German', 'Spanish']
#
# for i in languages:
#     with open(f"../files/{i}.txt", "w") as file:
#         file.write(i)
#

with open("../files/file.txt", 'r') as file:
    content = file.read()
    print(content)
    print(len(content))