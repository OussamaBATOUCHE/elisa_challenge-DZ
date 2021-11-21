from flask import Flask, request
from tensorflow import keras

app = Flask(__name__, template_folder="template")

# Load the model
model = keras.models.load_model("ml/best_model.h5")


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get data
        data = [[float(request.form.get('lon')), float(
            request.form.get('lat')), int(request.form.get('day'))]]
        print("[Data from post] ", data)
        # Make prediction
        print(model.summary())
        pred = model.predict(data)
        result = pred[0][0]
        print(result)
        return result


if __name__ == '__main__':
    app.run(port=3000, debug=True)