# 🛰️ GeoTIFF Viewer using GDAL

An interactive desktop application built with **Python, GDAL, and Tkinter** to visualize GeoTIFF satellite images with real-time coordinate tracking and user interaction.

---

## 📌 Features

* 📂 Load and display GeoTIFF satellite images
* 🖱️ Real-time mouse tracking

  * Pixel coordinates (X, Y)
  * Geographic coordinates (Latitude, Longitude)
* 📍 Mark specific locations using input coordinates
* 🔍 Zoom functionality using mouse wheel *(Bonus)*
* ✋ Pan functionality using mouse drag *(Bonus)*

---

## 🛠️ Technologies Used

* Python
* GDAL (Geospatial Data Abstraction Library)
* Tkinter (GUI Framework)

---

## 📁 Project Structure

```
Assignment3/
│── data/                # Sample GeoTIFF files
│── src/                 # Source code
│── requirements.txt     # Dependencies
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/geotiff-gdal-viewer.git
cd geotiff-gdal-viewer
```

### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main application:

```
python src/main.py
```

---

## 🧠 How It Works

* GDAL reads GeoTIFF metadata and raster data
* Pixel coordinates are mapped to geographic coordinates (lat/lon)
* Tkinter handles GUI rendering and user interaction
* Mouse events dynamically update displayed coordinates

---

## 📸 Functional Overview

* Move mouse → See X, Y and Lat, Lon update in real-time
* Enter Lat/Lon → Click "Mark" → Cross appears on image
* Scroll → Zoom in/out
* Drag → Pan image

---

## 🚀 Future Improvements

* Add multi-layer support
* Export marked coordinates
* Integrate map overlays (OpenStreetMap, etc.)
* Improve UI/UX design

---

## 👩‍💻 Author

**Nimra Jabbar**
