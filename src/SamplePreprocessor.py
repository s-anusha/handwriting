from __future__ import division
from __future__ import print_function

import random
import numpy as np
import cv2


def preprocess(img, imgSize, dataAugmentation=False):
    "put img into target img of size imgSize, transpose for TF and normalize gray-values"

    # Gaussian filtering
    # blur = cv2.GaussianBlur(img, (5, 5), 0)

    # Normalization
    norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

    # Otsu's thresholding
    ret, th = cv2.threshold(norm, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Morphological tranformation
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)

    # Gaussian blurring to remove noise
    img = cv2.GaussianBlur(opening, (5, 5), 0)

    # cv2.imshow('img', img)
    # cv2.waitKey(0)

    # there are damaged files in IAM dataset - just use black image instead
    if img is None:
        img = np.zeros([imgSize[1], imgSize[0]])

    # increase dataset size by applying random stretches to the images
    if dataAugmentation:
        stretch = (random.random() - 0.5)  # -0.5 .. +0.5
        wStretched = max(int(img.shape[1] * (1 + stretch)), 1)  # random width, but at least 1
        img = cv2.resize(img, (wStretched, img.shape[0]))  # stretch horizontally by factor 0.5 .. 1.5

    # create target image and copy sample image into it
    (wt, ht) = imgSize
    (h, w) = img.shape
    fx = w / wt
    fy = h / ht
    f = max(fx, fy)
    newSize = (max(min(wt, int(w / f)), 1),
               max(min(ht, int(h / f)), 1))  # scale according to f (result at least 1 and at most wt or ht)
    img = cv2.resize(img, newSize)
    target = np.ones([ht, wt]) * 255
    target[0:newSize[1], 0:newSize[0]] = img

    # transpose for TF
    img = cv2.transpose(target)

    # normalize
    (m, s) = cv2.meanStdDev(img)
    m = m[0][0]
    s = s[0][0]
    img = img - m
    img = img / s if s > 0 else img
    return img
