import tkinter as tk
from PIL import Image, ImageTk   # 👈 NEW: import Pillow

# Map stitches to image file paths
STITCH_IMAGES = {
    "slst": "images/slst.png",
    "ch": "images/ch.png",
    "sc": "images/sc.png",
    "hdc": "images/hdc.png",
    "dc": "images/dc.png"
}

def draw_stitches(parsed_pattern):
    root = tk.Tk()
    root.title("Crochet Visualizer (with resized images)")

    canvas = tk.Canvas(root, width=1000, height=400, bg="white")
    canvas.pack()

    x, y = 50, 100  # starting position

    images_cache = []  # 🛑 keep a reference to avoid garbage collection

    for stitch, count in parsed_pattern:
        img_path = STITCH_IMAGES.get(stitch)
        if img_path:
            # ✅ Load image with Pillow & resize it
            pil_img = Image.open(img_path)
            pil_img = pil_img.resize((64, 64))  # 🎯 adjust size here
            img = ImageTk.PhotoImage(pil_img)

            images_cache.append(img)  # store reference
            
            # ✅ Draw each stitch as many times as count says
            for _ in range(count):
                canvas.create_image(x, y, image=img, anchor="center")
                x += 70  # spacing between images (resize + padding)

    root.mainloop()
