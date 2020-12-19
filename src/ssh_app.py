from flask import Flask, jsonify, request, make_response
from api_handler import handler_get_interfaces, handler_get_interface
import json
app = Flask(__name__)


@app.route("/get_all_interfaces", methods=["GET"], strict_slashes=False)
def get_interfaces():
    data = handler_get_interfaces()
    return json.dumps(data), 200


@app.route("/get_interface/<iname>/<inum>", methods=["GET"], strict_slashes=False)
def get_single_interface(iname, inum=None):
    if iname == "":
        return make_response(jsonify("interface name required"), 404)
    iface = "{}/{}".format(iname, inum) if inum else iname
    data = handler_get_interface(iface)
    return json.dumps(data), 200


if __name__ == "__main__":
    app.run(debug=True)
