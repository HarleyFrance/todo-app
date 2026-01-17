import FreeSimpleGUI as sg
from zip_creator import make_archive

layout=[
    [sg.Text("Select files to compress: "),sg.InputText(), sg.FilesBrowse("Choose", key="files")],
    [sg.Text("Select destination folder: "),sg.InputText(), sg.FolderBrowse("Choose", key="folder")],
    [sg.Button("Compress")]]
# layout=[[sg.Text("Enter feet: "), sg.InputText()], [sg.Text("Enter inches"), sg.InputText()],[sg.Button("Compress")]]
window = sg.Window('Convert', layout)


while True:
    event, values = window.read()
    match event:
        case "Compress":
            print(f"Event: {event}")
            print(f"Values: {values}")
            filepath = values["files"].split(";")
            folder = values["folder"]
            make_archive(filepath, folder)
        case sg.WIN_CLOSED:
            exit()

window.read()
window.close()
