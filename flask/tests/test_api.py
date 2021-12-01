# Unit Testing for Sewer API

import requests

def test_has_sewer_valid_address():
    response = requests.get("http://192.168.1.249:105/hasSewer?add=123+Main+st&zip=02911")
    assert response.json()['sewer'] == 'municipal'
    assert response.status_code == 200

def test_has_sewer_invalid_zip():
    response = requests.get("http://192.168.1.249:105/hasSewer?add=123+Main+st&zip=0291")
    assert response.json()['error'] == 'Invalid Zip Code'

def test_has_sewer_invalid_address():
    response = requests.get("http://192.168.1.249:105/hasSewer?zip=02911")
    assert response.json()['error'] == 'Invalid Address'

def test_has_sewer_no_parameters():
    response = requests.get("http://192.168.1.249:105/hasSewer")
    assert response.json()['error'] == 'No Parameters'

def test_prop_details_valid_address():
    response = requests.get("http://192.168.1.249:105/propertyDetails?add=123+Main+st&zip=02911")
    assert response.json()['property']['sewer'] == 'municipal'
    assert response.status_code == 200

def test_prop_details_invalid_zip():
    response = requests.get("http://192.168.1.249:105/propertyDetails?add=123+Main+st&zip=0291")
    assert response.json()['error'] == 'Invalid Zip Code'

def test_prop_details_invalid_address():
    response = requests.get("http://192.168.1.249:105/propertyDetails?zip=02911")
    assert response.json()['error'] == 'Invalid Address'

def test_prop_details_no_parameters():
    response = requests.get("http://192.168.1.249:105/propertyDetails")
    print(response.content)
    assert response.json()['error'] == 'No Parameters'