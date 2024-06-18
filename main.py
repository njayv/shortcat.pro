import os, discord
from discord import slash_command, Option
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents |= discord.Intents.guilds
intents |= discord.Intents.messages
intents |= discord.Intents.message_content
intents |= discord.Intents.members

owners = [984833786560794624]

class customBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    

    async def close(self):
        for name,cog in self.cogs.items():
            cog._eject(self)
            print(f"Ejected {name}")
        await super().close()


bot = customBot(
    command_prefix=".", case_insensitive = True, help_command = None,
    intents=intents, owner_ids = set(owners), 
    status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Bagging tutorials...")
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

bot.run(os.getenv('discBot_token'))