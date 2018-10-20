import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    await client.change_status(game=discord.Game(name='Pessoas no inferno, junto com a Mogi'))
    print('Estou pronta u..u')
    print(client.user.name)
    print(client.user.id)
    print('--------------')

@client.event
async def on_message(message):
    if message.content.lower() == 'milo':
        await client.send_message(message.channel, "Oiii, o que deseja?")
    if message.content.lower().startswith('rode a moeda'):
        moeda = random.randint(1, 2)
        if moeda == 1:
            await client.add_reaction(message, "😐")
        else:
            await client.add_reaction(message, "👵🏽")
    if message.content.lower().startswith('bom_dia'):
        await client.send_message(message.channel, "Bom dia, tudo bem contigo?")

    if message.content.lower().startswith('ataque milo'):
        if message.author.id == '471090543724724235' or message.author.id == '265510900000227328':
            messagem = message.content.split();
            await client.send_message(message.channel,"Dou uma cabeçada no " + messagem[2])
        else:
            await client.send_message(message.channel,"Desculpa, mas só obedeço ordens da Mogi, rum!")
    if message.content.lower().startswith('milo, mande'):
        messagem = message.content.lower().split('milo, mande')
        await client.send_message(message.channel,"Vá" + messagem[1])
    if message.content.lower().startswith('milo, eu quero um'):
        messagem = message.content.lower().split('milo, eu quero um')
        await client.send_message(message.channel,"Aqui está o seu "+ messagem[1])
    if message.content.lower().startswith('milo, diga'):
        messagem = message.content.lower().split('milo, diga')
        await client.send_message(message.channel,messagem[1])
        await client.delete_message(message)

client.run('NTAyOTYyNjkyODE5MjU1Mjk3.DqwBtg.IcOUDjQB6BVP4e84vXVQh5hthns')

