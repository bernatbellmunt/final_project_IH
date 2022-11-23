import numpy as np
import pandas as pd
import cv2



index=["color", "color_name", "hex", "R", "G", "B"]
color_csv = pd.read_csv('datasets/colors.csv', names=index, header=None)



def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(color_csv)):
        d = abs(R- int(color_csv.loc[i,"R"])) + abs(G- int(color_csv.loc[i,"G"]))+ abs(B- int(color_csv.loc[i,"B"]))
        if(d=minimum):
            minimum = d
            cname = color_csv.loc[i,"color_name"]
    return cname



def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

