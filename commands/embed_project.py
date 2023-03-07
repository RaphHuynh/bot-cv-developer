import discord


def embed_project(user_data):
    embed = discord.Embed(
        title="My project",
        color=discord.Colour.random()
    )
    if user_data['project'] is not None:
        embed.add_field(name="Title", value=user_data['project']['title'])
        embed.add_field(name="Date", value=user_data['project']['date'])
        embed.add_field(name="Description", value=user_data['project']['description'], inline=False)
        embed.add_field(name="Skill", value=user_data['project']['skill'])
    else:
        embed.add_field(name="Title", value=None)
        embed.add_field(name="Date", value=None)
        embed.add_field(name="Description", value=None)
        embed.add_field(name="Skill", value=None)

    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4365/4365945.png")
    embed.set_footer(text="By RaynhCoding",
                     icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/2491ce53-2798-4444-9a7f-0c712febc209-profile_image-300x300.png")

    return embed
