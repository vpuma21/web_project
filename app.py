from flask import Flask
from routes import routes

app = Flask(__name__)

# register all CRUD routes
app.register_blueprint(routes)

@app.route("/")
def home():
    return "<h1>Weather API server running</h1>"

if __name__ == "__main__":
    app.run(debug=True)