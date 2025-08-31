from flask import Flask
#Create a simple Flask application
app = Flask(__name__)
# Import the Flask class from the flask module
# Create an instance of the Flask application
@app.route("/")
def home():
    return "<h1> Welcome to my first Flask app! </h1>"
@app.route("/about")
def about():
    return "This is the About page."
# __name__ is a special variable that gets the name of the current module
if __name__ == "__main__":
    # Run the Flask application in debug mode (auto-reloads on changes)
    app.run(debug=True)

