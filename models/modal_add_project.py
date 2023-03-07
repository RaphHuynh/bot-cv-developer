import dataclasses
import json
import os

import discord
from dataclasses import dataclass
from .user import User
from .project import Project


@dataclass(init=False)
class ModalAddProject(discord.ui.Modal):
    def __init__(self, *, title: str = "Add a project") -> None:
        super().__init__(title=title)

        self.add_item(discord.ui.InputText(label="title of project"))
        self.add_item(discord.ui.InputText(label="A description for your project"))
        self.add_item(discord.ui.InputText(label="The Date of project", placeholder="20XX"))
        self.add_item(discord.ui.InputText(label="Skills", placeholder="HTML CSS REACT WORDPRESS ..."))

    async def callback(self, interaction: discord.Interaction):
        path = f"./json/{interaction.user.id}.json"
        try:
            file = open(path, "r")
        except FileNotFoundError:
            file = open(path, "w")

        if (os.path.getsize(path)) != 0:
            user_data = json.load(file)
            user = User(**user_data)
            setattr(user, 'project', Project(f"{self.children[0].value}", f"{self.children[1].value}", f"{self.children[2].value}",f"{self.children[3].value}"))
            file.close()
            file = open(path, "w")
            json.dump(dataclasses.asdict(user), file, indent=11)
            file.close()

        else:
            user = User(id_user=interaction.user.id,project=Project(f"{self.children[0].value}", f"{self.children[1].value}", f"{self.children[2].value}"))
            json_string = json.dumps(dataclasses.asdict(user), indent=11)
            file.write(json_string)
            file.close()

        await interaction.response.send_message("Finish")
