import discord


def embed_skill(user_data):
    embed = discord.Embed(
        title="My Skills",
        color=discord.Colour.random()
    )
    if user_data['skill'] is not None:
        embed.add_field(name="Languages", value=user_data['skill']['language'], inline=False)
        embed.add_field(name="Frameworks", value=user_data['skill']['framework'], inline=False)
        embed.add_field(name="Tools", value=user_data['skill']['tools'], inline=False)
        embed.add_field(name="System", value=user_data['skill']['system'])
    else:
        embed.add_field(name="Languages", value=None)
        embed.add_field(name="Frameworks", value=None)
        embed.add_field(name="Tools", value=None)
        embed.add_field(name="System", value=None)
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/8347/8347446.png")
    embed.set_footer(text="By RaynhCoding",
                     icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/2491ce53-2798-4444-9a7f-0c712febc209-profile_image-300x300.png")

    return embed
