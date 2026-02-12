# Data-Mining

Utilities to automatically replace registration numbers inside screenshots for **RapidMiner** and **Talend** using OpenCV template matching.

---

## ⚠️ Disclaimer

### RapidMiner

Works **reliably** for the top registration number area.

Make sure:

* The registration number appears only once
* No duplicates elsewhere in the screenshot

---

### Talend

Talend is **tricky and inconsistent**.

Because Talend uses:

* different fonts
* different weights
* different colors
* multiple UI styles

The script may leave **1–4 registration numbers unedited**.

If that happens, it's usually faster to manually edit the number directly inside Talend.

---

## 📁 Project Structure

```
rapidminer_agent/
│   rapidminer.py
│   rapidminer_patch/

talend_agent/
│   talend.py
│   talend_oldpatch/
│   talend_newpatch/
```

---

## 🔧 Requirements

```bash
pip install -r requirements.txt
```

---

# 🚀 RapidMiner Usage

1. Put all screenshots inside `rapidminer_agent/`
2. Add your patch image inside `rapidminer_patch/`
3. Ensure everything is in the same folder:

   ```
   rapidminer.py
   rapidminer_patch/
   your_images.png
   ```
4. Run:

   ```bash
   python rapidminer.py
   ```

---

# 🚀 Talend Usage

Talend requires **two patches**:

* `talend_oldpatch` → crop of the existing registration number (used for detection)
* `talend_newpatch` → replacement number image

### Steps

1. Put all screenshots inside `talend_agent/`
2. Place your patches:

   ```
   talend_oldpatch/
   talend_newpatch/
   ```
3. Ensure structure:

   ```
   talend.py
   talend_oldpatch/
   talend_newpatch/
   your_images.png
   ```
4. Run:

   ```bash
   python talend.py
   ```

---

## 🧠 How it Works

* Template matching (OpenCV)
* Finds old registration number
* Recolors background
* Replaces with new patch

---

## ✅ Notes

* RapidMiner → very reliable
* Talend → partial success expected due to UI inconsistencies

---

## Author

Ayush Mishra
