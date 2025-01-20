// main.js for handling frontend logic like form validation, submitting requests, etc.

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
