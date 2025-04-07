# %%
import requests
import json

response = requests.get('https://br1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1&api_key=RGAPI-7e988315-3513-48d5-8df0-161d40298a5a')
response.status_code

# %%
json_data = json.loads(response.text)
# %%
print(json_data[0],['res'][0])
# %%
