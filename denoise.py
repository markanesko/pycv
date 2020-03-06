import cv2 as cv
import numpy as np

import os
from pathlib import Path

cwd = os.getcwd()
test_data = os.path.join(cwd, 'test_data')

def denoise(images_folder):
    for i in os.listdir(images_folder):
        if i.endswith('.jpg'):
            img = cv.imread(os.path.join(images_folder, i))

            modified = cv.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21) # check parameters

            Path(os.path.join(images_folder, 'denoised')).mkdir(parents=True, exist_ok=True)
            cv.imwrite(os.path.join(images_folder, 'denoised', i), modified)

    return 0

def main():

    denoise(test_data)

    return 0

main()