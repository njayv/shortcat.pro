import discord
import json
from discord import Option, ApplicationContext, slash_command
from discord.ext import commands

class testcmd(commands.Cog):

    def init(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(name='track_strategy', description="Display the Track Strategy of a given track name.")
    async def track_strat(self, ctx: ApplicationContext, map_selection=Option(name='track_name', description='Use Abbreviation Of Track!')):

        with open("./track_jsons/strategy.json", "r+") as f:
            strategies= json.load(f)
            picked_strategy= [entry for entry in strategies if entry["code"] == map_selection]
            if len(picked_strategy) == 0:
                return await ctx.respond("That's not a track! Try using the abbriviation of the track you'd like to see.\n-# For example: MKS = Mario Kart Stadium, rMMM = Moo Moo Meadows ('r' meaning Retro Cup), dBP = Baby Park ('d' meaning DLC), bKC ('b' meaning Booster Course)")
            picked_strategy= picked_strategy[0]           
        
        embed_msg = discord.Embed(
            colour= discord.Color.random(),
            title= str(map_selection),
            thumbnail= f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/{str(map_selection).lower()}.webp",
            description= picked_strategy["description"]
            )

        #embed_msg.set_footer(text= "Images and descriptions taken from the 'shortcat.pro' website.", icon_url= 'https://shortcat.pro')
        #embed_msg.set_image(url= f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/{str(map_selection).lower()}.webp")

        await ctx.respond(embed= embed_msg)

    @slash_command(name='item_map', description="Display the Item Map of a given track name.")
    async def item_map(self, ctx: ApplicationContext, map_selection=Option(name='track_name', description='Use Abbreviation Of Track!')):

        embed_msg = discord.Embed(
            colour= discord.Color.random(),
            title= str(map_selection),
            description= "Test"
            )
        
        embed_msg.set_footer(text= "Images and descriptions taken from the 'shortcat.pro' website.", icon_url= 'https://shortcat.pro')
        embed_msg.set_image(url= f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/item_dist_map/{str(map_selection).lower()}.webp")

        await ctx.respond(embed= embed_msg)


def setup(bot: commands.Bot):
    bot.add_cog(testcmd(bot))