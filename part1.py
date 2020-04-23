import requests
import json 

#Configuración
urlReproduccionReciente="https://api.spotify.com/v1/me/player/currently-playing"
token="BQDAJHoQs-53W7x7KafUMIYekg2kuOT7Wu0Me21yM5ws8pWUmMLioGrlnCOO3aXbUo6VosiRYZWNbQy2mokY1g-kuqOYAvv8g-u2H4YISHxuCjY19j0BrMgnxruQJA418T8fxdyvUEwdr6T8Z_5rXTIJDwdVYTKJEePgjaF7zZwsQrK1"
user_id="1280778938?si=6cHOzXEEQDWR9udOsXGdOg"

query=f'{urlReproduccionReciente}'

response=requests.get(query,
            headers={"Content-Type":"application/json",
            "Authorization":f"Bearer {token}"})


respuesta=response.json()

cancion = respuesta['item']['name']
artista = respuesta['item']['artists'][0]['name']
id_Artista = respuesta['item']['artists'][0]['id']

print(f"Cancion: {cancion} Artista: {artista} Id: {id_Artista}")

