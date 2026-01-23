import FreeSimpleGUI as sg
from zipExtractor import zip_extract

sg.theme('DarkBlue')
layout=[
    [sg.Text('Select Archive'), sg.Input(), sg.FileBrowse(button_text='Choose',key='archive')],
    [sg.Text('Select Destination'), sg.Input(), sg.FolderBrowse(button_text='Choose',key='folder')],
    [sg.Button("Extract"), sg.Text(key='output', text_color='green')],

]

window = sg.Window('Archive Extractor', layout)

while True:
    event, values = window.read()
    print(event, values)
    archive = values['archive']
    destination_dir = values['folder']
    zip_extract(archive, destination_dir)
    window['output'].update(value='Files Extracted successfully!')


window.close()