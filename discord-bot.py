import discord
import logging
from discord.ext import commands
#importando as bibliotecas necessárias: Discord é a biblioteca básica do discord.py; logging é uma biblioteca que ajuda a organizar e outputar erros; discord.ext é uma biblioteca para comandos mais avançados, da qual pegamos justamente commands.
#importing the necessary libraries: Discord is discord.py's basic library; logging is a library that helps to organize and output errors; discord.ext is a library with more advanced commands, from which we are importing commands, which does exactly that.
client = discord.Client()
#prepara o client, que é necessário para que o bot consiga se comunicar com o Discord. Para mais informações, leia a documentação do Discord.py.
#sets up the client so that the bot can communicate with Discord. For more information, read the Discord.py documentation.

@client.event
async def on_ready ():
    print ('bot ON!'.format(client))
#faz com que o bot imprima no terminal a mensagem "bot ON!" quando ele estiver logado no Discord. Isso ajuda a saber quando o bot realmente está ligado e funcionando.
#this makes it so the bot prints the message "bot ON!" in the terminal when it's succesfully logged onto Discord. This helps us by showing us when the bot is online and working.


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!teste'):
        await   message.channel.send('teste')
#esse comando ativa quando qualquer mensagem é enviada. Caso o autor da mensagem seja o próprio bot, o comando é encerrado - isso serve para evitar que o bot fique se respondendo ou executando o comando infinitamente. Em seguida, ele checa se a mensagem começa com "!teste", caso isso seja verdade, ele escreve a mensagem "teste."
#this command activates when any message is sent. If the author of the message is the Bot itself, the command is terminated - this serves to prevent the bot from answering itself, or that the command runs infinitely. Then it checks if the messager starts with "!Test", and if that is true, it writes the message "test". 
@client.event
async def on_message(message):
    if str(message.role) == ('reaper'):
        await message.channel.purge(limit = 1)

client.run('OTU4NDI1MDc2MzA5NTg1OTQw.YkNI6A.nR9DOPgQV_n43OWDMOZah7Sm8G4')
#isso fornece à API o token do nosso bot, para que este possa se comunicar com o Discord através dela.
#this provides the API our bot's token so that it can communicate with Discord through that.