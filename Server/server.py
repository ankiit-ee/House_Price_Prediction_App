from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/location')
def get_location():
    response = jsonify({
        'locations' : util.get_location()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    BHK = int(request.form['BHK'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estiimated_price': util.estimate_price(location, total_sqft, bath, BHK)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Flask server for Home Price Prediction")
    app.run()
