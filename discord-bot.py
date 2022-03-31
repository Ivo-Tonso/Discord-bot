#IF YOU HAVE TROUBLE UNDERSTANDING ANYTHING IN HERE, YOU SHOULD EITHER READ THE DISCORD.PY DOCUMENTATION OR CONTACT ME. MY SOCIALS ARE ON README
#SE VOCÊ TIVER DIFICULDADE PARA ENTENDER QUALQUER COISA AQUI, VOCÊ DEVERIA OU LER A DOCUMENTAÇÃO OFICIAL DO DISCORD.PY, OU ME CONTACTAR. MINHAS REDES SOCIAIS ESTÃO NO README.MD
#LIBRARIES AND PREPARATIONS----------------------------
import discord
#biblioteca principal do discord.py. O bot inteiro é baseado nela.
#main discord.py library. The entire bot is based on it.
from discord.ext import commands
#nos dá opções mais avançadas de comandos, além de um prefixo global para os mesmos (como mostrado abaixo)
#gives us access to more advanced command options, as well as a global prefix (as shown below)
client = commands.Bot (command_prefix="!")
#seta o client para que possamos interagir com o Discord, e define o prefixo de todos os comandos como sendo "!"
#sets the client so that we can interact with Discord, and sets the prefix for all commands as "!"
#------------------------------------------------------

#MAIN CODE---------------------------------------------
@client.event
async def on_ready ():
    print ('bot ON!'.format(client))
#faz com que o bot imprima no terminal a mensagem "bot ON!" quando ele estiver logado no Discord. Isso ajuda a saber quando o bot realmente está ligado e funcionando.
#this makes it so the bot prints the message "bot ON!" in the terminal when it's succesfully logged onto Discord. This helps us by showing us when the bot is online and working.
@client.command()
async def teste (ctx):
    await ctx.send('teste')
#comando simples de teste. O bot espera o prefixo definido no começo do arquivo, para então identificar o contexto "teste" - ele então manda uma mensagem dizendo "teste".
#simple test command. The bot waits for the prefix defined in the beginning of the code, and then identifies the context "test" - it then simply sends a message conaining "text".
client.run('token')
#isso fornece à API o token do nosso bot, para que este possa se comunicar com o Discord através dela. Você deve colocar o Token do seu próprio bot aqui.
#this provides the API our bot's token so that it can communicate with Discord through that. You need to input your bot's own token here
#-----------------------------------------------------
