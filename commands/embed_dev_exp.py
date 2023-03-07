import discord


def embed_dev_exp(user_data):
    embed = discord.Embed(
        title="My Experience",
        color=discord.Colour.random()
    )
    if user_data['developerExperience'] is not None:
        embed.add_field(name="Job", value=user_data['developerExperience']['job'], inline=False)
        embed.add_field(name="Date", value=user_data['developerExperience']['date'])
        embed.add_field(name="Employer", value=user_data['developerExperience']['employer'])
        embed.add_field(name="Description", value=user_data['developerExperience']['description'], inline=False)
        embed.add_field(name="Skills", value=user_data['developerExperience']['skill'])
    else:
        embed.add_field(name="Job", value=None)
        embed.add_field(name="Date", value=None)
        embed.add_field(name="Employer", value=None)
        embed.add_field(name="Description", value=None)
        embed.add_field(name="Skills", value=None)
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3281/3281307.png")
    embed.set_footer(text="By RaynhCoding",
                     icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/2491ce53-2798-4444-9a7f-0c712febc209-profile_image-300x300.png")

    return embed