import glob

myFiles = glob.glob("files/*.txt")


for filepath in myFiles:
    with open(filepath, "r") as myFile:
        print(myFile.read())
