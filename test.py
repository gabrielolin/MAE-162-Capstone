#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import copy
import argparse
import itertools
from collections import Counter
from collections import deque

#from picamera2 import Picamera2

import cv2 as cv
import numpy as np
import mediapipe as mp

from cv2 import VideoCapture
from cv2 import waitKey

from utils import CvFpsCalc
from model import KeyPointClassifier
from model import PointHistoryClassifier

cap = cv.VideoCapture('dev/video0',cv.CAP_V4L)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 2650)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1440)
ret,frame = cap.read()
cv.imwrite('image.jpg',frame)
cap.release

