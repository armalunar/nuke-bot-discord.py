import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.guild_messages = True
intents.reactions = True
intents.message_content = True


bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Define a atividade do bot
    await bot.change_presence(activity=discord.Game(name=".nuke para nukar um canal"))



@bot.command()
async def nuke(ctx):
    
    if ctx.author.guild_permissions.administrator:
        
        deleted_channel = ctx.channel

        
        category = deleted_channel.category

       
        new_channel = await deleted_channel.clone()
        await new_channel.edit(position=deleted_channel.position)

       
        await new_channel.edit(category=category)

        
        await deleted_channel.delete()

        # Envia a mensagem de confirmação no novo canal
        await new_channel.send(f'```O canal {deleted_channel.name} foi nukado.```')

    else:
        await ctx.send('Você não tem permissão para usar este comando.')
		
# rode o bot
bot.run("Coloque seu token aqui")



# Créditos - armalunar