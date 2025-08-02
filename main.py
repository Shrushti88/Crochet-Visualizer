import tkinter as tk
from pattern_parser import parse_pattern
from PIL import Image, ImageTk
import os

# 🔗 IMAGE PATHS
STITCH_IMAGES = {
    "slst": "images/slst.png",
    "ch": "images/ch.png",
    "sc": "images/sc.png",
    "hdc": "images/hdc.png",
    "dc": "images/dc.png"
}

# ✅ keep images alive so they don’t vanish
images_cache = []

def generate_diagram():
    # clear previous diagram
    canvas.delete("all")
    images_cache.clear()

    pattern_text = entry.get()
    if pattern_text.strip() == "":
        status_label.config(text="⚠️ Please enter a crochet pattern first!", fg="red")
        return

    parsed = parse_pattern(pattern_text)
    print("Parsed pattern:", parsed)  # ✅ debug print

    status_label.config(text="✅ Pattern parsed successfully!", fg="green")

    x, y = 50, 100

    for stitch, count in parsed:
        img_path = STITCH_IMAGES.get(stitch)

        if not img_path:
            print(f"⚠️ No image for {stitch}")
            continue

        if not os.path.exists(img_path):
            print(f"🚨 Missing file: {img_path}")
            continue

        pil_img = Image.open(img_path).resize((64, 64))
        img = ImageTk.PhotoImage(pil_img)
        images_cache.append(img)  # ✅ store ref

        for _ in range(count):
            print(f"Drawing {stitch} at {x}, {y}")
            canvas.create_image(x, y, image=img, anchor="center")
            x += 70  # spacing

# ----------------- GUI -----------------
root = tk.Tk()
root.title("Crochet Visualizer")

# 📝 Entry box
tk.Label(root, text="Enter Crochet Pattern:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)

# 🎛 Button
generate_btn = tk.Button(root, text="Generate Diagram", command=generate_diagram,
                         font=("Arial", 12), bg="#8bc34a", fg="white")
generate_btn.pack(pady=10)

# ✅ Status label
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack()

# 🎨 Canvas to draw diagram directly
canvas = tk.Canvas(root, width=1000, height=400, bg="white")
canvas.pack(pady=20)

root.mainloop()
