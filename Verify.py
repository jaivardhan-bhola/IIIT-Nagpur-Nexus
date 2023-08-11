import discord

class Verification(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
    
    @discord.ui.button(emoji='✅', style=discord.ButtonStyle.green)
    async def verify(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = True
        await interaction.response.send_message('Verified!', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name='Member'))
        self.stop()