import discord
import json
from discord import Option, ApplicationContext, slash_command
from discord.ext import commands

rgb_map = {
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "yellow": (255, 255, 0),
    "gold": (255, 215, 0),
    "green": (0, 128, 0),
    "brown": (165, 42, 42),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "blue": (0, 0, 255),
}

class testcmd(commands.Cog):

    def init(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(name='track_strategy', description="Display the Track Strategy of a given track name.")
    async def track_strat(self, ctx: ApplicationContext, map_selection=Option(name='track_name', description='Use Abbreviation Of Track!')):

        with open("./track_jsons/strategy.json", "r+") as f:
            strategies= json.load(f)
            picked_strategy= [entry for entry in strategies if entry["code"].lower() == map_selection.lower()]
            if len(picked_strategy) == 0:
                return await ctx.respond("That's not a track! Try using the abbriviation of the track you'd like to see.\n-# For example: MKS = Mario Kart Stadium, rMMM = Moo Moo Meadows (**r** meaning Retro Cup), dBP = Baby Park (**d** meaning DLC), bKC (**b** meaning Booster Course)")
            picked_strategy= picked_strategy[0]
        
        embed_msg = discord.Embed(
            colour= discord.Color.from_rgb(*rgb_map.get(picked_strategy["color"], (0, 0, 0))),
            title= str(picked_strategy["name"]),
            thumbnail= f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/{str(map_selection).lower()}.webp",
            description= picked_strategy["description"]
            )

        embed_msg.set_footer(text= "Images and descriptions taken from the 'shortcat.pro' website.", icon_url= 'https://shortcat.pro/favicon.png')
        embed_msg.set_image(url= f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/cup_location/{picked_strategy["cup"]}.png")

        await ctx.respond(embed= embed_msg)

def setup(bot: commands.Bot):
    bot.add_cog(testcmd(bot))