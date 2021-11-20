from flask import Flask, request
import json

app = Flask(__name__, template_folder="template")


@app.route('/get_4g_season', methods=['GET', 'POST'])
def predict():

    f = open('../data_normalized.csv',)
    data = json.load(f)
    return data


if __name__ == '__main__':
    app.run(port=3000, debug=True)
