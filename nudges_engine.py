import random

def generate_nudges(actions, weather, aqi):
    tips = []

    temp = weather.get("temp", 25)
    desc = weather.get("description", "").lower()

    if actions["bath"] == "yes":
        if temp > 30:
            tips.append("It’s hot — understandable! But consider a quick shower to save 50L water.")
        else:
            tips.append("Try a 5-minute bucket bath to conserve water.")

    if actions["laundry"] == "yes":
        if "clear" in desc or "sun" in desc:
            tips.append("Perfect day to sun-dry clothes instead of using a dryer!")
        else:
            tips.append("Air-drying indoors still saves energy over electric dryers.")

    if actions["drive"] == "yes":
        if aqi and aqi > 150:
            tips.append("AQI is poor — Avoid driving today if you can.")
        else:
            tips.append("Try using public transport, walking, or cycling — double win!")

    if actions["ac"] == "yes":
        if temp < 25:
            tips.append("It's already cool 🌬 — you may not need the AC.")
        else:
            tips.append("Set AC to 26°C or use fan for energy efficiency.")

    if actions["devices"] == "yes":
        tips.append("Avoid using heavy appliances (iron/heater) during peak hours to reduce energy strain.")

    if actions["meat"] == "yes":
        tips.append("Going meatless for a day saves 1000+ liters of water. Try a veg meal today!")

    if actions["packaged"] == "yes":
        tips.append("Packaged food = more plastic. Try fresh/local alternatives today.")

    if actions["recycle"] == "yes":
        tips.append("Great job recycling! You're helping the planet breathe.")
    else:
        tips.append("Haven’t recycled today? Even 1 bottle makes a difference.")

    if actions["shopping"] == "yes":
        tips.append("Bring your own cloth bag to say no to single-use plastics.")

    if actions["outdoors"] == "yes":
        if aqi and aqi > 150:
            tips.append("AQI is high 🌫 — Avoid outdoor activities and protect your lungs.")
        else:
            tips.append("A nature walk is good for your mind and planet.")

    if actions["shipping"] == "yes":
        tips.append("Group online orders to reduce packaging and delivery trips.")

    if actions["wfh"] == "yes":
        tips.append("Nice! Working from home saves commute emissions & energy.")

    if temp > 35:
        tips.append("It's very hot! Drink water, stay cool, and reduce outdoor energy use.")
    elif temp < 15:
        tips.append("It’s chilly — consider layering clothes instead of turning on heaters.")

    if actions["ac"] == "yes" and actions["meat"] == "yes":
        tips.append("High AC + Meat diet = high carbon footprint. Try to offset by recycling or going plant-based.")

    green_score = sum(1 for value in actions.values() if value == "no")
    if green_score >= 9:
        tips.append("You're doing amazing! 9+ green choices today. The planet thanks you!")

    facts = [
        "Did you know? One recycled can saves enough energy to run a TV for 3 hours.",
        "Every meatless day saves enough water to fill 20 bathtubs.",
        "Plastic takes 450+ years to decompose. Avoid it when possible.",
        "Air-drying clothes saves ~1,000 lbs of CO₂ per year!"
    ]
    tips.append("Eco Fact: " + random.choice(facts))

    if not tips:
        tips.append("You're already making eco-friendly choices today!")

    return tips

