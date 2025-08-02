import tkinter as tk
from PIL import Image, ImageTk
import os

# ✅ global cache for images so Tkinter doesn’t delete them
images_cache = []

# ✅ map stitches to file paths
STITCH_IMAGES = {
    "slst": "images/slst.png",
    "ch": "images/ch.png",
    "sc": "images/sc.png",
    "hdc": "images/hdc.png",
    "dc": "images/dc.png"
}

def draw_stitches(parsed_pattern):
    print("🖼 draw_stitches called with:", parsed_pattern)  # DEBUG PRINT

    root = tk.Toplevel()  # ✅ Use Toplevel so it opens a *new* window without killing main GUI
    root.title("Crochet Diagram")
    canvas = tk.Canvas(root, width=1000, height=400, bg="white")
    canvas.pack()

    global images_cache
    x, y = 50, 100  # start position

    for stitch, count in parsed_pattern:
        img_path = STITCH_IMAGES.get(stitch)

        if not img_path:
            print(f"⚠️ No image found for stitch '{stitch}'")
            continue

        if not os.path.exists(img_path):
            print(f"🚨 File not found: {img_path}")
            continue

        # ✅ load & resize image
        pil_img = Image.open(img_path)
        pil_img = pil_img.resize((64, 64))  # adjust size here
        img = ImageTk.PhotoImage(pil_img)

        images_cache.append(img)  # store reference globally

        for _ in range(count):
            print(f"✅ Drawing {stitch} at x={x}, y={y}")  # DEBUG PRINT
            canvas.create_image(x, y, image=img, anchor="center")
            x += 70  # spacing between images

    root.mainloop()
