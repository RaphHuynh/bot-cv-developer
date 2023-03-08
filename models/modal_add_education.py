import dataclasses
import os.path
import json

import discord
from dataclasses import dataclass
from .user import User
from .education import Education


@dataclass(init=False)
class ModalAddEducation(discord.ui.Modal):
    degree: str
    institution: str
    date: str

    def __init__(self, *, title: str = "Add your degree") -> None:
        super().__init__(title=title)

        self.add_item(discord.ui.InputText(label="Your degree"))
        self.add_item(discord.ui.InputText(label="Your institution"))
        self.add_item(discord.ui.InputText(label="Date", placeholder="20XX-20XX"))

    async def callback(self, interaction: discord.Interaction):
        path = f"./data/user/{interaction.user.id}.json"
        try:
            file = open(path, "r")
        except FileNotFoundError:
            file = open(path, "w")

        if (os.path.getsize(path)) != 0:
            user_data = json.load(file)
            user = User(**user_data)
            setattr(user, 'education', Education(self.children[0].value, self.children[1].value, self.children[2].value))
            file.close()
            file = open(path, "w")
            json.dump(dataclasses.asdict(user), file, indent=11)
            file.close()
        else:
            user = User(id_user=interaction.user.id, education=Education(self.children[0].value, self.children[1].value, self.children[2].value))
            json_string = json.dumps(dataclasses.asdict(user), indent=11)
            file.write(json_string)
            file.close()

        await interaction.response.send_message("Finish")
