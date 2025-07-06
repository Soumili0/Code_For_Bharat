from flask import Flask, render_template, request, redirect, flash
from nudges_engine import generate_nudges
from utils import get_weather_data, get_aqi_data
import logging

app = Flask(__name__)
app.secret_key = "econudge_secret_2025"  # Needed for flash messages

# Enable logging to debug
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/get_nudges", methods=["POST"])
def nudges():
    try:
        form = request.form
        location = form["location"].strip()

        if not location:
            flash("Please enter a valid location.")
            return redirect("/")

        # Get all user inputs
        user_actions = {
            "bath": form.get("bath", "no"),
            "laundry": form.get("laundry", "no"),
            "drive": form.get("drive", "no"),
            "ac": form.get("ac", "no"),
            "meat": form.get("meat", "no"),
            "devices": form.get("devices", "no"),
            "packaged": form.get("packaged", "no"),
            "recycle": form.get("recycle", "no"),
            "shopping": form.get("shopping", "no"),
            "outdoors": form.get("outdoors", "no"),
            "shipping": form.get("shipping", "no"),
            "wfh": form.get("wfh", "no"),
        }

        logging.info(f"User inputs: {user_actions} | Location: {location}")

        # Fetch weather and AQI data
        weather = get_weather_data(location)
        aqi = get_aqi_data(location)

        if not weather:
            flash("Couldn't fetch weather data. Please check your city/PIN code.")
            return redirect("/")

        # Generate eco-nudges
        nudges = generate_nudges(user_actions, weather, aqi)

        return render_template("nudges.html", nudges=nudges, location=location, weather=weather, aqi=aqi)

    except Exception as e:
        logging.error(f"Error in /get_nudges: {e}")
        flash("Oops! Something went wrong. Try again.")
        return redirect("/")


# Optional: Health check endpoint for deployment
@app.route("/ping")
def ping():
    return "EcoNudge is alive 🌱", 200


if __name__ == "__main__":
    app.run(debug=True)
