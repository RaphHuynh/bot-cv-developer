import discord
from dataclasses import dataclass
from project.models import Skill


@dataclass(init=False)
class ModalAddSkill(discord.ui.Modal):
    skills: Skill

    def __init__(self, *, title: str = "Add your Skills") -> None:
        super().__init__(title=title)

        self.add_item(discord.ui.InputText(label="Your programming language", style=discord.InputTextStyle.long, placeholder="Python, CSS ..."))
        self.add_item(discord.ui.InputText(label="Your framework/cms and libraries", style=discord.InputTextStyle.long, placeholder="Django, Svelte ..."))
        self.add_item(discord.ui.InputText(label="Your tools", style=discord.InputTextStyle.long, placeholder="Figma, Postman ..."))
        self.add_item(discord.ui.InputText(label="Your system", style=discord.InputTextStyle.long, placeholder="MACOS, Linux, Debian ..."))

    async def callback(self, interaction: discord.Interaction):
        print(f"{interaction.user.id} + {self.children[0].value} + {self.children[1].value} + {self.children[2].value}")
        print(f"{self.children[3].value}")
        await interaction.response.send_message("Hello")