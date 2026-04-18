import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# ---------------- Image Functions ---------------- #
def encrypt_image(img, key):
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Simple encryption logic (add key + swap)
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[i, j] = (g, b, r)  # swap channels

    return img


def decrypt_image(img, key):
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            g, b, r = pixels[i, j]  # reverse swap

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[i, j] = (r, g, b)

    return img


# ---------------- GUI Functions ---------------- #
def open_image():
    global img, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if img_path:
        img = Image.open(img_path)
        messagebox.showinfo("Success", "Image loaded successfully!")


def save_image(image):
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        image.save(save_path)
        messagebox.showinfo("Saved", "Image saved successfully!")


def perform_encrypt():
    if not img:
        messagebox.showerror("Error", "Please load an image first!")
        return

    key = key_entry.get()
    if not key.isdigit():
        messagebox.showerror("Error", "Enter a valid numeric key!")
        return

    encrypted = encrypt_image(img.copy(), int(key))
    save_image(encrypted)


def perform_decrypt():
    if not img:
        messagebox.showerror("Error", "Please load an image first!")
        return

    key = key_entry.get()
    if not key.isdigit():
        messagebox.showerror("Error", "Enter a valid numeric key!")
        return

    decrypted = decrypt_image(img.copy(), int(key))
    save_image(decrypted)


# ---------------- GUI Design ---------------- #
root = tk.Tk()
root.title("Image Encryption Tool")
root.geometry("400x300")
root.config(bg="#1e1e2f")

img = None
img_path = ""

title = tk.Label(root, text="Image Encryption Tool", font=("Arial", 16, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=15)

# Load Button
tk.Button(root, text="Load Image", command=open_image,
          bg="#4CAF50", fg="white", width=20).pack(pady=5)

# Key Entry
tk.Label(root, text="Enter Key:", bg="#1e1e2f", fg="white").pack()
key_entry = tk.Entry(root)
key_entry.pack(pady=5)

# Encrypt / Decrypt Buttons
tk.Button(root, text="Encrypt Image", command=perform_encrypt,
          bg="#2196F3", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Decrypt Image", command=perform_decrypt,
          bg="#ff9800", fg="white", width=20).pack(pady=5)

# Run App
root.mainloop()