import PySimpleGUI as sg
from spongebobcase import SpongeBobCase as SBC

sbc = SBC()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Spongebob Case')],
            [sg.Text('Enter the text you wish to manipulate'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    output = sbc.alternatingCase(values)
    
        
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('The converted text is: ', output)

window.close()