import tkinter as tk  # Thư viện Tkinter để tạo giao diện người dùng
from tkinter import filedialog  # Thư viện để mở hộp thoại chọn tệp
from tensorflow.keras.models import load_model  # Thư viện TensorFlow để tải mô hình đã huấn luyện
from tensorflow.keras.preprocessing import image  # Thư viện để xử lý hình ảnh
import numpy as np  # Thư viện NumPy để xử lý mảng
from PIL import Image, ImageTk  # Thư viện Pillow để xử lý ảnh và hiển thị ảnh trên Tkinter
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2

model = load_model('C:/Users/LENOVO/OneDrive - Lunars Company/Desktop/dan4/DEMOs/model_LC.h5')

def predict_lung_cancer(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = img.reshape(1, 224, 224, 3)

    prediction = model.predict(img)
    if prediction < 0.5:
        return "Không phát hiện ung thư phổi."
    else:
        return "Phát hiện ung thư phổi."

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((450, 450), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(root, image=img)
        panel.image = img
        panel.grid(row=2, column=0, columnspan=2)
        result = predict_lung_cancer(file_path)
        result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Lung Cancer Detection")

# Add buttons and labels
upload_btn = tk.Button(root, text="Nhập vào hình ảnh", command=upload_image)
upload_btn.grid(row=0, column=0, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=0, column=1, padx=10, pady=10)

# Add cover image
cover_img = Image.open('C:/Users/LENOVO/OneDrive - Lunars Company/Desktop/dan4/DEMOs/wallape.jpg')  # Đường dẫn tới ảnh bìa của bạn
cover_img = cover_img.resize((450, 450), Image.LANCZOS)
cover_img = ImageTk.PhotoImage(cover_img)
panel = tk.Label(root, image=cover_img)
panel.image = cover_img
panel.grid(row=2, column=0, columnspan=2)


# Start the GUI loop
root.mainloop()