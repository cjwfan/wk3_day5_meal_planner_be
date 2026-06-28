from flask import Flask, request
from flask_cors import CORS
from meals import planned_meals

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return {"message": "Meal planner API is running."}

@app.get("/api/meals")
def get_meals():
    return planned_meals

@app.post("/api/meals")
def create_meal():
    data = request.get_json()
    if not data:
        return{"error": "Request body must be JSON"}, 400
    if "day" not in data or "meal" not in data:
        return {"error": "Day and meal are required"}, 400
    
    new_meal = {
        "id": len(planned_meals) + 1,
        "day": data["day"],
        "meal": data["meal"]
    }

    planned_meals.append(new_meal)
    return new_meal, 201