import json
import requests

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def upload_to_ipfs(data):
    # Implementasi fungsi untuk upload ke IPFS
    # Ini hanya contoh, Anda perlu menggantinya dengan implementasi yang sebenarnya
    api_url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": "YOUR_PINATA_API_KEY",
        "pinata_secret_api_key": "YOUR_PINATA_SECRET_API_KEY"
    }
    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()['IpfsHash']
    else:
        raise Exception("Failed to upload to IPFS")