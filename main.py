from discord.ext import commands, tasks
import os, random, asyncio

SPECIFIED_USER_ID = int(os.environ['SPECIFIED_USER_ID'])
CRON_JOB_HOURS = int(os.environ['CRON_JOB_HOURS'])
POKEMON_CHANNEL = int(os.environ['POKEMON_CHANNEL'])
DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']
EMOJIS = ['❤️', '💖', '💗', '💓', '💕', '💞', '💘', '😍', '🥰', '😘', '😻']

bot = commands.Bot(command_prefix='Nayeon ', bot=False)

@tasks.loop(hours=CRON_JOB_HOURS)
async def cronjob1():
    print('Cronjob 1 executed')
    channel = bot.get_channel(POKEMON_CHANNEL)

    if channel is not None:
        await channel.send('$p')
    else:
        print('Channel not found.')


@bot.event
async def on_ready():
    print(f'Bot is logged in as {bot.user}')
    if not cronjob1.is_running():
        cronjob1.start()


@bot.event
async def on_message(message):
    is_expected_user_message = (message.author.id == SPECIFIED_USER_ID and message.content.startswith("$p"))
    if is_expected_user_message and random.random() < 0.7:
        await asyncio.sleep(random.uniform(0.5, 1.5))
        await message.add_reaction(random.choice(EMOJIS))

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(DISCORD_BOT_TOKEN)
