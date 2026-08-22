import discord
import random
import os
from discord.ext import commands
from Ecologizer_logic import gen_ecoemoji
from Ecologizer_logic import get_duck_image_url
from Ecologizer_logic import get_dog_image_url
from Ecologizer_logic import get_weather_info_url
from Ecologizer_logic import info_list

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable bot y transferirle los privilegios
bot = commands.Bot(command_prefix= "$", intents=intents)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

#Saludar
@bot.command()
async def hola(ctx):
    await ctx.send(f"Hola! puedes consultar la lista de comandos ecológicos escribiendo $comandos")

#Despedirse
@bot.command()
async def adios(ctx):
    await ctx.send("¡Hasta luego, que la naturaleza te acompañe!🌿🌍")

#Enviar un ecomeme aleatorio (imagen)
@bot.command("ecomeme")
async def meme_aleatorio(ctx):
    mem_alet = random.choice(os.listdir("EXAMPLEDIR/EcologizerBOT/ecomemes"))

    with open(f"EXAMPLEDIR/EcologizerBOT/ecomemes/{mem_alet}", "rb") as f:
        picture = discord.File(f)
    await ctx.send (file=picture)

#Enviar un emoji aleatorio
@bot.command("ecoemoji")
async def gen_ecoemojies(ctx):
    await ctx.send(gen_ecoemoji())

#Enviar una imagen api de patos
@bot.command('patos')
async def duck(ctx):
    '''Una vez que llamamos al comando patos, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#Enviar una imagen api de perros
@bot.command('perros')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

#Enviar una info del tiempo
@bot.command('tiempo')
async def weather(ctx):
    info = get_weather_info_url()
    await ctx.send(info)

@bot.command()
async def comandos(ctx):
    commands_list = info_list()
    await ctx.send(f"Lista de comandos:\n{commands_list}")

@bot.command("tipsEco")
async def comandos(ctx):
    ecotips_list = info_list()
    await ctx.send(f"Lista de tips ecológicos:\n{ecotips_list}")

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Dicho para cuando un miembro se una"""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


bot.run("EXAMPLEKEYACCESS")
