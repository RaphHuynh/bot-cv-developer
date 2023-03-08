import discord
from .embed_resume import embed_resume
from .embed_skill import embed_skill
from .embed_project import embed_project
from .embed_education import embed_education
from .embed_dev_exp import embed_dev_exp


class SelectionMenuResume(discord.ui.Select):
    def __init__(self, user_data):
        self.user_data = user_data
        super().__init__(
            placeholder="Choose what you want to see",
            options=[
                discord.SelectOption(
                    label="Resume", emoji="👤", value="resume"
                ),
                discord.SelectOption(
                    label="Skill", emoji="💪", value="skill"
                ),
                discord.SelectOption(
                    label="Experience", emoji="💼", value="developerExperience"
                ),
                discord.SelectOption(
                    label="Project", emoji="📂", value="project"
                ),
                discord.SelectOption(
                    label="Degree", emoji="🎓", value="education"
                )
            ],
            min_values=1,
            max_values=1
        )

    async def callback(self, interaction):
        embed = None
        match self.values[0]:
            case "resume":
                embed = embed_resume(self.user_data)
            case "skill":
                embed = embed_skill(self.user_data)
            case "education":
                embed = embed_education(self.user_data)
            case "project":
                embed = embed_project(self.user_data)
            case "developerExperience":
                embed = embed_dev_exp(self.user_data)
        view = discord.ui.View()
        view.add_item(SelectionMenuResume(self.user_data))
        await interaction.response.edit_message(
            embed=embed, view=view
        )
