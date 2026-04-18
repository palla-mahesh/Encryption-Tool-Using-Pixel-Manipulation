# Encryption-Tool-Using-Pixel-Manipulation
👉 A beginner-friendly project that encrypts and decrypts images using pixel manipulation techniques, built with Python, Tkinter, and Pillow.
# 🖼️ Image Encryption Tool with GUI (Python & Tkinter)

## 📌 Description

This project is a **GUI-based Image Encryption Tool** developed using **Python**. It uses **pixel manipulation techniques** to encrypt and decrypt images by modifying RGB values and swapping color channels.

This project is part of my **SkillCraft Technology Internship (Task 02)** and focuses on applying basic cybersecurity concepts to image data.

## 🚀 Features

* 🔐 Encrypt images using a numeric key
* 🔓 Decrypt images back to original form
* 🔄 Pixel-level data transformation
* 🎨 RGB channel swapping
* 🖥️ Simple and user-friendly GUI

## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI)
* Pillow (Image Processing)

## 📂 Project Structure

```
image-encryption-tool/
│
├── image_encryptor.py
├── README.md
├── requirements.txt
└── screenshots/
```
## ▶️ How to Run

### 1️⃣ Install Python

Download from: https://www.python.org

✔ Add Python to PATH

---

### 2️⃣ Install Dependencies

```
pip install Pillow
``
---

### 3️⃣ Run the Application

```
python image_encryptor.py
```
## 💡 How It Works

* Each pixel contains RGB values `(R, G, B)`
* Encryption:

  * Adds a key to each value
  * Swaps color channels `(R→G, G→B, B→R)`
* Decryption:

  * Reverses the swap
  * Subtracts the key

## 🖼️ Example Workflow

```
Original Image → Encrypt (Key) → Distorted Image  
Distorted Image → Decrypt (Same Key) → Original Image
```

## 🎯 Use Cases

* Learning image encryption basics
* Understanding pixel manipulation
* Cybersecurity demonstrations
* Academic and hackathon projects

## ⚠️ Limitations

* Basic encryption method
* Not suitable for real-world secure systems

## 🔮 Future Enhancements

* Image preview in GUI
* Drag-and-drop support
* Strong encryption (AES)
* Batch image processing
## 👨‍💻 Author

Palla Venkata Mahesh
GitHub: https://github.com/palla-mahesh

## 📜 License

This project is licensed under the MIT License.

⭐ If you like this project, give it a star!
