import discord


def embed_education(user_data):
    embed = discord.Embed(
        title="My degree",
        color=discord.Colour.random()
    )
    if user_data['education'] is not None:
        embed.add_field(name="Degree", value=user_data['education']['degree'])
        embed.add_field(name="Institution", value=user_data['education']['institution'])
        embed.add_field(name="Date", value=user_data['education']['date'])
    else:
        embed.add_field(name="Degree", value=None)
        embed.add_field(name="Institution", value=None)
        embed.add_field(name="Date", value=None)
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2997/2997291.png")
    embed.set_footer(text="By RaynhCoding",
                     icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/2491ce53-2798-4444-9a7f-0c712febc209-profile_image-300x300.png")

    return embed
