import cv2
import glob
import os
import numpy as np

OLD_SAMPLE = r"C:\Users\Lenovo\Documents\Projects\Ss_name_chhange\old_patch.jpeg"
NEW_PATCH = r"C:\Users\Lenovo\Documents\Projects\Ss_name_chhange\patch4.jpeg"

# ✅ NEW: output folder
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


old_patch = cv2.imread(OLD_SAMPLE)
new_patch = cv2.imread(NEW_PATCH)

if old_patch is None or new_patch is None:
    raise Exception("Missing old_patch.jpeg or patch.jpeg")

oh, ow = old_patch.shape[:2]
nh, nw = new_patch.shape[:2]


def process(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    old_gray = cv2.cvtColor(old_patch, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray, old_gray, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    count = 0

    for (y, x) in zip(*locations):
        # img[y:y+nh, x:x+nw] = new_patch
        patch = new_patch.copy()

        # estimate patch background from corners (more robust)
        corners = np.array([
            patch[0,0], patch[0,-1],
            patch[-1,0], patch[-1,-1]
        ])
        bg_color = corners.mean(axis=0)

        # create tolerant mask (handles compression noise)
        diff = np.linalg.norm(patch - bg_color, axis=2)
        mask = diff < 20   # tolerance (10–30 works well)

        # sample target background
        target_bg = img[y, x]

        # recolor background pixels
        patch[mask] = target_bg

        img[y:y+nh, x:x+nw] = patch

        count += 1

    # ✅ ONLY CHANGE HERE
    out = os.path.join(OUTPUT_DIR, "fixed_" + os.path.basename(img_path))

    cv2.imwrite(out, img)

    print(f"Fixed {count} occurrence(s) in:", out)


images = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg")

for f in images:
    if f in [OLD_SAMPLE, NEW_PATCH]:
        continue
    process(f)
