import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user}')

@bot.command()
async def setup(ctx):
    if ctx.message.author.guild_permissions.administrator:
        # Check if the channel already exists
        existing_channel = discord.utils.get(ctx.guild.channels, name='💬-command-unit')
        
        if existing_channel:
            embed = discord.Embed(
                title='Error',
                description='💬-command-unit channel already exists.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        else:
            # Create the channel
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False)
            }
            channel = await ctx.guild.create_text_channel('💬-command-unit', overwrites=overwrites)
            
            embed = discord.Embed(
                title='Success',
                description='💬-command-unit channel has been created.',
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title='Error',
            description='You need to be an administrator to run this command.',
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

bot.run('MTE2NTk3ODQwMjUxNjM3MzUwNA.GImzim.qleajfEYkgxJjl-P8tXA_Xu1Y_TT-MGxaBu_6I')
