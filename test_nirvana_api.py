import requests


# valid status code test for Nirvana API
def test_nirvana_s_code():
    resp = requests.get("https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")
    print(resp.status_code)
    assert resp.status_code == 200

# INVALID status code test for Nirvana API
def test_nirvana_s_code_invalid():
    resp = requests.get("https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")
    print(resp.status_code)
    assert resp.status_code == 205

# valid founding date of Nirvana
def test_nirvana_founded():
    resp = requests.get("https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")
    json_response = resp.json()
    print(json_response["life-span"]["begin"])
    assert (json_response["life-span"]["begin"]) == "1988-01"

# INVALID founding date of Nirvana
def test_nirvana_founded_invalid():
    resp = requests.get("https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")
    json_response = resp.json()
    print(json_response["life-span"]["begin"])
    assert (json_response["life-span"]["begin"]) == "1990-01"



# valid end date of Nirvana
def test_nirvana_disbanded():
    resp = requests.get("https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")
    json_response = resp.json()
    print(json_response["life-span"]["end"])
    assert (json_response["life-span"]["end"]) == "1994-04-05"

# INVALID end date of Nirvana
def test_nirvana_disbanded_invalid():
    resp = requests.get("https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")
    json_response = resp.json()
    print(json_response["life-span"]["end"])
    assert (json_response["life-span"]["end"]) == "1999-04-09"



# valid test - nirvana is no longer an active band
def test_nirvana_notActive():
    resp = requests.get("https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")
    json_response = resp.json()
    print(json_response["life-span"]["ended"])
    assert (json_response["life-span"]["ended"]) == True

# INVALID test - nirvana is no longer an active band
def test_nirvana_notActive_invalid():
    resp = requests.get("https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")
    json_response = resp.json()
    print(json_response["life-span"]["ended"])
    assert (json_response["life-span"]["ended"]) == False


# valid city of birth for Nirvana
def test_nirvana_place():
    resp = requests.get("https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")
    json_response = resp.json()
    print(json_response["begin-area"]["name"])
    assert (json_response["begin-area"]["name"]) == "Aberdeen"

# INVALID city of birth for Nirvana
def test_nirvana_place_invalid():
    resp = requests.get("https://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")
    json_response = resp.json()
    print(json_response["begin-area"]["name"])
    assert (json_response["begin-area"]["name"]) == "Haifa"



