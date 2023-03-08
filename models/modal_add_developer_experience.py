import dataclasses

import discord
import os
import json
from dataclasses import dataclass
from .user import User
from .developer_experience import DeveloperExperience


@dataclass(init=False)
class ModalAddDeveloperExperience(discord.ui.Modal):

    def __init__(self, *, title: str = "Add your job") -> None:
        super().__init__(title=title)

        self.add_item(discord.ui.InputText(label="Your job"))
        self.add_item(discord.ui.InputText(label="The date", placeholder="20XX-20XX"))
        self.add_item(discord.ui.InputText(label="The employer", placeholder="Microsoft"))
        self.add_item(discord.ui.InputText(label="A description"))
        self.add_item(discord.ui.InputText(label="The skill of your job", placeholder="React, JavaScript, Nuxt.js Tailwind CSS ..."))

    async def callback(self, interaction: discord.Interaction):
        path = f"./data/user/{interaction.user.id}.json"
        try:
            file = open(path, "r")
        except FileNotFoundError:
            file = open(path, "w")

        if (os.path.getsize(path)) != 0:
            user_data = json.load(file)
            user = User(**user_data)
            setattr(user, 'developerExperience', DeveloperExperience(self.children[0].value, self.children[1].value, self.children[2].value, self.children[3].value, self.children[4].value))
            file.close()
            file = open(path, "w")
            json.dump(dataclasses.asdict(user), file, indent=11)
            file.close()
        else:
            user = User(id_user=interaction.user.id, developerExperience=DeveloperExperience(self.children[0].value, self.children[1].value, self.children[2].value, self.children[3].value, self.children[4].value))
            json_string = json.dumps(dataclasses.asdict(user), indent=11)
            file.write(json_string)
            file.close()

        await interaction.response.send_message("The form it's validate")
