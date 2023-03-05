import discord
from dataclasses import dataclass


@dataclass(init=False)
class ModalCreateResume(discord.ui.Modal):
    lastname: str
    firstname: str
    portfolio: str
    github: str
    description: str
    # skills: Skill = field(default=None)
    # project: Project = field(default=None)
    # developer_experience: DeveloperExperience = field(default=None)
    # education: Education = field(default=None)

    def __init__(self, *, title: str = "Create your resume") -> None:
        super().__init__(title=title)

        self.add_item(discord.ui.InputText(label="Your lastname"))
        self.add_item(discord.ui.InputText(label="Your firstname"))
        self.add_item(discord.ui.InputText(label="Link of your portfolio"))
        self.add_item(discord.ui.InputText(label="Link of your github"))
        self.add_item(discord.ui.InputText(label="A little description", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        print(f"{interaction.user.id} + {self.children[0].value} + {self.children[1].value} + {self.children[2].value}")
        print(f"{self.children[3].value} + {self.children[4].value}")
        await interaction.response.send_message("Fini")
