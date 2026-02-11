import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Bot configuration - Using environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
API_BASE_URL = os.getenv('API_BASE_URL', 'https://long-bio-dusky.vercel.app/')  

print(f"Configuration loaded:")
print(f"- API Base URL: {API_BASE_URL}")

# Initialize bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is ready! Available commands: !bio, !bio_jwt, !bio_access, !help')

@bot.command(name='bio')
async def set_bio(ctx, uid: str, password: str, *, bio_text: str):
    """Set Free Fire bio using UID and password"""
    try:
        # Prepare the API request
        api_url = f"{API_BASE_URL}/bio_upload"
        params = {
            'bio': bio_text,
            'uid': uid,
            'pass': password
        }

        # Make the API call
        response = requests.post(api_url, data=params, timeout=30)
        result = response.json()

        # Create response embed
        embed = discord.Embed(title="✅ Bio Update Result", color=0x00ff00)
        embed.add_field(name="Status", value=result.get("status", "Unknown"), inline=False)
        embed.add_field(name="Bio Text", value=result.get("bio", "N/A"), inline=False)
        
        if result.get("name"):
            embed.add_field(name="Name", value=result.get("name"), inline=True)
        if result.get("region"):
            embed.add_field(name="Region", value=result.get("region"), inline=True)
        if result.get("uid"):
            embed.add_field(name="UID", value=result.get("uid"), inline=True)
        
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
        
    except requests.exceptions.ConnectionError:
        error_embed = discord.Embed(title="❌ Connection Error", 
                                  description=f"Cannot connect to API at {API_BASE_URL}", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)
    except requests.exceptions.Timeout:
        error_embed = discord.Embed(title="⏰ Timeout Error", 
                                  description=f"API request timed out", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)
    except ValueError:  # JSON decode error
        error_embed = discord.Embed(title="❌ Response Error", 
                                  description=f"API returned invalid response", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)
    except Exception as e:
        error_embed = discord.Embed(title="❌ Error", 
                                  description=f"An error occurred: {str(e)}", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)

@bot.command(name='bio_jwt')
async def set_bio_jwt(ctx, jwt: str, *, bio_text: str):
    """Set Free Fire bio using JWT token"""
    try:
        # Prepare the API request
        api_url = f"{API_BASE_URL}/bio_upload"
        params = {
            'bio': bio_text,
            'jwt': jwt
        }

        # Make the API call
        response = requests.post(api_url, data=params, timeout=30)
        result = response.json()

        # Create response embed
        embed = discord.Embed(title="✅ Bio Update Result (JWT)", color=0x00ff00)
        embed.add_field(name="Status", value=result.get("status", "Unknown"), inline=False)
        embed.add_field(name="Bio Text", value=result.get("bio", "N/A"), inline=False)
        
        if result.get("name"):
            embed.add_field(name="Name", value=result.get("name"), inline=True)
        if result.get("region"):
            embed.add_field(name="Region", value=result.get("region"), inline=True)
        if result.get("uid"):
            embed.add_field(name="UID", value=result.get("uid"), inline=True)
        
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
        
    except requests.exceptions.ConnectionError:
        error_embed = discord.Embed(title="❌ Connection Error", 
                                  description=f"Cannot connect to API at {API_BASE_URL}", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)
    except requests.exceptions.Timeout:
        error_embed = discord.Embed(title="⏰ Timeout Error", 
                                  description=f"API request timed out", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)
    except ValueError:  # JSON decode error
        error_embed = discord.Embed(title="❌ Response Error", 
                                  description=f"API returned invalid response", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)
    except Exception as e:
        error_embed = discord.Embed(title="❌ Error", 
                                  description=f"An error occurred: {str(e)}", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)

@bot.command(name='bio_access')
async def set_bio_access(ctx, access_token: str, *, bio_text: str):
    """Set Free Fire bio using access token"""
    try:
        # Prepare the API request
        api_url = f"{API_BASE_URL}/bio_upload"
        params = {
            'bio': bio_text,
            'access': access_token
        }

        # Make the API call
        response = requests.post(api_url, data=params, timeout=30)
        result = response.json()

        # Create response embed
        embed = discord.Embed(title="✅ Bio Update Result (Access Token)", color=0x00ff00)
        embed.add_field(name="Status", value=result.get("status", "Unknown"), inline=False)
        embed.add_field(name="Bio Text", value=result.get("bio", "N/A"), inline=False)
        
        if result.get("name"):
            embed.add_field(name="Name", value=result.get("name"), inline=True)
        if result.get("region"):
            embed.add_field(name="Region", value=result.get("region"), inline=True)
        if result.get("uid"):
            embed.add_field(name="UID", value=result.get("uid"), inline=True)
        
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
        
    except requests.exceptions.ConnectionError:
        error_embed = discord.Embed(title="❌ Connection Error", 
                                  description=f"Cannot connect to API at {API_BASE_URL}", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)
    except requests.exceptions.Timeout:
        error_embed = discord.Embed(title="⏰ Timeout Error", 
                                  description=f"API request timed out", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)
    except ValueError:  # JSON decode error
        error_embed = discord.Embed(title="❌ Response Error", 
                                  description=f"API returned invalid response", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)
    except Exception as e:
        error_embed = discord.Embed(title="❌ Error", 
                                  description=f"An error occurred: {str(e)}", 
                                  color=0xff0000)
        await ctx.send(embed=error_embed)

@bot.command(name='help_ff')
async def help_ff_command(ctx):
    """Show help information"""
    embed = discord.Embed(title="🤖 Free Fire Bio Bot Help", color=0x00ffff)
    embed.add_field(
        name="!bio <uid> <password> <bio_text>", 
        value="Update bio using UID and password", 
        inline=False
    )
    embed.add_field(
        name="!bio_jwt <jwt_token> <bio_text>", 
        value="Update bio using JWT token", 
        inline=False
    )
    embed.add_field(
        name="!bio_access <access_token> <bio_text>", 
        value="Update bio using access token", 
        inline=False
    )
    embed.add_field(
        name="!help_ff", 
        value="Show this help message", 
        inline=False
    )
    embed.set_footer(text="Free Fire Bio Bot")
    await ctx.send(embed=embed)

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)