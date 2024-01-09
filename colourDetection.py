import cv2
import pandas as pd


# Reading the image in opencv
img = cv2.imread("SJR05678.jpg")

# declaring global variables which are used later
clicked = False
r = g = b = xpos = ypos = 0

# Read csv colors files with pandas
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("colors.csv", names=index, header=None)


# Function to get colour name
def getColorName(r, g, b):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(r - int(csv.loc[i, "R"])) + abs(g - int(csv.loc[i, "G"])) + abs(b - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


# Functio to get the x,y co-ordinates
def draw_function(event, x, y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r, g, b, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_function)

while True:
    cv2.imshow("Image", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = getColorName(r, g, b) + "R=" + str(r) + "G=" + str(g) + "B=" + str(b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
