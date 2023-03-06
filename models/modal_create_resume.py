import dataclasses
import json
import discord
import os
from dataclasses import dataclass, field
from .user import User


@dataclass(init=False)
class ModalCreateResume(discord.ui.Modal):

    def __init__(self, *, title: str = "Create your resume") -> None:
        super().__init__(title=title)

        self.add_item(discord.ui.InputText(label="Your lastname"))
        self.add_item(discord.ui.InputText(label="Your firstname"))
        self.add_item(discord.ui.InputText(label="Link of your portfolio"))
        self.add_item(discord.ui.InputText(label="Link of your github"))
        self.add_item(discord.ui.InputText(label="A little description", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        path = f"./json/{interaction.user.id}.json"
        try:
            file = open(path, "r")
        except FileNotFoundError:
            file = open(path, "w")

        if (os.path.getsize(path)) != 0:
            file.close()
            file = open(path, "r")
            user_data = json.load(file)
            print(user_data)
            user = User(**user_data)
            setattr(user, 'lastname', f"{self.children[0].value}")
            setattr(user, 'firstname', f"{self.children[1].value}")
            setattr(user, 'portfolio', f"{self.children[2].value}")
            setattr(user, 'github', f"{self.children[3].value}")
            setattr(user, 'description', f"{self.children[4].value}")
            file.close()
            file = open(path, "w")
            json.dump(dataclasses.asdict(user), file, indent=11)
            file.close()

        else:
            user = User(interaction.user.id, f"{self.children[0].value}", f"{self.children[1].value}", f"{self.children[2].value}", f"{self.children[3].value}", f"{self.children[4].value}")
            json_string = json.dumps(dataclasses.asdict(user), indent=11)
            file.write(json_string)
            file.close()

        await interaction.response.send_message("The form it's validate")
