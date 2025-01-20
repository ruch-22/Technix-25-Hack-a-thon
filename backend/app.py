from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Home page

@app.route('/single_resume')
def single_resume():
    return render_template('single_resume.html')  # Page for analyzing a single resume

@app.route('/multiple_resumes')
def multiple_resumes():
    return render_template('multiple_resumes.html')  # Page for analyzing multiple resumes

if __name__ == '__main__':
    app.run(debug=True)
