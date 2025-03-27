from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import os

app = Flask(__name__)

# Ensure the upload folder exists
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")  # Ensure this matches the file name

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return "No file uploaded", 400
    
    file = request.files["image"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return render_template("index.html", filename=file.filename)

@app.route("/edit", methods=["POST"])
def edit():
    filename = request.form["filename"]
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    image = cv2.imread(filepath)
    
    action = request.form["action"]
    
    if action == "grayscale":
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif action == "blur":
        image = cv2.GaussianBlur(image, (15, 15), 0)
    elif action == "sharpen":
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        image = cv2.filter2D(image, -1, kernel)
    elif action == "sepia":
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        image = cv2.transform(image, sepia_filter)
        image = np.clip(image, 0, 255)
    elif action == "brightness":
        beta = int(request.form["value"])  
        image = cv2.convertScaleAbs(image, beta=beta)
    elif action == "contrast":
        alpha = float(request.form["value"])  
        image = cv2.convertScaleAbs(image, alpha=alpha)
    
    edited_filepath = os.path.join(UPLOAD_FOLDER, "edited_" + filename)
    cv2.imwrite(edited_filepath, image)
    
    return render_template("index.html", filename=filename, edited_filename="edited_" + filename)

@app.route("/download/<filename>")
def download(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
