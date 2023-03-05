import discord
from dataclasses import dataclass


@dataclass(init=False)
class ModalAddProject(discord.ui.Modal):
    title: str
    description: str
    skill: str

    def __init__(self, *, title: str = "Add a project") -> None:
        super().__init__(title=title)

        self.add_item(discord.ui.InputText(label="title of project"))
        self.add_item(discord.ui.InputText(label="A description for your project", style=discord.InputTextStyle.long))
        self.add_item(discord.ui.InputText(label="Skills", placeholder="HTML CSS REACT WORDPRESS ...", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        print(f"{interaction.user.id} + {self.children[0].value} + {self.children[1].value} + {self.children[2].value}")

        await interaction.response.send_message("Finish")
