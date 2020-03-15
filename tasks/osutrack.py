import discord, asyncio
from discord.ext import commands

class OsuTrack(commands.Cog):
    """osu! Tracking Background Task."""
    def __init__(self, bot):
        self.bot = bot
        self.task = self.bot.loop.create_task(self.trackCheck())

    async def trackCheck(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            # Tracking code goes here

            await asyncio.sleep(600) # Check every 10 minutes

def setup(bot):
    bot.add_cog(OsuTrack(bot))
