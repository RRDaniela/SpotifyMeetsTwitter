import requests
import json 

#Configuración
urlReproduccionReciente="https://api.spotify.com/v1/me/player/currently-playing"
token="BQDpAYyZjorYEdsudMqzDsX5h_Ssz_Jv-Iyqk9CgQhOXfDEuiKeimmXbfhaJtpjVqXh0XaHCYvygqb58fIErhUcu1wVMU2_OvFDJKmMORByjurO2hQV08PyjzYnKEHMndJgzX3B4CZClPwdBuUmE_kbSNwhj-MU1yswyUgMz_bZAZrgb"
user_id="1280778938?si=6cHOzXEEQDWR9udOsXGdOg"

query=f'{urlReproduccionReciente}'

response=requests.get(query,
            headers={"Content-Type":"application/json",
            "Authorization":f"Bearer {token}"})


respuesta=response.json()

print(respuesta['item']['name'])
#cancion = respuesta['item']['name']
#artista = respuesta['item']['artists'][0]['name']
#id_Artista = respuesta['item']['artists'][0]['id']

#print(f"Cancion: {cancion} Artista: {artista} Id: {id_Artista}")

'''
# SETTINGS 
endpoint_url = "https://api.spotify.com/v1/recommendations?"
token = "BQBwSnbMO2bUtZ8mJ07bddrUBkC_XlOek78vPutjX_6xCcGCnqo5L4v7Qqy6s0xLnrT9gGJ5n1MO1WiewU4ekwJQ_irZshWEMuWQOljLPZqsD0UZACceCkqky2B40IE4N4M_tDl3syabwNVa_SHfGA9Jk4eBYpLluAFoLJrgB4w"
user_id = "1280778938?si=6cHOzXEEQDWR9udOsXGdOg"


# OUR FILTERS
limit=10
market="US"
seed_genres="indie"
target_danceability=0.5
uris = [] 

# PERFORM THE QUERY
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'


response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()

json_response = response.json()

for i in json_response['tracks']:
            uris.append(i)
            print(f"\"{i['name']}\" by {i['artists'][0]['name']}")
'''