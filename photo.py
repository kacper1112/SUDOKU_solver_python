import cv2
import numpy as np
import os

def prep_image(image):
    # convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    edges = cv2.Canny(gray, 50, 150)
    # inverted = cv2.bitwise_not(image)
    # inverted = cv2.cvtColor(inverted, cv2.COLOR_BGR2GRAY)
    # return inverted
    return edges


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    for line in lines:
        for rho, theta in line:
            dgr = (theta * 180) / np.pi
            if (-5 <= dgr and dgr <= 5) or (85 <= dgr <= 95):
                # print((theta * 180) / np.pi)
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1200 * (-b))
                y1 = int(y0 + 1200 * (a))
                x2 = int(x0 - 1200 * (-b))
                y2 = int(y0 - 1200 * (a))
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    return line_image

filename = 'image2.jpg'
source = cv2.imread('images/' + filename)
image = np.copy(source)
inverted = prep_image(image)
lines = cv2.HoughLines(inverted, 1, np.pi / 180, 200)
line_image = display_lines(image, lines)

result = cv2.addWeighted(image, 0.8, line_image, 1, 1)

os.chdir(os.getcwd() + '/images')
if cv2.imwrite(filename[:-4] + '_result.jpg', result):
    print('Success')
else:
    print('Something went wrong :))')
