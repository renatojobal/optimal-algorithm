import flask
import main

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def apply_algorithm():
    data = flask.request.get_json()
    print("Here is the data")
    print(data["pages_list"])

    # Parse the data
    pages_list = data["pages_list"]
    frames_number = data["frames_number"]

    result_matrix = main.apply_optimal_algorithm(pages_list=pages_list, frames_number=frames_number)

    return {"result_matrix":result_matrix}

app.run()
