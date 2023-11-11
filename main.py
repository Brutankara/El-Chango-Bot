import discord


TOKEN=''
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if 'https://x.com' in str(message.content):
		if message.reference and message.reference.resolved:
			await message.reference.resolved.reply(message.author.mention + ": " + message.content.replace('https://x.com', 'https://fixupx.com'))
		else:
			await message.channel.send(message.author.mention + ": " + message.content.replace('https://x.com', 'https://fixupx.com'))
		await message.delete()

	if 'https://twitter.com' in str(message.content):
		if message.reference and message.reference.resolved:
			await message.reference.resolved.reply(message.author.mention + ": " + message.content.replace('https://twitter.com', 'https://fxtwitter.com'))
		else:
			await message.channel.send(message.author.mention + ": " + message.content.replace('https://twitter.com', 'https://fxtwitter.com'))
		await message.delete()

	if message.content.startswith('!chad'):
		if message.reference and message.reference.resolved:
			await message.reference.resolved.reply(message.author.mention + ": ", file=discord.File('giga-chad.gif'))
		else:
			await message.channel.send(message.author.mention + ": ", file=discord.File('giga-chad.gif'))
		await message.delete()

client.run(TOKEN)
