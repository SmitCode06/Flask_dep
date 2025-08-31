# Import Flask for web app creation, request to handle parameters from the URL
from flask import Flask, request
# Import datetime to show current server time
from datetime import datetime

# Create the Flask application instance
app = Flask(__name__)

# Home route - displays instructions
@app.route("/")
def home():
    # Returning HTML with heading and paragraph tags
    return """
    <h1>Welcome to the Calculator App</h1>  <!-- h1: Main heading -->
    <p>Use <code>/add?num1=10 & num2=20</code> to add two numbers.</p> 
    <!-- p: paragraph, code: inline code formatting -->
    """

# About route - displays info about the app
@app.route("/about")
def about():
    return "This is the About page of the Calculator App."

# Just a path parameter
@app.route("/course/<course_name>")
def course(course_name):
    return f"Welcome to the {course_name} course!"

# Path with subpath (like folder style URL)
@app.route("/course/<course_name>/topic/<topic_name>")
def course_topic(course_name, topic_name):
    return f"Course: {course_name} | Topic: {topic_name}"



# Route to add numbers using GET method
@app.route("/add", methods=["GET"])
def add_numbers():
    # Retrieve 'num1' from the query parameters; default is 0 if not provided; convert to float
    num1 = request.args.get("num1", default=0, type=float)
    # Retrieve 'num2' from the query parameters; default is 0 if not provided; convert to float
    num2 = request.args.get("num2", default=0, type=float)


    # Perform the addition
    result = num1 + num2

    # Get current server time in "YYYY-MM-DD HH:MM:SS" format
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Return the result as HTML
    return f"""
    <h1>Calculation Result</h1> <!-- h1: heading for result section -->
    <p>{num1} + {num2} = {result}</p> <!-- p: shows the addition calculation -->
    <p>Calculated at: {current_time}</p> <!-- p: shows the current server time -->
    """

# Start the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
