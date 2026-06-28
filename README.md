# Meal Planner Backend

This Flask API stores a small meal plan and lets the frontend read and add meals.

## Routes

- `GET /` returns a welcome message.
- `GET /api/meals` returns all planned meals.
- `POST /api/meals` adds a new meal.

## How to Run

Create and activate a virtual environment, then install the requirements:

py -m venv .venv
source .venv/Scripts/activate
py -m pip install -r requirements.txt