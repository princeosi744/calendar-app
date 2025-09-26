from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is the Calendar App running in Docker!"

@app.route("/calendar")
def calendar():
    # Example: return current month calendar days
    today = datetime.date.today()
    month_days = [str(today.replace(day=d)) for d in range(1, 29)]
    return jsonify({
        "month": today.strftime("%B"),
        "year": today.year,
        "days": month_days
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

