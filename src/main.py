# Usage: python main.py filepath

from helpers import implt
import cv2
import sys
import page
import words
import os
from recognize import recognize
import shutil

if len(sys.argv) < 2:
    print('Usage: python main.py filepath')
    sys.exit(1)

IMG = sys.argv[1]
image = cv2.cvtColor(cv2.imread(IMG), cv2.COLOR_BGR2RGB)
implt(image)

# Crop image and get bounding boxes
crop = page.detection(image)
implt(crop)
boxes = words.detection(crop)
lines = words.sort_words(boxes)
numberOfLines = len(lines)

if os.path.exists('../out/'):
    shutil.rmtree('../out')
if not os.path.exists('../out/'):
    os.mkdir('../out/')

for i in range(numberOfLines):
    if not os.path.exists('../out/' + str(i) + '/'):
        os.mkdir('../out/' + str(i) + '/')
    numberOfWords = len(lines[i])
    for j in range(numberOfWords):
        word = crop[lines[i][j][1]:lines[i][j][3], lines[i][j][0]:lines[i][j][2]]
        cv2.imwrite('../out/' + str(i) + '/' + str(j) + '.png', word)

recognize()

# Word crop
# crop_img = crop[lines[0][0][1]:lines[0][0][3], lines[0][0][0]:lines[0][0][2]]
# cv2.imwrite('crop.png', crop_img)
# implt(crop_img)

# Crude line crop
# crop_img = crop[lines[0][0][1]:lines[0][12][3], lines[0][0][0]:lines[0][12][2]]
# implt
