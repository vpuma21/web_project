from flask import Flask
import routes

app = Flask(__name__)

# register routes
routes.register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)