from discord.ext import commands
import os

POKEMON_CHANNEL = int(os.environ['POKEMON_CHANNEL'])
DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']

bot = commands.Bot(command_prefix='Nayeon ', bot=False)

@bot.event
async def on_ready():
    channel = bot.get_channel(POKEMON_CHANNEL)

    if channel is not None:
        await channel.send('$p')
    else:
        print('Channel not found.')

    await bot.close()


bot.run(DISCORD_BOT_TOKEN)
