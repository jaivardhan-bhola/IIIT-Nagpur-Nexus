import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from Roles import Pronouns, State, State2, Branch, Specialization, Batch
load_dotenv()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='>', intents=discord.Intents.all())
    
    async def on_ready(self):
        print('Logged in as ' + self.user.name)

bot = Bot()

@bot.command()


async def r(ctx):
    view_pronouns = Pronouns()
    await ctx.send('Please select your pronouns', view=view_pronouns)
    await view_pronouns.wait()
    view_state = State()
    await ctx.send('Please select your state', view=view_state, delete_after=20)
    view_state2 = State2()
    await ctx.send(view=view_state2, delete_after=20)
    view_branch = Branch()
    await ctx.send('Please select your Branch',view=view_branch)
    await view_branch.wait()
    view_specialization = Specialization()
    await ctx.send('Please select your Specialization',view=view_specialization)
    await view_specialization.wait()
    view_batch = Batch()
    await ctx.send('Please select your Batch',view=view_batch)
    await view_batch.wait()
    message = await ctx.fetch_message(ctx.message.id)
    await message.delete()

bot.run(os.getenv('TOKEN'))