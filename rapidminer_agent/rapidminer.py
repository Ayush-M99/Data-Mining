import cv2
import glob
import os

PATCH_FILE = "rapidminer_agent/rapidminer_patch.jpeg"

patch = cv2.imread(PATCH_FILE)

if patch is None:
    raise Exception("patch.jpeg not found")

ph, pw = patch.shape[:2]


def process(img_path):
    img = cv2.imread(img_path)

    # paste patch directly at top-left
    img[0:ph, 0:pw] = patch

    out = "fixed_" + os.path.basename(img_path)
    cv2.imwrite(out, img)

    print("Fixed:", out)


images = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg")

for f in images:
    if f == PATCH_FILE:
        continue
    process(f)