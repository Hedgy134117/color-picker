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
    # get an image of the area of where the cursor is
    im2 = pyautogui.screenshot("b.gif", region=(curPos[0], curPos[1], 100, 100))
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
    [sg.Text("Delay"), sg.InputText("3", size=(2, 1), key="delay"), sg.Text("(seconds)")],
    [sg.Text("Colors Appear here", key="color"), sg.Image("b.gif", key="image"), sg.Text("<- Preview Image")],
    [sg.Button("Start"), sg.Quit()]
]

# create the window
window = sg.Window("Color Picker").Layout(layout)

# info for the user
print("This is the console, it will show all previous RGB values.")
print("When hovering over an area, it will look at the color of the top left area of the cursor.")

# infinite loop
while True:
    # any button clicks or other events
    event, values = window.Read()

    # if the quit button is clicked
    if event == "Quit":
        # end the infinite loop
        break

    # if the start button is clicked
    if event == "Start":
        # get the delay that the user inputed and wait that amount of seconds
        time.sleep(int(values['delay']))
        # get the text and replace it with the RGB value of the pixel
        window.FindElement("color").Update(getColor())
        # get the image of the cursor area and replace it with the new image of the cursor area
        window.FindElement("image").Update("b.gif")
