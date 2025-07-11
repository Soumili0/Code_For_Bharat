import random

def generate_nudges(actions, weather, aqi=None):
    """
    Generate eco-friendly nudges based on user actions, weather, and air quality
    
    Args:
        actions (dict): User responses to questions (keys: bath, laundry, etc.)
        weather (dict): Weather data with temp, description, etc.
        aqi (int, optional): Air Quality Index value
    
    Returns:
        list: Personalized eco-tips
    """
    tips = []
    
    # Default values if data is missing
    temp = weather.get("temp", 25)
    desc = weather.get("description", "").lower()
    humidity = weather.get("humidity", 50)
    
    # Ensure actions is a dictionary
    if not isinstance(actions, dict):
        return ["Please answer all questions to get personalized tips"]
    
    # ---- Specific Nudge Conditions ----
    
    # Bathing habit nudges
    if actions.get("bath") == "yes":
        if temp > 30:
            tips.append("It's hot — understandable! But consider a quick shower (5 mins max) to save 50+ liters of water.")
        else:
            tips.append("Try a bucket bath today (uses ~15L) instead of shower (uses ~75L).")
    
    # Laundry nudges
    if actions.get("laundry") == "yes":
        if "clear" in desc or "sun" in desc:
            tips.append("Great drying weather! Sun-dry clothes instead of using a dryer (saves 3kg CO2 per load).")
        else:
            tips.append("Air-dry clothes indoors - still better than energy-hungry dryers.")
    
    # Transportation nudges
    if actions.get("drive") == "yes":
        if aqi and aqi > 150:
            tips.append(f"AQI is {get_aqi_level(aqi)} — Try public transport or cycling to reduce pollution.")
        else:
            tips.append("Consider carpooling or public transport next time (saves money & emissions).")
    
    # AC usage nudges
    if actions.get("ac") == "yes":
        if temp < 25:
            tips.append("It's already cool ({temp}°C) — try opening windows instead of AC.")
        else:
            tips.append(f"Set AC to 26°C (ideal balance) — each degree lower increases energy use by 6%.")
    
    # Heavy devices nudges
    if actions.get("devices") == "yes":
        tips.append("Run heavy appliances (washer/iron) during off-peak hours (before 5pm or after 9pm).")
    
    # Diet-related nudges
    if actions.get("meat") == "yes":
        tips.append("Meat production uses 10x more water than plants. Try a veg meal tomorrow!")
    
    if actions.get("packaged") == "yes":
        tips.append("Prefer fresh/local food over packaged — saves plastic and preservatives.")
    
    # Recycling nudges
    if actions.get("recycle") == "yes":
        tips.append("♻️ Great job recycling! One aluminum can saves enough energy to power a TV for 3 hours.")
    else:
        tips.append("Start small — recycle just one item today (bottle/can/paper).")
    
    # Shopping nudges
    if actions.get("shopping") == "yes":
        tips.append("Bring reusable bags next time — plastic bags take 500+ years to decompose.")
    
    # Outdoor activity nudges
    if actions.get("outdoors") == "yes":
        if aqi and aqi > 150:
            tips.append(f"⚠️ AQI {aqi} is unhealthy — limit outdoor exercise today.")
        else:
            tips.append("Spending time in nature reduces stress and connects you to the environment.")
    
    # Shipping nudges
    if actions.get("shipping") == "yes":
        tips.append("Combine online orders — fewer deliveries mean less packaging and emissions.")
    
    # WFH nudges
    if actions.get("wfh") == "yes":
        tips.append("WFH saves commute emissions! But remember to turn off devices when not in use.")
    
    # ---- Weather-based General Tips ----
    if temp > 35:
        tips.append("🔥 Heat alert! Close curtains during day, open windows at night for natural cooling.")
    elif temp < 15:
        tips.append("❄️ Chilly? Layer up with warm clothes before turning on heaters.")
    
    if humidity > 80:
        tips.append("Humidity high — use exhaust fans to prevent mold (healthier than dehumidifiers).")
    
    # ---- Special Combination Tips ----
    if actions.get("ac") == "yes" and actions.get("meat") == "yes":
        tips.append("Meat + AC = high footprint. Balance with meat-free days and natural cooling.")
    
    if actions.get("drive") == "yes" and actions.get("shopping") == "yes":
        tips.append("Combine shopping trips — one big trip emits less than multiple small ones.")
    
    # ---- Score-based Feedback ----
    green_actions = sum(1 for a in actions.values() if a == "no")
    if green_actions >= 8:
        tips.append(f"🌿 Amazing! {green_actions}/12 eco-actions today. You're a sustainability champion!")
    elif green_actions <= 3:
        tips.append("Every small change helps! Try implementing one tip today.")
    
    # ---- Random Eco Fact ----
    facts = [
        "The average shower uses 12L per minute — reducing by 2 mins saves 24L!",
        "Food waste generates 8% of global emissions — plan meals carefully.",
        "A laptop uses 85% less energy than a desktop computer.",
        "LED bulbs use 75% less energy and last 25x longer than incandescent.",
        "One tree absorbs 10kg of CO2 per year — plant one if you can!"
    ]
    tips.append("💡 Eco Fact: " + random.choice(facts))
    
    return tips

def get_aqi_level(aqi):
    """Convert AQI number to descriptive level"""
    if aqi <= 50: return "Good"
    elif aqi <= 100: return "Moderate"
    elif aqi <= 150: return "Unhealthy for Sensitive Groups"
    elif aqi <= 200: return "Unhealthy"
    elif aqi <= 300: return "Very Unhealthy"
    else: return "Hazardous"