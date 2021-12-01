# HomeTapInterview

## Table of Contents
- [HomeTapInterview](#hometapinterview)
  - [Table of Contents](#table-of-contents)
  - [Approach](#approach)
  - [Stack](#stack)
  - [Setup](#setup)
    - [Frontend](#frontend)
    - [Backend](#backend)
    - [Mock Server](#mock-server)
    - [Running Tests](#running-tests)
  - [Tools Used](#tools-used)
  - [Assumptions](#assumptions)
  - [Task Objectives](#task-objectives)
  - [Guidelines](#guidelines)
  - [Security](#security)
  - [Next Steps](#next-steps)
  - [JSON-Object](#json-object)

## Approach 
1. I wanted to treat this assignment as a real project. This lead me to create a very basic react based frontend that is able to interact with the Flask based backend. I also added some unit tests for the Flask API. 
2. As noted in the guidelines, houseCanary's api is a pay-to-use API which means we will need to mock some data. 

## Stack
- Frontend: React
- Backend: Flask
- Mocking framework: postman mock server

## Setup
### Frontend
- `cd frontend`
- `npm install`
- `npm start`
### Backend
- Python Version: 3.8.0
- Create Virtual env
- `cd flask`
- `python -m venv env` (or use python3 instead of python)
- `source env/bin/activate`, If on Windows (` .\/env/Scripts/activate`)
- Set up Virtual env
- `pip install flask`
- `pip install flask_cors`
- `pip install requests`
- `pip install pytest`
- Start Flask server: `python app.py`
### Mock Server
- Open Postman and create new mock server
- Create a get request with the following parameters:

| Request Method | Request URL | Response Code | Response Body |
| -------  | ------- | ------- | -------  |
| GET     | /property/details | 200 | [JSON OBJECT](#JSON-Object) |

### Running Tests
- Have Flask server and postman mock server running
- In a second terminal run `python`

## Tools Used
- VS code
- Postman

## Assumptions
- user does not need to be authenticated in order to make this API request
___

## Task Objectives
- We have a web app that homeowners interact with to provide us information about their home.
- New feature: The web app should prompt homeowners with an additional question if we believe their home has a septic system.
- We believe that we can get the answer to the septic system question from the third party API described here: https://api-docs.housecanary.com/#property-details.
- We want to assume that over time, we may find other third parties with this info, or this particular third party may change their API, and we want to leave the web app implementation alone. Meaning that you should build an intermediary web service that consumes data from the HouseCanary API described at the link above, and make that information available through a custom API endpoint you design for our web app to use.

## Guidelines
- You should implement the intermediary web service that exposes a custom API for answering the question above, and calls the third party (HouseCanary) API to get the relevant data.
- You do not need to implement any aspect of the web app that has the homeowner-facing interaction.
- Please note that we are a predominantly macOS and Python shop. We would prefer the submission to be created in one of the Python-based web frameworks if you are comfortable with those.
- If you look at this problem statement and conclude that in a real scenario you would build something that has a fundamentally different architecture, it would be interesting to hear about that, and you could talk about the possibility of a different design and rationale when you present your result. But in this case, we want to see you design an API, call an API, and implement an API, so consider those aspects as requirements for what you actually implement.
- The HouseCanary API above has public documentation, but the API itself is restricted to organizations with paid access. We recommend that you mock up API responses in unit tests or via an API mocking tool (e.g. Swaggerhub, Postman Mock Server, Stoplight).
- Give thought to security, scalability, and maintainability. 
Our goal is to get a sense of how you approach problems, and get a sense of what it would be like to work together, not to give you a huge multi-day homework assignment. If some of your ideas for a completed product would turn this into a massive project, you may wish to write those up as suggested “Next Steps”.
- Provide a link to a GitHub repository with your code and a README that explains how to run it.

___

## Security
- Since we are operating under the assumption users do not need to be authenticated, this API will be exposed to anyone that can curl/ GET it. It would be a good idea to add a limiter, to avoid multiple requests to the houseCanary API from the same user costing you money for each request to houseCanary. This leads to my next point of implementing a database in order to avoid calling houseCanary multiple times for the same property Address. This approach may be a bad idea if property details are out of date, or updated frequently. 
- Ideally before production I like to do a security test using some type of load testing or security auditing (For example, Kali Linux and Metasploit framework)
  
## Next Steps
- Unit tests were completed to check basic cases and not edge cases. 
- unit testing and automation testing for the frontend => this seemed too far out of scope for this assignment. However, if I were to I would use Jest for unit testing and Selenium for automation Testing.
- CI/CD As-Is this would be a straight forward project to add some CI/CD within github/gitlab, we would have to substitute the postman mock server for a CI/CD friendly alternative.

## JSON-Object
```
{
    "property/details": {
        "api_code_description": "ok",
        "api_code": 0,
        "result": {
            "property": {
                "air_conditioning": "yes",
                "attic": false,
                "basement": "full_basement",
                "building_area_sq_ft": 1824,
                "building_condition_score": 5,
                "building_quality_score": 3,
                "construction_type": "Wood",
                "exterior_walls": "wood_siding",
                "fireplace": false,
                "full_bath_count": 2,
                "garage_parking_of_cars": 1,
                "garage_type_parking": "underground_basement",
                "heating": "forced_air_unit",
                "heating_fuel_type": "gas",
                "no_of_buildings": 1,
                "no_of_stories": 2,
                "number_of_bedrooms": 4,
                "number_of_units": 1,
                "partial_bath_count": 1,
                "pool": true,
                "property_type": "Single Family Residential",
                "roof_cover": "Asphalt",
                "roof_type": "Wood truss",
                "site_area_acres": 0.119,
                "style": "colonial",
                "total_bath_count": 2.5,
                "total_number_of_rooms": 7,
                "sewer": "municipal",
                "subdivision" : "CITY LAND ASSOCIATION",
                "water": "municipal",
                "year_built": 1957,
                "zoning": "RH1"
            },

            "assessment":{
                "apn": "0000 -1111",
                "assessment_year": 2015,
                "tax_year": 2015,
                "total_assessed_value": 1300000.0,
                "tax_amount": 15199.86
            }
        }
    }
}
```