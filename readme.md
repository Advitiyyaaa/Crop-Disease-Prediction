# 🌿 Crop Disease Prediction System

An AI-powered web application that detects crop diseases from leaf images using Deep Learning. This project helps farmers and users identify plant diseases quickly and take preventive actions.

---

## 🚀 Features

* 📸 Upload leaf images for disease detection
* 🧠 Deep Learning model (TensorFlow/Keras)
* 🌐 User-friendly web interface using Streamlit
* ⚡ Real-time prediction
* 📊 Model training and evaluation included

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* NumPy, Pandas
* Matplotlib / Seaborn
* Streamlit

---

## 📂 Project Structure

```
Crop-Disease-Prediction/
│── train/                      # Training dataset (not included)
│── valid/                      # Validation dataset (not included)
│── test/                       # Sample test images
│── main.py                     # Streamlit web app
│── train_crops_disease.ipynb   # Model training notebook
│── Test_plant_disease.ipynb    # Testing notebook
│── trained_plant_disease_model.keras  # Saved model (optional)
│── training_hist.json          # Training history
│── images/                     # UI images (logo, homepage)
│── README.md
│── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/advitiyyaaa/Crop-Disease-Prediction.git
cd Crop-Disease-Prediction
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the application

```
streamlit run main.py
```

---

## 📊 Model Details

* Model Type: Convolutional Neural Network (CNN)
* Framework: TensorFlow / Keras
* Task: Multi-class image classification
* Input: Leaf images
* Output: Predicted disease class

---

## 📁 Dataset

* Dataset is **not included** due to size constraints
* You can download it from Kaggle (PlantVillage Dataset)

👉 After downloading, place it like:

```
train/
valid/
```


## 💡 Future Improvements

* Add mobile app support
* Improve model accuracy with transfer learning
* Deploy on cloud (AWS / GCP / Azure)
* Add treatment suggestions for diseases

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

## 📜 License

This project is for educational purposes.

---

## 👨‍💻 Author

Advitiya Gupta
AI/ML Enthusiast | Aspiring Software Developer
