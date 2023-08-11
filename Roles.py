import discord

class Pronouns(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.value = None
    
    @discord.ui.button(label='He/Him', style=discord.ButtonStyle.green)
    async def he(self,interaction: discord.Interaction,  button: discord.ui.Button):
        self.value = 'He/Him'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        if discord.utils.get(interaction.guild.roles, name='She/Her') in interaction.user.roles:
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name='She/Her'))
        if discord.utils.get(interaction.guild.roles, name='They/Them') in interaction.user.roles:
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name='They/Them'))
        await interaction.message.delete()
        
        self.stop()
    
    @discord.ui.button(label='She/Her', style=discord.ButtonStyle.green)
    async def she(self,interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'She/Her'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        if discord.utils.get(interaction.guild.roles, name='He/Him') in interaction.user.roles:
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name='He/Him'))
        if discord.utils.get(interaction.guild.roles, name='They/Them') in interaction.user.roles:
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name='They/Them'))
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label='They/Them', style=discord.ButtonStyle.green)
    async def they(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'They/Them'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        if discord.utils.get(interaction.guild.roles, name='He/Him') in interaction.user.roles:
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name='He/Him'))
        if discord.utils.get(interaction.guild.roles, name='She/Her') in interaction.user.roles:
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name='She/Her'))
        await interaction.message.delete()
        self.stop()

class State(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.value = None
    
    @discord.ui.button(label="Andhra Pradesh", style=discord.ButtonStyle.green)
    async def andhra(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Andhra Pradesh'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="Arunachal Pradesh", style=discord.ButtonStyle.green)
    async def arunachal(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Arunachal Pradesh'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Assam", style=discord.ButtonStyle.green)
    async def assam(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Assam'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Bihar", style=discord.ButtonStyle.green)
    async def bihar(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Bihar'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="Chhattisgarh", style=discord.ButtonStyle.green)
    async def chhattisgarh(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Chhattisgarh'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="Goa", style=discord.ButtonStyle.green)
    async def goa(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Goa'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="Gujarat", style=discord.ButtonStyle.green)
    async def gujarat(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Gujarat'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="Haryana", style=discord.ButtonStyle.green)
    async def haryana(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Haryana'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="Himachal Pradesh", style=discord.ButtonStyle.green)
    async def himachal(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Himachal Pradesh'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Karnataka", style=discord.ButtonStyle.green)
    async def karnataka(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Karnataka'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="Kerala", style=discord.ButtonStyle.green)
    async def kerala(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Kerala'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Madhya Pradesh", style=discord.ButtonStyle.green)
    async def madhya(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Madhya Pradesh'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Maharashtra", style=discord.ButtonStyle.green)
    async def maharashtra(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Maharashtra'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete() 
        self.stop()
    
    @discord.ui.button(label="Manipur", style=discord.ButtonStyle.green)
    async def manipur(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Manipur'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete() 
        self.stop()
    
    @discord.ui.button(label="Meghalaya", style=discord.ButtonStyle.green)
    async def meghalaya(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Meghalaya'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete() 
        self.stop()
    
    @discord.ui.button(label="Mizoram", style=discord.ButtonStyle.green)
    async def mizoram(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Mizoram'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete() 
        self.stop()
    
    @discord.ui.button(label="Nagaland", style=discord.ButtonStyle.green)
    async def nagaland(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Nagaland'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete() 
        self.stop()
    
    @discord.ui.button(label="Odisha", style=discord.ButtonStyle.green)
    async def odisha(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Odisha'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete() 
        self.stop()

class State2(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.value = None
    @discord.ui.button(label="Punjab", style=discord.ButtonStyle.green)
    async def punjab(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Punjab'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete() 
        self.stop()
    
    @discord.ui.button(label="Rajasthan", style=discord.ButtonStyle.green)
    async def rajasthan(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Rajasthan'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete() 
        self.stop()
    
    @discord.ui.button(label="Sikkim", style=discord.ButtonStyle.green)
    async def sikkim(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Sikkim'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Tamil Nadu", style=discord.ButtonStyle.green)
    async def tamil(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Tamil Nadu'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Telangana", style=discord.ButtonStyle.green)
    async def telangana(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Telangana'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Tripura", style=discord.ButtonStyle.green)
    async def tripura(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Tripura'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Uttar Pradesh", style=discord.ButtonStyle.green)
    async def up(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Uttar Pradesh'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Uttarakhand", style=discord.ButtonStyle.green)
    async def uttarakhand(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Uttarakhand'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="West Bengal", style=discord.ButtonStyle.green)
    async def wb(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        self.value = 'West Bengal'
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="Andaman and Nicobar Islands", style=discord.ButtonStyle.green)
    async def an(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Andaman and Nicobar Islands'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles,name=self.value))
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Chandigarh", style=discord.ButtonStyle.green)
    async def ch(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Chandigarh'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles,name=self.value))
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Dadra and Nagar Haveli and Daman and Diu", style=discord.ButtonStyle.green)
    async def dd(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Dadra and Nagar Haveli and Daman and Diu'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles,name=self.value))
        await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="Delhi", style=discord.ButtonStyle.green)
    async def delhi(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Delhi'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles,name=self.value))
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Jammu and Kashmir", style=discord.ButtonStyle.green)
    async def jk(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Jammu and Kashmir'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles,name=self.value))
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Ladakh", style=discord.ButtonStyle.green)
    async def ladakh(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Ladakh'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles,name=self.value))
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Lakshadweep", style=discord.ButtonStyle.green)
    async def lakshadweep(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Lakshadweep'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles,name=self.value))
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="Puducherry", style=discord.ButtonStyle.green)
    async def puducherry(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Puducherry'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles,name=self.value))
        await interaction.message.delete()
        self.stop()

class Branch(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    
    @discord.ui.button(label="CSE", style=discord.ButtonStyle.green)
    async def cse(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'CSE'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="ECE", style=discord.ButtonStyle.green)
    async def ece(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'ECE'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
class Specialization(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    @discord.ui.button(label="CSE Core", style=discord.ButtonStyle.green)
    async def cse_core(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'CSE Core'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="CSE AI/ML", style=discord.ButtonStyle.green)
    async def cse_aiml(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'CSE AI/ML'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="CSE HCIG", style=discord.ButtonStyle.green)
    async def cse_hcig(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'CSE HCIG'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()

    @discord.ui.button(label="CSE DSA", style=discord.ButtonStyle.green)
    async def cse_dsa(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'CSE DSA'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="ECE Core", style=discord.ButtonStyle.green)
    async def ece_core(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'ECE Core'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value)) 
        await interaction.message.delete()
        self.stop()
    
    @discord.ui.button(label="ECE IOT", style=discord.ButtonStyle.green)
    async def ece_iot(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'ECE IOT'
        await interaction.response.send_message(f'You selected {self.value}', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name=self.value))
        await interaction.message.delete()
        self.stop()
