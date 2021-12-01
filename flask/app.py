from flask import Flask, json, request, jsonify
from flask.wrappers import Request
import requests
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

POSTMAN_MOCK_SERVER = "https://99432624-78a2-4637-9d7d-95373d6c0c3a.mock.pstmn.io"

# return false if zip is None or invalid length
def validate_zip(zip):
    # if zip does not exists
    if(not zip):
         return False

    return True if len(zip) == 5 else False   

# return false if add is None
# This would need a third party API to validate the address past this
# > House Canary possibly handles this and returns an error if the address
# is invalid
def validate_address(add):
    if not add:
        return False
    return True

# returns object from postman mock server / house canary
def prop_details():
    address = request.args.get('add')
    zip = request.args.get('zip')

    # if not parameters are added
    if not validate_address(address) and not validate_zip(zip):
        return 'No Parameters', 403

    # Validate zipcode
    if not validate_zip(zip):
        return 'Invalid Zip Code', 403
    
    # Validate address
    if not validate_address(address):
        return 'Invalid Address', 403

    # use Postman mock server to get property value
    house_canary = requests.get("{url}/property/details?{address}&{zip}".format(url = POSTMAN_MOCK_SERVER,address = address, zip = zip))
    house_canary_json = house_canary.json()["property/details"]["result"]
    
    return house_canary_json, 200


# return object of the sewer property
# Expects => add=123+Main+st&zip=12345
@app.route('/hasSewer', methods=['GET'])
@cross_origin()
def has_sewer():
    property_details, code = prop_details()
    if code == 403:
        return jsonify({"error": property_details})

    return jsonify({"sewer": property_details["property"]["sewer"]})

   
# return json object of the property details
# Expects => add=123+Main+st&zip=12345
@app.route('/propertyDetails', methods=['GET'])
@cross_origin()
def get_prop_details():
    details, code = prop_details()
    if code == 403:
        return jsonify({"error": details})

    return jsonify(details)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)