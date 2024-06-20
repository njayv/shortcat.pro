import discord
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
    
    @slash_command(name= 'choose', description= 'Choose a track to view info about.')
    async def choose(self, ctx: ApplicationContext, selection=Option(name='track', description='Name of track. E.g. MKS (Mario Kart Stadium)', choices=['MKS', 'Other', 'Not Sure'])):
        await ctx.respond(f"You selected: {selection}")
    
    @slash_command(name= 'map_image', description= 'Send and image of the track selected.')
    async def map_image(self, ctx: ApplicationContext, map_selection=Option(name='track_name', description='Name of the track.', choices=['MKS', 'Not Implemented Yet'])):
        await ctx.respond(file= discord.File(f'./map_images/{map_selection}.webp'))
    
    @slash_command(name='map_image_embed', description="Send and image of the track selected. (But it's an embed)")
    async def map_image(self, ctx: ApplicationContext, map_selection=Option(name='track_name', description='Name of the track.', choices=['MKS', 'WP', 'SSC', 'TR'])):
        embed_msg = discord.Embed(colour= discord.Color.from_rgb(114, 137, 218), title= str(map_selection))
        embed_msg.set_image(url= f"https://raw.github.com/njayv/shortcat.pro/master/map_images/{map_selection}.webp")
        await ctx.respond(embed= embed_msg)


def setup(bot: commands.Bot):
    bot.add_cog(testcmd(bot))