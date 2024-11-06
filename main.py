import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Merhaba {client.user}! ben bir botum!')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)




    if message.content.startswith('iklim değişikliği nedir?'):
        await message.channel.send("nedeni ne olursa olsun iklimin ortalama durumunda ve/ya da değişkenliğinde onlarca yıl ya da daha uzun süre boyunca gerçekleşen değişiklikler")
        
client.run("")
