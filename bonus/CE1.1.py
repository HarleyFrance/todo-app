# import FreeSimpleGUI as sg
#
# layout=[
#     [sg.Text("Enter Feet: "),sg.InputText(key="feet")],
#     [sg.Text("Enter Inches: "),sg.InputText(key="inches")],
#     [sg.Button("Convert"),sg.Button("Exit"), sg.Text(key="convert")]]
#
#
# window = sg.Window('Converter', layout)
#
# while True:
#     event, values = window.read()
#     match event:
#         case "Convert":
#             meters = float(values["feet"]) * 0.3048 + float(values["inches"]) * 0.0254
#             window["convert"].update(f"{meters:.3f} m")
#         case "Exit":
#             exit()
#         case sg.WIN_CLOSED:
#             exit()
# window.read()
# window.close()
import FreeSimpleGUI as sg


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


sg.theme("Black")

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, exit_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Convert':
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                result = convert(feet, inches)
                window["output"].update(value=f"{result} m", text_color="white")
            except ValueError:
                sg.popup(
                    "Please provide two numbers.",
                    title="Invalid Input",
                    keep_on_top=True
                )

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()
