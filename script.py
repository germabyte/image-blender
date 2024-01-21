import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog, simpledialog
from PIL import Image, ImageTk

def blend_images(image1_path, image2_path, num_intermediates):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Ensure both images are the same size
    h1, w1 = image1.shape[:2]
    h2, w2 = image2.shape[:2]
    h, w = min(h1, h2), min(w1, w2)
    image1 = cv2.resize(image1, (w, h))
    image2 = cv2.resize(image2, (w, h))

    intermediates = []
    for i in range(1, num_intermediates + 1):
        alpha = i / (num_intermediates + 1)
        blended = cv2.addWeighted(image1, 1 - alpha, image2, alpha, 0)
        intermediates.append(blended)

    return intermediates

def save_intermediates(intermediates, base_name="intermediate"):
    for i, image in enumerate(intermediates):
        cv2.imwrite(f"{base_name}_{i+1}.png", image)

def select_image1():
    global image1_path
    image1_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if image1_path:
        load_image(image1_path, label_image1)

def select_image2():
    global image2_path
    image2_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if image2_path:
        load_image(image2_path, label_image2)

def load_image(image_path, label):
    image = Image.open(image_path)
    image = image.resize((250, 250))  # Updated this line
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

def generate_intermediates():
    num_intermediates = simpledialog.askinteger("Input", "Number of intermediary images (max 100):",
                                                parent=root, minvalue=1, maxvalue=100)
    if image1_path and image2_path and num_intermediates:
        intermediates = blend_images(image1_path, image2_path, num_intermediates)
        save_intermediates(intermediates)
        label_result.config(text=f"{num_intermediates} intermediates generated and saved.")

root = Tk()
root.title("Image Blender")

image1_path = None
image2_path = None

label_image1 = Label(root)
label_image1.pack()

button_select1 = Button(root, text="Select Image 1", command=select_image1)
button_select1.pack()

label_image2 = Label(root)
label_image2.pack()

button_select2 = Button(root, text="Select Image 2", command=select_image2)
button_select2.pack()

button_generate = Button(root, text="Generate Intermediates", command=generate_intermediates)
button_generate.pack()

label_result = Label(root, text="")
label_result.pack()

root.mainloop()
