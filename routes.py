def register_routes(app):

    @app.route("/")
    def home(): # this is the home screen
        return "Weather Report Website"
    
    @app.route("/about") # an about section
    def about():
        return """<h2>About this website</h2>
        <p>This website will collect weather data from using the Open-Meteo API</p>
        <p>It will allow the user to create,read,update,and delete weather observations through a Flask Server</p>
        """

    # Create section, in where u create an observation
    @app.route("/ingest", methods=["POST"])
    def ingest():
        return "POST: create observation"

    # This is where you get all of your observations
    @app.route("/observations", methods=["GET"])
    def list_observations():
        return "GET: all observations"

    # This is where you want to read one
    @app.route("/observations/<int:id>", methods=["GET"])
    def get_observation(id):
        return f"GET observation {id}"

    # This is where you update an observation
    @app.route("/observations/<int:id>", methods=["PUT"])
    def update_observation(id):
        return f"PUT update observation {id}"

    # This is where you delete an observation
    @app.route("/observations/<int:id>", methods=["DELETE"])
    def delete_observation(id):
        return f"DELETE observation {id}"