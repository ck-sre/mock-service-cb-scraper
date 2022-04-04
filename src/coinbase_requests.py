from flask import Flask
from flask import jsonify
from flask import request
import requests
from requests.exceptions import HTTPError
from healthcheck import HealthCheck

from prometheus_client import generate_latest
from prometheus_flask_exporter import PrometheusMetrics

import logging

import os

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


# Sample response
# {"msg":{"base":"BTC","currency":"USD","amount":"47358.18"}}

app = Flask(__name__)

# Metrics vars
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Coinbase scraper info', version='1.0.0')

# App specific vars
spot_svc_url = os.getenv("SPOT_SVC_URL", "https://api.coinbase.com/v2/prices/spot?currency=")
accepted_currencies = os.getenv("ACCEPTED_CURRENCIES", ["EUR", "GBP", "USD","JPY"])

# Healthcheck endpoint
health = HealthCheck()
app.add_url_rule('/health', 'healthcheck', view_func=lambda: health.run())

# Default root path
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello'})

# Serve the spot request, but also collect metrics
@app.route('/<string:currency>', methods=['GET'])
@metrics.gauge('in_progress', 'Long running requests in progress')
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
def get_spot_price(currency):
    if not check_sanity(currency):
        LOGGER.error("Failure, {} is not a valid type of currency".format(currency))
        return jsonify({"status": False, "msg": "Not a valid type of currency"})
    try:
        btc_spot_response = requests.get(spot_svc_url + currency)
        btc_spot_response.raise_for_status()
    except HTTPError as http_err:
        LOGGER.error("HTTP error occurred while connecting", http_err)
        return jsonify({"status": False, "msg": http_err})
    except Exception as err:
        LOGGER.error("Other error occurred", err)
        return jsonify({"status": False, "msg": err})
    else:
        LOGGER.info("Success retrieving spot prices!")
        return jsonify({"status": True, "msg": btc_spot_response.json()})

# Serve metrics
@app.route('/metrics/')
@metrics.do_not_track()
def metrics():
    return generate_latest()

# Check sanity of args
def check_sanity(arg):
    if arg in accepted_currencies:
        return True

# For the lambda function deployed
def lambda_handler(event, context):
    if event:
        try:
            app.run(host='0.0.0.0',port=5001, debug=True)
        except TypeError as te:
            LOGGER.error("The response was not of string type", te)
    
if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0',port=os.getenv('APP_PORT', 5001), debug=True)
    except TypeError as te:
        LOGGER.error("The response was not of string type", te)
