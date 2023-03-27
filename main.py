import PySimpleGUI as sg
from spongebobcase import SpongeBobCase as SBC

sbc = SBC()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Spongebob Case')],
            [sg.Text('Enter the text you wish to manipulate'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Checkbox("Alternating Case", default=True, key="-AC-")],
            [sg.Checkbox("Random Case", default=False), sg.Text("--This doesn't work yet")],
            [sg.InputText("", size=(0, 1), key='OUTPUT')]]

# Create the Window
window = sg.Window('Spungyboob', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    
    
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    # If Alternating Case checkbox is clicked, cal function
    if values["-AC-"] == True:
        output = sbc.alternatingCase(values)
    
        
    window['OUTPUT'].update(value=output)

window.close()