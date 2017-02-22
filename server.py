from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def get_homepage():
    """The homepage"""

    return render_template('index.html')


@app.route('/get_list', methods=['POST'])
def get_list():
    """Gets a list of objects from send_data()"""

    data = request.get_json()
    modified_data = {}

    for i, item in enumerate(data['data']):
        modified_data[i] = item

    return jsonify(modified_data)


if __name__ == "__main__":

        app.run(host="0.0.0.0", debug=True)
