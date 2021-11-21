from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__, template_folder="template")

CORS(app)

@app.route('/get_5g_days', methods=['GET'], )
def get_5g_days():

    with open('./20k_5g_data_normalized.csv', 'r') as file:
        return file.read(), 200, {'Content-Type': 'text/csv; charset=utf-8'}

@app.route('/get_4g_days', methods=['GET'], )
def get_4g_days():

    with open('./20k_4g_data_normalized.csv', 'r') as file:
        return file.read(), 200, {'Content-Type': 'text/csv; charset=utf-8'}

@app.route('/get_5g_season', methods=['GET'], )
def get_5g_season():

    with open('./20k_5g_data_season_normalized.csv', 'r') as file:
        return file.read(), 200, {'Content-Type': 'text/csv; charset=utf-8'}

if __name__ == '__main__':
    app.run(port=3000, debug=True)
