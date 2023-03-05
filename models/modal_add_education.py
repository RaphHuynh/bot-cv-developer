import discord
from dataclasses import dataclass


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
        print(f"{interaction.user.id} + {self.children[0].value} + {self.children[1].value} + {self.children[2].value}")

        await interaction.response.send_message("Finish")
