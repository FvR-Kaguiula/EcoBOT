import random
import requests

def gen_ecoemoji():
    emoji = ["🌿", "🌱", "🌳", "🌲", "🌍", "🌸", "🍃", "🌼", "🌻", "🌾", "🌺", "🍀"]
    themoji = random.choice(emoji)
    return themoji


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


def get_weather_info_url():    
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    querystring = {EXAMPLECOORD}
    headers = {
	"x-rapidapi-key": "EXAMPLEKEYACCESS",
	"x-rapidapi-host": "weatherbit-v1-mashape.p.rapidapi.com"
}
    res = requests.get(url, headers=headers, params=querystring)
    data = res.json()
    
    #Regresar la información ordenada
    weather_data = data['data'][0]
    formatted_data = (
        f"Ciudad: {weather_data['city_name']}\n"
        f"Temperatura: {weather_data['temp']}°C\n"
        f"Descripción: {weather_data['weather']['description']}\n"
        f"Viento: {weather_data['wind_spd']} mph desde {weather_data['wind_cdir_full']}\n"
        f"Humedad: {weather_data['rh']}%\n"
        f"Presión: {weather_data['pres']} mb\n"
        f"Índice UV: {weather_data['uv']}\n"
        f"Visibilidad: {weather_data['vis']} millas\n"
        f"Hora de observación: {weather_data['ob_time']}\n"
    )
    return(formatted_data)

def info_list():
    info_list_commands = (
        "**$hola**: El bot dice hola\n"
        "**$adios**: El bot dice adiós\n"
        "**$ecomeme**: El bot envia un meme aleatoria de un conjunto de imagenes\n"
        "**$ecoemoji**: Genera un emoji aleatorio\n"
        "**$patos**: Foto de patos\n"
        "**$perros**: Foto de perros\n"
        "**$tiempo**: Muestra información sobre el tiempo\n"
    )
    return info_list_commands

def ecotips_list():
    ecotips_list = (
        "**$Paneles solares**: Instala paneles solares para generar electricidad\n"
        "**$adios**: El bot dice adiós\n"
        "**$ecomeme**: El bot envia un meme aleatoria de un conjunto de imagenes\n"
        "**$ecoemoji**: Genera un emoji aleatorio\n"
        "**$patos**: Foto de patos\n"
        "**$perros**: Foto de perros\n"
        "**$tiempo**: Muestra información sobre el tiempo\n"
    )
    return ecotips_list
