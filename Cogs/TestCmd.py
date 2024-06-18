from discord import Option, ApplicationContext, slash_command
from discord.ext import commands

class TestCmd(commands.Cog):

    def init(self, bot):
        self.bot: commands.Bot = bot
    
    @commands.command()
    async def Test(self, ctx: commands.Context):
        await ctx.send("It didn't work :clueless:")

def setup(bot: commands.Bot):
    bot.add_cog(TestCmd(bot))