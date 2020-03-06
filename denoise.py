import cv2 as cv
import numpy as np

import os
from pathlib import Path

cwd = os.getcwd()
test_data = os.path.join(cwd, 'test_data')

result_name = 'denoised_3_3_7_21'

def denoise(images_folder):
    Path(os.path.join(images_folder, result_name)).mkdir(parents=True, exist_ok=True)
    for i in os.listdir(images_folder):
        if i.endswith('.jpg'):
            img = cv.imread(os.path.join(images_folder, i))

            modified = cv.fastNlMeansDenoisingColored(img, None, 3, 3, 7, 21) # check parameters

            cv.imwrite(os.path.join(images_folder, result_name, i), modified)

    return 0

def main():

    denoise(test_data)

    return 0

main()