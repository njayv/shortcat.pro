import discord
from discord import Option, ApplicationContext, slash_command
from discord.ext import commands

class testcmd(commands.Cog):

    def init(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(name='track_strategy', description="Display the Track Strategy of a given track name.")
    async def map_image(self, ctx: ApplicationContext, map_selection=Option(name='track_name', description='Use Abbreviation Of Track!')):
        embed_msg = discord.Embed(
            colour= discord.Color.random(),
            title= str(map_selection),
            
            )
        
        embed_msg.set_footer(text= "Images and descriptions taken from the 'shortcat.pro' website.", icon_url= 'https://shortcat.pro')
        embed_msg.set_image(url= f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/{map_selection}.webp")

        await ctx.respond(embed= embed_msg)

    @slash_command(name='item_map', description="Display the Item Map of a given track name.")
    async def map_image(self, ctx: ApplicationContext, map_selection=Option(name='track_name', description='Use Abbreviation Of Track!')):
        embed_msg = discord.Embed(
            colour= discord.Color.random(),
            title= str(map_selection),
            
            )
        
        embed_msg.set_footer(text= "Images and descriptions taken from the 'shortcat.pro' website.", icon_url= 'https://shortcat.pro')
        embed_msg.set_image(url= f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/item_dist/{map_selection}.webp")

        await ctx.respond(embed= embed_msg)


def setup(bot: commands.Bot):
    bot.add_cog(testcmd(bot))