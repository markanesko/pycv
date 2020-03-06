# USAGE
# python adjust_gamma.py --image example_01.png

# import the necessary packages
from __future__ import print_function
import numpy as np
import argparse
import cv2
import os
from pathlib import Path

path = os.getcwd()

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")

	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image")
#args = vars(ap.parse_args())

for i in os.listdir(path):
    # load the original image
    if i.endswith('.jpg'):
        original = cv2.imread(os.path.join(path, i))
        
        # loop over various values of gamma
        # for gamma in np.arange(0.0, 3.5, 0.5):
        # ignore when gamma is 1 (there will be no change to the image)
        gamma = 1.67

        # apply gamma correction and show the images
        gamma = gamma if gamma > 0 else 0.1
        adjusted = adjust_gamma(original, gamma=gamma)
        cv2.putText(adjusted, "g={}".format(gamma), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        #cv2.imshow("Images", adjusted)

        Path(os.path.join(path, 'gama')).mkdir(parents=True, exist_ok=True)
        cv2.imwrite(os.path.join(path, 'gama', i.split('-1-4')[0] + '_gama167.jpg'), adjusted)

