import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("Client ID: {0.user.id}".format(bot))
    print("-----------------------------------------")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    

    user = message.author
    msg = message.content
    try:
        print(f"{user} said {msg}")
    except UnicodeEncodeError:
        print(f"{user.id} said {msg}")

    await bot.process_commands(message)


@bot.command()
async def testembed(ctx):
    emebed = discord.Embed(title="Title", description="dess", color=discord.Color)




@bot.command()
async def annoy(ctx, member: discord.Member):
    await ctx.message.delete()
    for i in range(100):
        await member.send("BAISSE D'UN TON")

@bot.command(aliases=["dit-moi-ca"])
async def say(ctx, *, words):
    await ctx.send(words)



@bot.command()
async def ping(ctx):
    await ctx.send("message")



bot.run(config.TOKEN)
