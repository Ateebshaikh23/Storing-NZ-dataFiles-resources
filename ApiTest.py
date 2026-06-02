import requests
import json

# Replace with your actual API token
API_TOKEN = "YOUR_API_TOKEN"

# Replace {id} with a competition ID
# Example: 2021 = Premier League
competition_id = 2021

url = f"https://api.football-data.org/v4/competitions/{competition_id}/matches"

headers = {
    "X-Auth-Token": "c4e87582dce64646a8933f210577ffc9"
}

response = requests.get(url, headers=headers)

print(f"Status Code: {response.status_code}")

if response.status_code != 200:
    print("\nError Response:")
    print(response.text)
    exit()

data = response.json()

print("\nResponse Type:")
print(type(data))

if isinstance(data, dict):
    print("\nTop Level Keys:")
    print(list(data.keys()))

    # Print nested structure information
    for key, value in data.items():
        print(f"\n{key}: {type(value).__name__}")

        if isinstance(value, dict):
            print(f"  Keys: {list(value.keys())[:20]}")

        elif isinstance(value, list):
            print(f"  Records: {len(value)}")

            if len(value) > 0 and isinstance(value[0], dict):
                print(f"  Sample Fields: {list(value[0].keys())}")

elif isinstance(data, list):
    print(f"\nTotal Records: {len(data)}")

    if len(data) > 0 and isinstance(data[0], dict):
        print("\nFields:")
        print(list(data[0].keys()))

print("\nSample Data:")
print(json.dumps(data, indent=2)[:5000])