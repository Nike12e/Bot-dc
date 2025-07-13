import discord
from discord.ext import commands
from discord.ui import Button, View
import json
import os

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

DATA_FILE = "invites_data.json"

def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("user_invites", {}), data.get("user_claimed", {})
    return {}, {}

def guardar_datos():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"user_invites": user_invites, "user_claimed": user_claimed}, f)

user_invites, user_claimed = cargar_datos()

PREMIOS = [
    (1, "🎁 Premio por 1 invitación: Rol Invitador"),
    (2, "🎉 Premio por 2 invitaciones: Acceso a canal especial"),
    (5, "🏆 Premio por 5 invitaciones: Rol VIP"),
    (10, "👑 Premio por 10 invitaciones: Rol Leyenda + Sorpresa"),
]

def obtener_premio(invites):
    premio = None
    for req, desc in reversed(PREMIOS):
        if invites >= req:
            premio = desc
            break
    return premio

@bot.event
async def on_ready():
    print("="*40)
    print(f"✅ El bot está encendido como {bot.user}")
    print(f"🟢 Conectado a {len(bot.guilds)} servidores.")
    print("="*40)
    await bot.change_presence(activity=discord.Game(name="Creador !Nike"))

@bot.event
async def on_member_join(member):
    # Detectar invitaciones usadas
    guild = member.guild
    invites_antes = await guild.invites()
    await discord.utils.sleep_until(discord.utils.utcnow() + discord.utils.timedelta(seconds=2))
    invites_despues = await guild.invites()
    for invite in invites_despues:
        for old_invite in invites_antes:
            if invite.code == old_invite.code and invite.uses > old_invite.uses:
                if invite.inviter:
                    user_id = invite.inviter.id
                    user_invites[str(user_id)] = user_invites.get(str(user_id), 0) + 1
                    guardar_datos()
                break

@bot.command(name="misinvitaciones")
async def mis_invitaciones(ctx):
    user_id = str(ctx.author.id)
    invites = user_invites.get(user_id, 0)
    claimed = user_claimed.get(user_id, False)

    embed = discord.Embed(
        title="🎊 Premios por Invitaciones",
        description=f"Tienes **{invites}** invitaciones.\n\nPremios disponibles:",
        color=discord.Color.blue()
    )
    for req, desc in PREMIOS:
        embed.add_field(
            name=f"{req} invitación{'es' if req > 1 else ''}",
            value=desc,
            inline=False
        )

    premio_actual = obtener_premio(invites)
    if invites >= 1 and not claimed and premio_actual:
        button = Button(label="Reclamar premio", style=discord.ButtonStyle.green)

        async def button_callback(interaction):
            user_claimed[user_id] = True
            guardar_datos()
            await interaction.response.edit_message(
                content="¡Reclamaste tu premio! 🎉",
                embed=None,
                view=None
            )

        button.callback = button_callback
        view = View()
        view.add_item(button)
        await ctx.send(embed=embed, view=view)
    elif claimed:
        await ctx.send("Ya reclamaste tu premio.")
    else:
        await ctx.send(embed=embed)

@bot.command(name="sumarinvitacion")
@commands.has_permissions(administrator=True)
async def sumar_invitacion(ctx, miembro: discord.Member):
    user_id = str(miembro.id)
    user_invites[user_id] = user_invites.get(user_id, 0) + 1
    guardar_datos()
    await ctx.send(f"Ahora {miembro.mention} tiene {user_invites[user_id]} invitaciones.")

@bot.command(name="cleaninvitaciones")
@commands.has_permissions(administrator=True)
async def clean_invitaciones(ctx, miembro: discord.Member):
    user_id = str(miembro.id)
    user_invites[user_id] = 0
    user_claimed[user_id] = False
    guardar_datos()
    await ctx.send(f"Las invitaciones de {miembro.mention} han sido borradas.")

# Reemplaza 'TU_TOKEN_AQUI' por el token de tu bot
bot.run('MTM5Mzc5MzY0NjA3NTA1MjA4Mw.GuHyTO.SkHEO4bgyeZBzLSJSgMYf0PEZdWrc6riJkEKgM')