import requests
import json

def get_aci_token(apic_url, username, password):
    url = f"https://{apic_url}/api/aaaLogin.json"
    payload = json.dumps({
        "aaaUser": {
            "attributes": {
                "name": username,
                "pwd": password
            }
        }
    })
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, data=payload, headers=headers, verify=False)
        response.raise_for_status
        token = response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]
        print("Authentication successful")
        return token
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")