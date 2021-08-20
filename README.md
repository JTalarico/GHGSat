# GHGSat
[GHGSat Challenge 2: REST API](https://github.com/GHGSat/tech-challenge/tree/master/webdev#challenge-2-rest-api)

## Setup
0. Prerequisites
	* pip3 installed
	* Python3 installed
1. Install requirements
	* `pip3 install -r requirements.txt`
2. Run server
	* `python3 Api.py`
3. Call API
	* Imagery Endpoint
		* `http://localhost:5000/imagery?lat=xx&lon=yy`, where xx/yy are latitude/longitude
	* Overlay Endpoint
		* `http://localhost:5000/overlay`
4. Run Tests
	* `python3 -m pytest tests/` 
