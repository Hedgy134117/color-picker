#libraries
import pyautogui
from PIL import Image
import PySimpleGUI as sg
import time

# function for getting the color of an area on screen
def getColor():
    # position of the mouse
    curPos = pyautogui.position()
    # get an image (the pixel of where the cursor is), call it "a.gif"
    im = pyautogui.screenshot("a.gif", region=(curPos[0], curPos[1], 1, 1))
    # width and height (1, 1) of the image
    width, height = im.size
    for i in range(width):
        for j in range(height):
            # get the color
            curPixel = im.getpixel((i, j))
            # print it to the console
            print(curPixel)
            # return the string of the color
            return str(curPixel)

# layout of GUI
layout = [
    [sg.Text("WARNING: After clicking the Start button, you have 3 seconds to hover over the are you want.")],
    [sg.Text("Colors Appear here", key="color")],
    [sg.Button("Start")]
]

# create the window
window = sg.Window("Color Picker").Layout(layout)

# infinite loop
while True:
    # any button clicks or other events
    event, values = window.Read()

    # if the start button is clicked
    if event == "Start":
        # wait 3 seconds to let the user hover over the area they want
        time.sleep(3)
        # get the text and replace it with the RGB value of the pixel
        window.FindElement("color").Update(getColor())


