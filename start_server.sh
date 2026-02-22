#!/bin/bash
# Install dependencies if missing (simple check)
if ! pip show gunicorn > /dev/null; then
    echo "Installing gunicorn..."
    pip install gunicorn
fi

# Run Gunicorn
# -w 4: Use 4 worker processes (handle multiple users at once)
# -b 0.0.0.0:8000: Listen on all network interfaces on port 8000
# python_course_tester:app : The file is python_course_tester.py, the Flask variable is 'app'
echo "Starting Python Course Website on port 8000..."
gunicorn -w 4 -b 0.0.0.0:8000 python_course_tester:app
