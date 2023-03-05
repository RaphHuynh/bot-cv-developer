import discord
from dataclasses import dataclass


@dataclass(init=False)
class ModalAddDeveloperExperience(discord.ui.Modal):
    job: str
    date: str
    employer: str
    description: str
    skill: str

    def __init__(self, *, title: str = "Add your job") -> None:
        super().__init__(title=title)

        self.add_item(discord.ui.InputText(label="Your job"))
        self.add_item(discord.ui.InputText(label="The date", placeholder="20XX-20XX"))
        self.add_item(discord.ui.InputText(label="The employer", placeholder="Microsoft"))
        self.add_item(discord.ui.InputText(label="A description", style=discord.InputTextStyle.long))
        self.add_item(discord.ui.InputText(label="The skill of your job", style=discord.InputTextStyle.long, placeholder="React, JavaScript, Nuxt.js Tailwind CSS ..."))

    async def callback(self, interaction: discord.Interaction):
        print(f"{interaction.user.id} + {self.children[0].value} + {self.children[1].value} + {self.children[2].value} + {self.children[3].value} + {self.children[4].value}")

        await interaction.response.send_message("Finish")