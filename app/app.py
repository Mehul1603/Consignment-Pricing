import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from model.model import predict_data
from model.model import __version__ as model_version

app = Flask(__name__)

@app.route("/")
def predict():
    return render_template("index.html")

@app.route("/", methods = ["GET", "POST"])
def getvalue():
    po_so = bool(request.form['po_so'])
    asn_dn = bool(request.form['asn_dn'])
    country = int(request.form['country'])
    fulfill_via = bool(request.form['fulfill_via'])
    vendor_inco_term = int(request.form['vendor_inco_term'])
    sub_classification = int(request.form['sub_classification'])
    unit_of_measure = int(request.form['unit_of_measure_(per_pack)'])
    line_item_quantity = int(request.form['line_item_quantity'])
    pack_price = float(request.form['pack_price'])
    unit_price = float(request.form['unit_price'])
    first_line_designation = bool(request.form['first_line_designation'])
    freight_cost = float(request.form['freight_cost_(usd)'])
    shipment_mode = int(request.form['shipment_mode'])
    line_item_insurance = float(request.form['line_item_insurance_(usd)'])
    days_to_process = int(request.form['days_to_process'])
    prediction = predict_data(np.array([po_so, asn_dn, country, fulfill_via, vendor_inco_term, sub_classification, unit_of_measure, line_item_quantity, pack_price, unit_price, first_line_designation, freight_cost, shipment_mode, line_item_insurance, days_to_process]))
    return render_template("index.html", response = prediction)

if __name__ == "__main__":
    app.run(debug=True)