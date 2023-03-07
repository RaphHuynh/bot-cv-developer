import discord


def embed_resume(user_data):
    embed = discord.Embed(
        title="About me",
        color=discord.Colour.random()
    )
    embed.add_field(name="Firstname", value=user_data['firstname'])
    embed.add_field(name="Lastname", value=user_data['lastname'])
    embed.add_field(name="Portfolio", value=user_data['portfolio'], inline=False)
    embed.add_field(name="Github", value=user_data['github'])
    embed.add_field(name="Description", value=user_data['description'], inline=False)
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2115/2115958.png")
    embed.set_footer(text="By RaynhCoding", icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/2491ce53-2798-4444-9a7f-0c712febc209-profile_image-300x300.png")

    return embed
