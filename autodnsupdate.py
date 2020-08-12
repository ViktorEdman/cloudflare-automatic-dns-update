import requests
import json
import datetime
from settings import token, zoneId

url = "https://api.cloudflare.com/client/v4/zones/"+zoneId+"/dns_records"

payload = ""
headers = {
    'content-type': "application/json",
    'authorization': "Bearer "+token
    }

dnsResponseJson = requests.request("GET", url, data=payload, headers=headers)
dnsResponseObject = json.loads(dnsResponseJson.text)
dnsZoneArray = dnsResponseObject['result']

dnsZoneIp = ""
entryId = ""

for dnsZone in dnsZoneArray:
    if dnsZone['type'] == "A":
        dnsZoneIp = dnsZone['content']
        entryId = dnsZone['id']



externalIpResponse = requests.get('http://ipinfo.io/ip')
externalIp = externalIpResponse.content.strip()

print(datetime.datetime.now())
print("DNS Zone IP: "+dnsZoneIp)
print("Current external IP: "+externalIp)

if dnsZoneIp == externalIp:
    print('Match!')
    print('No DNS update required\n')
else:
    print('Mismatch!')
    payload = "{\n\t\"content\": \""+externalIp+"\"\n}"
    url = "https://api.cloudflare.com/client/v4/zones/"+zoneId+"/dns_records/"+entryId
    response = requests.request("PATCH", url, data=payload, headers=headers)
    if response.ok:
        print('Updated DNS Record to '+externalIp+"\n")
    else:
        print('Could not update DNS record because: '+response.reason+"\n")
