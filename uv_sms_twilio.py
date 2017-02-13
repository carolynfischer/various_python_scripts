from twilio.rest import TwilioRestClient
import requests
import json

# put your own credentials here
ACCOUNT_SID = 'AC35b50441bb1747209a47261121cde171'
AUTH_TOKEN = '5aad2981b7ebb1d8f9b47033421b6522'
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

# UV forecast 
uv_url="https://iaspub.epa.gov/enviro/efservice/getEnvirofactsUVHOURLY/ZIP/94109/json"
uv_response = requests.get(uv_url)
uv_data = json.loads(uv_response.text)
maximum_uv = -1
uv_time = 0

for entry in uv_data:
    if entry['UV_VALUE'] > maximum_uv:
        maximum_uv = entry['UV_VALUE']
        uv_time = entry['DATE_TIME'].split()[1] \
                + " " + entry['DATE_TIME'].split()[2]

# Rain forecast
# this uses as API that gathers weather information from different sources
url = "https://www.metaweather.com/api/location/2487956/"
response = requests.get(url)
data = json.loads(response.text)
umbrella = False

for source in data['consolidated_weather']:
    if "Showers" or "Rain" in source['weather_state_name']:
        umbrella = True

if umbrella:
    rain = "You should bring an umbrella today, it's going to rain"

    client.messages.create(
       to = '+16504850646',
       from_ = '+16504698266',
       body = rain,
    )

if maximum_uv >= 6:
    message = "The maximum UV value today is " + str(maximum_uv) \
            + " at " + str(uv_time) \
            + ". Use sunscreen and try to stay indoors from 12 to 2 PM."

    client.messages.create(
       to = '+16504850646',
       from_ = '+16504698266',
       body = message,
    )