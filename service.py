import flask
import main
from utils import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def apply_algorithm():
    """
    Unique entrance for this API
    :return: a result matrix
    """
    data = flask.request.get_json()

    # Parse the data

    pages_list = data["pages_list"]
    frames_number = data["frames_number"]
    default_null = data.get("default_null")

    result_matrix = main.apply_optimal_algorithm(pages_list=pages_list, frames_number=frames_number)
    print("Default null {}".format(default_null))
    matrix_for_response = get_matrix_for_response(result_matrix, default_null=default_null)

    return {"result_matrix": matrix_for_response}


app.run()
