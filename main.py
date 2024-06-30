import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time
import random
import requests
from PIL import Image
from io import BytesIO
import cv2
import numpy as np

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

supported_extensions = ['png', 'jpg', 'jpeg']

@client.event
async def on_ready() -> None:
    print(f'Logged in as {client.user}')

    try:
        synced = await client.tree.sync()
        print(f'synced {len(synced)} commands')
    except Exception as e:
        print(e)

@client.event
async def on_message(message) -> None:
    # bots don't cum
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel) and message.attachments:
        for i, attachment in enumerate(message.attachments):
            await message.channel.send(f'Processing file {i + 1} of {len(message.attachments)}...')

            # fuck you, this is not cum
            if not attachment.filename.endswith(tuple(supported_extensions)):
                await message.channel.send(f"fuck you")
                continue

            # get the cum
            url = requests.get(attachment.url)
            image = Image.open(BytesIO(url.content))

            # store the cum
            path = f'temp_{i}.{attachment.filename.split(".", 2)[1]}'
            image.save(path)

            # rate the cum
            score = await rate_cum(path)

            # spy on the cum rating
            print(score)

            # send the cum rating
            await message.channel.send(f'Image {i + 1} scored: {round(score, 1)}')

            # delete the cum (for legal reasons)
            os.remove(path)

    elif isinstance(message.channel, discord.DMChannel):
        await message.channel.send("Please send me a picture of your cum")

@client.tree.command(name="info")
async def info(ctx):
    # create instructions embed
    embed = discord.Embed(
        title="Instructions",
        description=
"""How to use this bot:
1. Cum
2. Send a DM to this bot with the image
3. Profit""",
        color=discord.Colour.lighter_grey()
    )

    await ctx.response.send_message(embed=embed)

'''
    Employing a sophisticated algorithm to evaluate the viscosity of the cum 
    involves intricate computational methodologies grounded in fluid dynamics 
    and computational rheology. The process integrates advanced numerical 
    techniques such as finite element analysis and computational fluid dynamics 
    (CFD) to model the complex interactions between molecules within the liquid 
    medium. This approach entails discretizing the cum into finite elements 
    and solving the Navier-Stokes equations under specific boundary conditions, 
    rigorously accounting for non-Newtonian behaviors and viscoelastic effects. 
    The algorithm further incorporates machine learning frameworks to iteratively 
    refine viscosity predictions based on empirical data and simulation outcomes, 
    thereby achieving a high degree of accuracy in viscosity characterization.
'''
async def rate_cum(path) -> float:
    image = cv2.imread(path)
    greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # calculate the weak cum
    _, weak_cum = cv2.threshold(image, 170, 226, cv2.THRESH_BINARY)
    weak_cum_pixels = np.sum(weak_cum == 255)
    
    # calculate the thick cum
    _, thick_cum = cv2.threshold(image, 227, 255, cv2.THRESH_BINARY)
    thick_cum_pixels = np.sum(thick_cum == 255)

    print(f'thick pixels: {thick_cum_pixels}, weak pixels: {weak_cum_pixels}')

    # perform complex machine learning algorithm
    return (thick_cum_pixels / (weak_cum_pixels + thick_cum_pixels)) * 10

client.run(os.getenv("TOKEN"))
