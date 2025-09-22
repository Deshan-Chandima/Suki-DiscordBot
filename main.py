import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler= logging.FileHandler(filename='discord.log', encoding='utf-8',mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)

role1="gaymer"

@bot.event
async def on_ready():
    print(f"We are Ready to go in,{bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}- dont use that words!")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello{ctx.author.mention}!")

@bot.command()
async def assign(ctx):
    role=discord.utils.get(ctx.guild.roles, name=role1)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned to {role1}")
    else:
        await ctx.send("Role doesn't exit")

@bot.command()
async def remove(ctx):
    role=discord.utils.get(ctx.guild.roles, name=role1)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has had been {role1} removed")
    else:
        await ctx.send("Role doesn't exit")

@bot.command()
async def dm(ctx,*,msg):
    await ctx.author.send(f"You said {msg}")

@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to you msg")

@bot.command()
async def poll(ctx,*, question):
    embed =discord.Embed(title="New poll",description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎🏿")
    

@bot.command()
@commands.has_role(role1)
async def secret(ctx):
    await ctx.send("welcome to the club!")

@secret.error
async def secret_error(ctx, error):
    if isinstance(error , commands.MissingRole):
        await ctx.send("You do not have permission to do that!")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)