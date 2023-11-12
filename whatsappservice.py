import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAEjLKhjxTIBO5Sm3j7RZC1ofjZAn3J85Ae7ZAONsOFzcjCXlZCVE3VMouEZAyHFDtEFkEV6qF2idQrz3wy7vR7fiZAUeTbfXYwNPZCwJrxmRxCdZAICPBQsn1CrycvdNZA4C1n1GqzrlOYumOc8TCHrZCX4yuSJ1OwhHkYkYwB6Idr8JZCVFovc9pE9MlhUB7PyX8Q7ertquIpHYUcnzIpnumJ4PoimWlXP6QBrDpFploZD"
        api_url = "https://graph.facebook.com/v17.0/147740105078242/messages"       
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)
        if response.status_code == 200:
            return True
        
        return False
        
    except Exception as exception:
        print (exception)
    return False
