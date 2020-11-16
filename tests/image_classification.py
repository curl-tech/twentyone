import argparse
import yaml
import time
from pathlib import Path

import glob

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

import sys
sys.path.append("src")
sys.path.append("src/yolo")

from detect import detect

if __name__ == '__main__':

    img_folder = "tests/img/"

    files = glob.glob(img_folder+"*.jpg")

    for file in files:
        img_source = "tests/img/batch_3_IMG_5037.jpg"
        with torch.no_grad():
            img, text = detect(file)

        img_small = cv2.resize(img, None, fx = 0.35, fy = 0.35)
        cv2.imshow("Image", img_small)
        cv2.waitKey(0)

        print(text)
