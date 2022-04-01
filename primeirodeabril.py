import discord

client = discord.Client()

@client.event
async def on_message(message):
    if str(message.author) == "Lightw4lk3r#4956":
        await message.channel.purge(limit=1)




client.run('OTU4NDI1MDc2MzA5NTg1OTQw.YkNI6A.Yhk_KR42GDFOJ8Lv7dO04firtkw')
