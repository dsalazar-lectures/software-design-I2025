from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def index():
  # Render the 'index.html' template
  return render_template('index.html')

# Run the app in debug mode
if __name__ == '__main__':
  app.run(debug=True)
