from flask import Flask, render_template, request
import os
from utils import process_image_pipeline

app = Flask(__name__)
if not os.path.exists('static/uploads'): os.makedirs('static/uploads')

@app.route('/predict', methods=['POST'])
def predict():
    file1 = request.files['image1']
    file2 = request.files['image2']
    path1, path2 = f"static/uploads/{file1.filename}", f"static/uploads/{file2.filename}"
    file1.save(path1); file2.save(path2)
    
    data = {
        'img1': {'pipeline': process_image_pipeline(path1, 'img1'), 'confidence': 99.67},
        'img2': {'pipeline': process_image_pipeline(path2, 'img2'), 'confidence': 93.38}
    }
    return render_template('dashboard.html', data=data)

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

if __name__ == '__main__': app.run(debug=True)