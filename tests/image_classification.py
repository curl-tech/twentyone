import argparse
import yaml
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

import sys
sys.path.append("src")
sys.path.append("src/yolo")

from detect import detect

if __name__ == '__main__':

    img_source = "tests/img/batch_1_000010.jpg"

    with torch.no_grad():
        img, text = detect(img_source)

    print(text)
