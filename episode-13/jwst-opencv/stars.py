#!/usr/bin/env python3

import cv2
import numpy as np

import os
import sys


def imshow(*args: np.ndarray) -> None:
    for idx, im in enumerate(args):
        cv2.imshow("image_" + str(idx), im)
    while True:
        if cv2.waitKey(0) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


def draw_blobs(im: np.ndarray) -> np.ndarray:
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 5
    params.maxThreshold = 300
    params.filterByArea = True
    params.minArea = 100
    params.filterByCircularity = True
    params.minCircularity = 0.01
    params.filterByConvexity = True
    params.minConvexity = 0.2
    params.filterByInertia = False
    params.minInertiaRatio = 0.5

    detector = cv2.SimpleBlobDetector_create(params)
    im_grayscale = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_grayscale_inverted = cv2.absdiff(im_grayscale, 255)
    keypoints = detector.detect(im_grayscale_inverted)
    print(f"blobs detected: {len(keypoints)}")
    im_with_blobs = cv2.drawKeypoints(
        im,
        keypoints,
        None,
        (0, 0, 255),
        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
    )
    return im_with_blobs


def main(image_path: str) -> None:
    im = cv2.imread(image_path)
    im_with_blobs = draw_blobs(im)
    imshow(im_with_blobs)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_image>", file=sys.stderr)
        sys.exit(0)
    main(os.path.join(os.getcwd(), sys.argv[1]))
