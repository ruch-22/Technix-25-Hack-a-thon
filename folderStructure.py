import os

# Define the folder structure
folders = [
    "resume",
    "resume/backend",
    "resume/backend/static",
    "resume/backend/static/css",
    "resume/backend/static/js",
    "resume/backend/templates",
    "resume/backend/uploads",
    "resume/backend/models",
    "resume/frontend",
    "resume/frontend/assets",
    "resume/frontend/css",
    "resume/frontend/js",
]

# Files to create
files = {
    "resume/backend/app.py": '''from flask import Flask, render_template, request, jsonify
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
''',
    "resume/backend/static/css/style.css": '''body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    margin: 0;
    padding: 0;
}

.container {
    width: 80%;
    margin: 0 auto;
    text-align: center;
    padding: 20px;
}

h1 {
    color: #333;
}

.options {
    margin-top: 20px;
}

.options button {
    padding: 12px 20px;
    font-size: 18px;
    margin: 10px;
    cursor: pointer;
    border: none;
    background-color: #4CAF50;
    color: white;
    border-radius: 5px;
}

.options button:hover {
    background-color: #45a049;
}

.job-details-form {
    margin-top: 30px;
    text-align: left;
}

.job-details-form label {
    font-size: 16px;
    margin-top: 10px;
}

.job-details-form input,
.job-details-form textarea {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 15px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

.job-details-form button {
    padding: 10px 15px;
    font-size: 16px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.job-details-form button:hover {
    background-color: #0056b3;
}
''',
    "resume/backend/static/js/main.js": '''// main.js for handling frontend logic like form validation, submitting requests, etc.

document.getElementById('job-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting normally

    const jobTitle = document.getElementById('job-title').value;
    const skills = document.getElementById('skills').value;

    if (jobTitle && skills) {
        // Send the job requirements to the backend
        fetch('/submit_job_requirements', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ job_title: jobTitle, skills: skills })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Job requirements submitted:', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
''',
    "resume/backend/templates/index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume Analyzer</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Resume Analyzer</h1>
        <p>Welcome! Choose an option below to upload resumes for analysis.</p>

        <div class="options">
            <button onclick="window.location.href='/upload_single'">Analyze Single Resume</button>
            <button onclick="window.location.href='/upload_multiple'">Analyze Multiple Resumes</button>
        </div>

        <div class="job-details-form">
            <h3>Enter Job Requirements</h3>
            <form id="job-form" action="/submit_job_requirements" method="POST">
                <label for="job-title">Job Title:</label>
                <input type="text" id="job-title" name="job_title" required>
                
                <label for="skills">Required Skills:</label>
                <textarea id="skills" name="skills" rows="4" required></textarea>

                <button type="submit">Submit Job Requirements</button>
            </form>
        </div>
    </div>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
''',
    "resume/frontend/index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume Analyzer</title>
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Resume Analyzer</h1>
        <p>Welcome! Choose an option below to upload resumes for analysis.</p>

        <div class="options">
            <button onclick="window.location.href='/upload_single'">Analyze Single Resume</button>
            <button onclick="window.location.href='/upload_multiple'">Analyze Multiple Resumes</button>
        </div>

        <div class="job-details-form">
            <h3>Enter Job Requirements</h3>
            <form id="job-form" action="/submit_job_requirements" method="POST">
                <label for="job-title">Job Title:</label>
                <input type="text" id="job-title" name="job_title" required>
                
                <label for="skills">Required Skills:</label>
                <textarea id="skills" name="skills" rows="4" required></textarea>

                <button type="submit">Submit Job Requirements</button>
            </form>
        </div>
    </div>

    <script src="static/js/main.js"></script>
</body>
</html>
''',
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as file:
        file.write(content)

print("Project structure created successfully.")
