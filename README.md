# Modern Image Editor

A **web-based image editor** built with **Flask** and **OpenCV** that allows users to upload images and apply various filters such as grayscale, blur, sharpen, sepia, brightness, and contrast adjustments.

---

## Features

* Upload an image from your device.
* Apply the following filters to your image:

  * Grayscale
  * Blur
  * Sharpen
  * Sepia
  * Brightness adjustment
  * Contrast adjustment
* Preview both the **original** and **edited** images side by side.
* Download the edited image to your device.
* Responsive design for desktop and mobile devices.

---

## Tech Stack

* **Backend:** Python, Flask
* **Image Processing:** OpenCV, NumPy
* **Frontend:** HTML, CSS, JavaScript

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/modern-image-editor.git
   cd modern-image-editor
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```
   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask application:**

   ```bash
   python app.py
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## Usage

1. Upload an image using the **file input**.
2. Apply filters by clicking the respective buttons.
3. Adjust **brightness** or **contrast** using the sliders and apply.
4. Preview the **original** and **edited** images.
5. Click **Download Edited Image** to save the image locally.

---

## Folder Structure

```
modern-image-editor/
│
├─ app.py                 # Flask application
├─ requirements.txt       # Python dependencies
├─ templates/
│  └─ index.html          # Main HTML page
├─ static/
│  ├─ styles.css          # CSS styling
│  └─ script.js           # JavaScript for interactivity
└─ uploads/               # Folder for uploaded and edited images
```

---

## Dependencies

* Flask
* OpenCV (`opencv-python`)
* NumPy

Install all dependencies using:

```bash
pip install flask opencv-python numpy
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).

Do you want me to do that?
