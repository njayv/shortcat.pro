import discord
import json
import math
from discord import Option, ApplicationContext, slash_command
from discord.ext import commands
from discord.ui import Button, View

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

cups = [
    "mushroom",
    "flower",
    "star",
    "crown",
    "shell",
    "banana",
    "leaf",
    "lightning",
    "egg",
    "triforce",
    "crossing",
    "special",
    "bell",
    "goldendash",
    "luckycat",
    "turnip",
    "propeller",
    "rock",
    "moon",
    "fruit",
    "boomerang",
    "feather",
    "cherry",
    "acorn",
    "spiny",
]


class PaginationView(discord.ui.View):
    currentPage: int = 1
    sep: int = 5

    async def send(self, ctx):
        self.message = await ctx.respond(view=self)
        await self.updateMessage(self.data[: self.sep])

    def createEmbed(self, data):
        embed = discord.Embed(title="Test")
        for item in data:
            embed.add_field(name=item, value=item, inline=False)
        return embed

    async def updateMessage(self, data):
        self.updateButtons()
        await self.message.edit(embed=self.createEmbed(data), view=self)

    def updateButtons(self):
        total_pages = math.ceil(len(self.data) / self.sep)
        self.prev_button.disabled = self.currentPage <= 1
        self.next_button.disabled = self.currentPage >= total_pages

    @discord.ui.button(label="<", style=discord.ButtonStyle.primary)
    async def prev_button(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.defer()
        self.currentPage -= 1
        until_item = self.currentPage * self.sep
        from_item = until_item - self.sep
        await self.updateMessage(self.data[from_item:until_item])

    @discord.ui.button(label=">", style=discord.ButtonStyle.primary)
    async def next_button(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        await interaction.response.defer()
        self.currentPage += 1
        until_item = self.currentPage * self.sep
        from_item = until_item - self.sep
        await self.updateMessage(self.data[from_item:until_item])


class testcmd(commands.Cog):

    def init(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(
        name="track_strategy",
        description="Display the Track Strategy of a given track name.",
    )
    async def track_strat(
        self,
        ctx: ApplicationContext,
        map_selection=Option(
            name="track_name", description="Use Abbreviation of track!"
        ),
    ):

        with open("./track_jsons/strategy.json", "r+") as f:
            strategies = json.load(f)
            picked_strategy = [
                entry
                for entry in strategies
                if entry["code"].lower() == map_selection.lower()
            ]
            if len(picked_strategy) == 0:
                return await ctx.respond(
                    "That's not a track! Try using the abbriviation of the track you'd like to see. Try using '/tracks' to see a list of tracks\n-# For example: MKS = Mario Kart Stadium, rMMM = Moo Moo Meadows (**r** meaning Retro Cup), dBP = Baby Park (**d** meaning DLC), bKC (**b** meaning Booster Course)"
                )
            picked_strategy = picked_strategy[0]

        embed_msg = discord.Embed(
            colour=discord.Color.from_rgb(
                *rgb_map.get(picked_strategy["color"], (0, 0, 0))
            ),
            title=picked_strategy["name"],
            thumbnail=f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/{str(map_selection).lower()}.webp",
            description=picked_strategy["description"],
        )
        embed_msg.add_field(
            name="Track Type:", value=picked_strategy["type"], inline=True
        )
        embed_msg.add_field(
            name="Best Placement:", value=picked_strategy["bestPlacement"], inline=True
        )
        embed_msg.set_footer(
            text="Images and descriptions taken from the 'shortcat.pro' website.",
            icon_url="https://shortcat.pro/favicon.png",
        )
        embed_msg.set_image(
            url=f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/cup_location/{picked_strategy['cup']}.png"
        )

        await ctx.respond(embed=embed_msg)

    @slash_command(
        name="track_abbreviations",
        description="Shows all tracks and their abbrieviations.",
    )
    async def track_abbr(
        self,
        ctx: ApplicationContext,
        cup_selection=Option(
            name="cup_name", description="Name of the cup.", choices=cups
        ),
    ):

        with open("./track_jsons/strategy.json", "r+") as f:
            strategies = json.load(f)

        tracks = ""

        for entry in [entry for entry in strategies if entry["cup"] == cup_selection]:
            tracks += f"{entry['name']}: {entry['code']}\n"

        embed_title = cup_selection[0].upper() + cup_selection[1:] + " Cup"

        embed_msg = discord.Embed(
            title=embed_title,
            description=tracks,
            thumbnail=f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/cup_icons/{cup_selection}.webp",
        )

        embed_msg.set_footer(
            text="Images and descriptions taken from the 'shortcat.pro' website.",
            icon_url="https://shortcat.pro/favicon.png",
        )
        embed_msg.set_image(
            url=f"https://raw.githubusercontent.com/njayv/shortcat.pro/master/map_images/cup_location/{cup_selection}.png"
        )

        await ctx.respond(embed=embed_msg)

    @slash_command(
        name="help", description="Shows all commands and their descriptions."
    )
    async def help(
        self,
        ctx: ApplicationContext,
    ):
        embed_msg = discord.Embed(
            title="Help",
            description="This bot is a discord intergration of the ***shortcat.pro*** website. It can show you how to drive a track, how to abbreviate them, and more to come!",
            color=discord.Color.yellow(),
        )
        embed_msg.add_field(
            name="Commands",
            value=(
                "`/track_strategy` - Shows the strategy of a track.\n"
                "`/track_abbreviations` - Shows all tracks, their abbreviations, and where to find them.\n"
                "`/help` - Shows this help message."
            ),
        )
        embed_msg.set_footer(
            text="Images and descriptions taken from the 'shortcat.pro' website.",
            icon_url="https://shortcat.pro/favicon.png",
        )
        embed_msg.set_thumbnail(url="https://shortcat.pro/favicon.png")

        await ctx.respond(embed=embed_msg)

    # @slash_command(
    #     name="bullet_spots",
    #     description="!!!BROKEN!!! Shows the best positions to use the Bullet Bill.",
    # )
    # async def bullet_spots(
    #     self,
    #     ctx: ApplicationContext,
    #     track_selection=Option(
    #         name="track_name", description="Use Abbreviation of track!"
    #     ),
    # ):

    #     with open("./track_jsons/strategy.json", "r+") as f:
    #         strategies = json.load(f)
    #         picked_track = [
    #             entry
    #             for entry in strategies
    #             if entry["code"].lower() == track_selection.lower()
    #         ]
    #         if len(picked_track) == 0:
    #             return await ctx.respond(
    #                 "That's not a track! Try using the abbriviation of the track you'd like to see. Try using '/tracks' to see a list of tracks\n-# For example: MKS = Mario Kart Stadium, rMMM = Moo Moo Meadows (**r** meaning Retro Cup), dBP = Baby Park (**d** meaning DLC), bKC (**b** meaning Booster Course)"
    #             )
    #         picked_track = picked_track[0]

    #     data = range(1, 15)
    #     pagination_view = PaginationView()
    #     pagination_view.data = data

    #     await pagination_view.send(ctx)


def setup(bot: commands.Bot):
    bot.add_cog(testcmd(bot))
