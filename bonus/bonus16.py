import FreeSimpleGUI as sg

layout=[[sg.Text("Select files to compress: "),sg.InputText(), sg.FilesBrowse("Choose")], [sg.Text("Select destination folder: "),sg.InputText(), sg.FolderBrowse("Choose")],[sg.Button("Compress")]]
# layout=[[sg.Text("Enter feet: "), sg.InputText()], [sg.Text("Enter inches"), sg.InputText()],[sg.Button("Compress")]]
window = sg.Window('Convert', layout)
window.read()
window.close()
