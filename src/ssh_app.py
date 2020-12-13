from flask import Flask, jsonify, request, make_response
from api_handler import handler_get_interfaces, handler_get_interface
app = Flask(__name__)


@app.route("/get_all_interfaces", methods=["GET"], strict_slashes=False)
def get_interfaces():
    data = handler_get_interfaces()
    return jsonify(data)


@app.route("/get_interface", methods=["GET"], strict_slashes=False)
def get_single_interface():
    iname = request.args.get('interface', "")
    if iname == "":
        return make_response(jsonify("interface name required"), 404)
    data = handler_get_interface(iname)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
