import discord
from discord.ext import commands
from commands.invite_rewards import InviteRewardsCommand
import config

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_member_join(member):
    # Aquí puedes manejar la lógica para cuando un nuevo miembro se une
    pass

@bot.event
async def on_member_remove(member):
    # Aquí puedes manejar la lógica para cuando un miembro se va
    pass

# Cargar comandos
bot.add_cog(InviteRewardsCommand(bot))

# Iniciar el bot
bot.run(config.TOKEN)