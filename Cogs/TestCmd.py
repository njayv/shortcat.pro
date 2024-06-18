from discord import Option, ApplicationContext, slash_command
from discord.ext import commands

class testcmd(commands.Cog):

    def init(self, bot):
        self.bot: commands.Bot = bot
    
    @commands.command()
    async def Test(self, ctx: commands.Context):
        await ctx.send("It didn't work :clueless:")

    @slash_command(name='ping')
    async def ping(self, ctx: ApplicationContext):
        await ctx.respond("Pong!")
    
    @slash_command(name='choose')
    async def choose(self, ctx: ApplicationContext, selection=Option(name='uhh', description='Pick this one!', choices=['A', 'B', 'C'])):
        await ctx.respond(f"You selected: {selection}")


def setup(bot: commands.Bot):
    bot.add_cog(testcmd(bot))