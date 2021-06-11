from keep_alive import keep_alive
from discord.ext import commands
import discord
import os
import time

TOKEN = os.environ['TOKEN']

client = commands.Bot(command_prefix = 's!')

ublacklist = {705252529499275354}

wblacklist = {"@here", "@everyone"}

@client.event
async def on_ready():
  print('We logged in to Discord. \nNow you can start using us.')
  
@client.command(name="ping", help="--Sends you a message. This is to make sure the bot works.")
async def ping(ctx):
  await ctx.send('Pong!')
  
@client.command(name="spam", help="--Spams the text you added after the command", category="Main Function")
async def spam(ctx, *Text): 
  if ctx.author.id in ublacklist:
        return
  
  output = ''
  
  for word in Text:
    output += word
    output += ' '
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  await ctx.send(output)
  time.sleep(.7)
  
@client.command(name="announce", help="--This is an bot developer-only command.", category="Developer Only")
async def announce(ctx, *Announcement):
  if ctx.message.author.id == 788274635871092777:
    annouce = ''
    for word in Announcement:
     annouce += word
     annouce += ' '
     
    await ctx.message.delete()
    await ctx.send(annouce)
    
  else:
     await ctx.send(message.author, "Hey, you are not the owner of this bot! Do not try to use this command! \n \nTip: Type `s!help [command]` to know more about that command.")
  
keep_alive()
client.run(TOKEN)