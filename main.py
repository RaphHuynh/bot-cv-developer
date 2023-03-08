import discord
import json
import models.modal_create_resume as mcr
import models.modal_add_skill as mas
import models.modal_add_education as mae
import models.modal_add_developer_experience as made
import models.modal_add_project as map
import commands.selection_menu_resume as slmr
from discord.ext.pages import Paginator, Page
from commands.embed_resume import embed_resume
from commands.embed_skill import embed_skill
from commands.embed_dev_exp import embed_dev_exp
from commands.embed_project import embed_project
from commands.embed_education import embed_education
from commands.generate_pdf import generate_pdf
from config import *


bot = discord.Bot(debug_guilds=[827506827616714782,1040767558573371392])


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
    name="view-cv-paginator",
    description="View someone's resume with a system of paginator."
)
async def view_cv_paginator(ctx, member: discord.Member):
    try:
        path = f"./data/user/{member.id}.json"
        file = open(path, "r")
        user_data = json.load(file)
        pages = [
            Page(embeds=[embed_resume(user_data)]),
            Page(embeds=[embed_skill(user_data)]),
            Page(embeds=[embed_dev_exp(user_data)]),
            Page(embeds=[embed_project(user_data)]),
            Page(embeds=[embed_education(user_data)])
        ]
        paginator = Paginator(pages=pages, author_check=True)
        file.close()

        await paginator.respond(ctx.interaction)

    except FileNotFoundError:
        await ctx.respond("This people doesn't have a resume.")


@bot.slash_command(
    name="view-cv-menu",
    descrption="View someone's resume with a system of menu."
)
async def view_cv_menu(ctx, member: discord.Member):
    try:
        path = f"./data/user/{member.id}.json"
        file = open(path, "r")
        user_data = json.load(file)
        embed = embed_resume(user_data)
        view = discord.ui.View(timeout=120)
        view.add_item(slmr.SelectionMenuResume(user_data))

        await ctx.respond(embed=embed, view=view, ephemeral=True)

    except FileNotFoundError:
        await ctx.respond("This people doesn't have a resume.")


@bot.slash_command(
    name="generate-resume",
    description="generate a resume PDF"
)
async def generate_command(ctx, member: discord.Member):
    try:
        path = f"./data/user/{member.id}.json"
        file = open(path, "r")
        user_data = json.load(file)
        icon = member.avatar
        if user_data['lastname'] and user_data['skill'] and user_data['project'] and user_data['education'] and user_data['developerExperience']:
            generate_pdf(user_data)
            await ctx.respond("PDF generate")
        else:
            await ctx.respond("The person did not complete their resume in full.")
    except FileNotFoundError:
        await ctx.respond("This people doesn't have a resume.")

bot.run(TOKEN)
