from flask import Flask, render_template, request

# Create the Flask application
app = Flask(__name__)

# ------------------------
# Home Route (GET Method)
# ------------------------
@app.route("/", methods=["GET"])
def home():
    """
    GET method:
    - When the user visits the root URL ("/"), Flask calls this function.
    - It simply renders the HTML form from index.html.
    """
    return render_template("index.html")


# ------------------------
# Form Submission Route (POST Method)
# ------------------------
@app.route("/submit", methods=["POST"])
def submit():
    """
    POST method:
    - Triggered when the form in index.html is submitted.
    - Retrieves form data using request.form and passes it to result.html.
    """
    name = request.form.get("name")   # Retrieve 'name' field from the form
    email = request.form.get("email") # Retrieve 'email' field from the form

    # Pass the data to the result page
    return render_template("result.html", name=name, email=email)


if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
