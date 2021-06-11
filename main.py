from keep_alive import keep_alive
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="dank memer robbers"))
        
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('pls rob'):
		await message.channel.send("You try to steal only to notice that rob was disabled in this server! You didn't know about this or you really is an idiot, and ended up getting this message.<br>**Tip:** Do not try to steal from any other guy in this server. Bankrob is also disabled.")
		
	if message.content.startswith('Pls rob'):
		 await message.channel.send("You try to steal only to notice that rob was disabled in this server! You didn't know about this or you really is an idiot, and ended up getting this message.<br>**Tip:** Do not try to steal from any other guy in this server. Bankrob is also disabled.")
	if message.content.startswith('$credits'):
	  await message.channel.send('Developer: ChesterWOV#2768; On repl.it')
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(os.getenv('TOKEN'))
