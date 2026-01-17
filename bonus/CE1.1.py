import FreeSimpleGUI as sg

layout=[
    [sg.Text("Enter Feet: "),sg.InputText(key="feet")],
    [sg.Text("Enter Inches: "),sg.InputText(key="inches")],
    [sg.Button("Convert"), sg.Text(key="convert")],]


window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    match event:
        case "Convert":
            meters = float(values["feet"]) * 0.3048 + float(values["inches"]) * 0.0254
            window["convert"].update(f"{meters:.3f} m")
        case sg.WIN_CLOSED:
            exit()
window.read()
window.close()
