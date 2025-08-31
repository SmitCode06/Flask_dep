# Importing required classes and functions from Flask
# Flask -> to create the application
# request -> to read incoming request data (form, JSON, query params, etc.)
# render_template_string -> to quickly render HTML code inside Python string
from flask import Flask, request, render_template_string

# Creating a Flask application instance
app = Flask(__name__)

# A simple HTML form stored in a Python string
# method="POST" → tells browser to send form data in the HTTP request body, not URL
# <input name="username"> → this will be the key when we access data via request.form["username"]
form_html = """
<form method="POST">
    Enter your name: <input type="text" name="username">
    <input type="submit" value="Submit">
</form>
"""

# Defining a route (URL path) "/"
# methods=["GET", "POST"] → this route accepts both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def home():
    # Checking which HTTP method is used by client
    if request.method == "POST":  # <-- request.method gives "GET" or "POST"
        # request.form is a dictionary-like object containing data sent in the form body
        # "username" is the name attribute from <input>
        username = request.form["username"]

        # Returning a response string back to the client
        return f"Hello, {username}! (Received via POST)"
    
    # If request is GET, show the HTML form
    return render_template_string(form_html)
@app.route("/form")
def form():
    return """
    <form action="/multiply" method="post">
        <input type="number" name="num1" placeholder="Enter number 1" required>
        <input type="number" name="num2" placeholder="Enter number 2" required>
        <button type="submit">Multiply</button>
    </form>
    """

# Route to handle multiplication
@app.route("/multiply", methods=["GET", "POST"])
def multiply_numbers():
    # Safely extract values from the form
    num1 = request.form.get("num1", type=float)
    num2 = request.form.get("num2", type=float)

    if num1 is None or num2 is None:
        return "<p>Error: Please enter valid numbers.</p>"

    result = num1 * num2
    return f"<h1>Result:</h1><p>{num1} × {num2} = {result}</p>"

# Starting the Flask development server in debug mode
# debug=True → auto-restarts server on code changes and shows error logs
if __name__ == "__main__":
    app.run(debug=True)
