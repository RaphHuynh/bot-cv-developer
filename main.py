import discord
import json
import models.modal_create_resume as mcr
import models.modal_add_skill as mas
import models.modal_add_education as mae
import models.modal_add_developer_experience as made
import models.modal_add_project as map
from commands.embed_resume import embed_resume
from commands.embed_skill import embed_skill
from commands.embed_dev_exp import embed_dev_exp
from commands.embed_project import embed_project
from commands.embed_education import embed_education
from config import *


bot = discord.Bot(debug_guilds=[827506827616714782])


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(
    name="command",
    description="list of commands"
)
async def command(ctx):
    embed = discord.Embed(
        title="Commands",
        description="All of the bot's commands.",
        color=discord.Colour.random()
    )
    embed.add_field(name="/register", value="Create a new resume.", inline=False)
    embed.add_field(name="/edit", value="Edit your own resume.", inline=False)
    embed.add_field(name="/view-cv", value="View someone's resume.", inline=False)
    embed.add_field(name="/generate-cv", value="Generate someone's resume as a PDF.", inline=False)
    embed.set_footer(text="By RaynhCoding")

    await ctx.respond(embed=embed)


@bot.slash_command(
    name="register",
    description="Create a new resume"
)
async def register(ctx):
    await ctx.send_modal(mcr.ModalCreateResume())


@bot.slash_command(
    name="add-skills",
    description="Add your Skills"
)
async def add_skill(ctx):
    await ctx.send_modal(mas.ModalAddSkill())


@bot.slash_command(
    name="add-education",
    descrption="Add your degree"
)
async def add_education(ctx):
    await ctx.send_modal(mae.ModalAddEducation())


@bot.slash_command(
    name="add-developer-experience",
    description="Add your a experience"
)
async def add_developer_experience(ctx):
    await ctx.send_modal(made.ModalAddDeveloperExperience())


@bot.slash_command(
    name="add-project",
    description="Add your a project"
)
async def add_project(ctx):
    await ctx.send_modal(map.ModalAddProject())


@bot.slash_command(
    name="view-cv",
    description="View someone's resume."
)
async def view_cv(ctx, member: discord.Member):
    try:
        embed = discord.Embed(
            title="My Resume",
            color=discord.Colour.random()
        )
        path = f"./json/{member.id}.json"
        file = open(path, "r")
        user_data = json.load(file)
        embed_r = embed_resume(user_data)
        embed_d_e = embed_dev_exp(user_data)
        embed_p = embed_project(user_data)
        embed_s = embed_skill(user_data)
        embed_e = embed_education(user_data)
        file.close()
        await ctx.respond(embed=embed_r)
        await ctx.respond(embed=embed_d_e)
        await ctx.respond(embed=embed_p)
        await ctx.respond(embed=embed_s)
        await ctx.respond(embed=embed_e)
    except FileNotFoundError:
        await ctx.respond("This people doesn't have a resume.")


bot.run(TOKEN)
