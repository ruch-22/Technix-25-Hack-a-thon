from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Upload folder for resumes
app.config['UPLOAD_FOLDER'] = './backend/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max file size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_job_requirements', methods=['POST'])
def submit_job_requirements():
    data = request.get_json()
    job_title = data.get('job_title')
    skills = data.get('skills')
    # Process job requirements (save, compare, etc.)
    return jsonify({"message": "Job requirements received", "job_title": job_title, "skills": skills})

if __name__ == '__main__':
    app.run(debug=True)
