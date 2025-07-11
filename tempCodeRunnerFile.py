from flask import Flask, render_template, request, jsonify
from nudges_engine import generate_nudges
from utils import get_weather_data, get_aqi_data

app = Flask(__name__)
app.secret_key = "econudge_secret_2025"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_nudge_step", methods=["POST"])
def get_nudge_step():
    try:
        data = request.get_json()
        location = data.get("location")
        actions = data.get("answers", {})
        
        if not location:
            return jsonify({"nudge": "Please provide a location"}), 400

        weather = get_weather_data(location)
        if not weather:
            return jsonify({"nudge": "Could not fetch weather data for this location"}), 400

        aqi = get_aqi_data(location)
        nudges = generate_nudges(actions, weather, aqi)
        
        if not nudges:
            return jsonify({"nudge": "You're making great eco-friendly choices!"})
        
        # Return the first nudge (simplified for this example)
        return jsonify({"nudge": nudges[0]})
    
    except Exception as e:
        print(f"Error in get_nudge_step: {str(e)}")
        return jsonify({"nudge": "An error occurred while generating nudges"}), 500

@app.route("/ping")
def ping():
    return "EcoNudge is alive", 200

if __name__ == "__main__":
    app.run(debug=True)