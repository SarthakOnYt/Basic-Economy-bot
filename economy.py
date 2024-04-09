from TOKEN import token
from discord.ext import commands
import json
from discord.ext.commands.cooldowns import BucketType
import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.messages = True
intents.message_content = True



bot = commands.Bot(command_prefix='?',intents=intents)
bot_author = 525646987077615616
t = BucketType.user

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error,commands.CommandNotFound):
      pass
  if isinstance(error, commands.CommandOnCooldown):
    time = error.retry_after
    min, sec = divmod(time, 60)
    hour, min = divmod(min, 60)
    print (int(hour),"hr,", int(min),"min,", int(sec),"sec")
    await ctx.send(f'This command is actually on cooldown, you can use it in {int(hour),"hr", int(min),"min", int(sec),"sec"}.')

@bot.event
async def on_ready():
    print("im alive")

# economy commands
@bot.command()
@commands.cooldown(1, 1800, t)
async def work(message):
    
    with open ("blacklist.json","r") as ri:
        a = json.load(ri)
        for key in a :
            if key == str(message.author.id):
                if a[str(key)] == "blacklisted":
                    await message.reply("you have been banned from using this bot")
                    return
    auth = message.author.id
    str_auth = str(auth)
    with open ("money.json","r+") as ri:
        file_dat = json.load(ri)
            
        if str_auth in file_dat:
            await message.reply("you did your task perfectly here take $1000")
            file_dat[str_auth]["wallet"] = file_dat[str_auth]["wallet"] + 1000
                
            with open("money.json","w") as json_file:
                json.dump(file_dat,json_file)
                
        else:
            await message.channel.send("you have been registered, please type the command again.")
            file_dat[auth] = {
                "wallet":0
                ,"bank" :0
            }
            ri.seek(0)
            json.dump(file_dat,ri)

            with open ("blacklist.json","r+")as rb:
                file_da = json.load(rb)
                file_da[auth] = "whitelisted"
                rb.seek(0)
                json.dump(file_da,rb)

@bot.command()
async def bal(message):
    with open ("blacklist.json","r") as ri:
        a = json.load(ri)
        for key in a :
            if key == str(message.author.id):
                if a[str(key)] == "blacklisted":
                    await message.reply("you have been banned from using this bot")
                    return
    
    auth = message.author.id
    str_auth = str(auth)
    l1=[]
    for mentioned in message.message.mentions:
        l1.append(mentioned.id)
    if len(l1) == 1:

        a = str(l1[0])
        with open("money.json","r") as rbi:
            bal = json.load(rbi)
            embed = discord.Embed() #,color=Hex code
            embed.add_field(name="Wallet", value=f'${bal[a]["wallet"]}',inline= False)
            embed.add_field(name="Bank", value=f'${bal[a]["bank"]}/${bal[a]["bank_cap"]}',inline=False)
            await message.reply(embed=embed)
    
    elif len(l1) ==0:
        with open("money.json","r") as rbi:
            bal = json.load(rbi)
            embed = discord.Embed() #,color=Hex code
            embed.add_field(name="Wallet", value=f'${bal[str_auth]["wallet"]}',inline= False)
            embed.add_field(name="Bank", value=f'${bal[str_auth]["bank"]}/${bal[str_auth]["bank_cap"]}',inline=False)
            await message.reply(embed=embed)
    
    else:
        await message.reply("only one user allowed")

@bot.command()
@commands.cooldown(1, 3600, t)
async def rob(message):
        with open ("blacklist.json","r") as ri:
            a = json.load(ri)
        for key in a :
            if key == str(message.author.id):
                if a[str(key)] == "blacklisted":
                    await message.reply("you have been banned from using this bot")
                    return
        
        auth = message.author.id
        str_auth = str(auth)
        l1=[]
        for mentioned in message.message.mentions:
            l1.append(mentioned.id)
        
        if len(l1) == 1:

            robbed = str(l1[0])
            
            with open("money.json","r")as ri:
                data = json.load(ri)
            if data[robbed]["wallet"] >= 1000:
                print(robbed,"was robbed by",message.author.id)
                data[str_auth]["wallet"] = data[str_auth]["wallet"] + 1000
                data[robbed]["wallet"] = data[robbed]["wallet"] - 1000
                with open("money.json","w") as json_file:
                    json.dump(data,json_file)
                await message.reply("robbery sucessfull")
        
            else:
                await message.reply("the user u mentioned does not have atleast $1000")
        else:
            await message.reply("please mention only one user")

@bot.command()
@commands.cooldown(1, 86400, t)
async def daily(message):
    with open ("blacklist.json","r") as ri:
        a = json.load(ri)
        for key in a :
            if key == str(message.author.id):
                if a[str(key)] == "blacklisted":
                    await message.reply("you have been banned from using this bot")
                    return
    auth = message.author.id
    str_auth = str(auth)
    with open ("money.json","r+") as ri:
        file_dat = json.load(ri)
            
        if str_auth in file_dat:
            await message.reply("here is your daily reward $10000")
            file_dat[str_auth]["wallet"] = file_dat[str_auth]["wallet"] + 10000
                
            with open("money.json","w") as json_file:
                json.dump(file_dat,json_file)

@bot.command()
async def dep(message):
    with open ("blacklist.json","r") as ri:
        a = json.load(ri)
        for key in a :
            if key == str(message.author.id):
                if a[str(key)] == "blacklisted":
                    await message.reply("you have been banned from using this bot")
                    return

    message.message.content = message.message.content.replace("?dep ","")
    try: 
        message.message.content = int(message.message.content)
    except:
        pass
    auth = message.author.id
    str_auth = str(auth)
    with open("money.json","r") as ri:
        data = json.load(ri)
        ri.close()
    space_left = data[str_auth]["bank_cap"] - data[str_auth]["bank"]

    if type(message.message.content) == int:
        if message.message.content <= space_left:
            if message.message.content <= data[str_auth]["wallet"]:
                data[str_auth]["bank"] += message.message.content
                data[str_auth]["wallet"] -= message.message.content
                await message.reply("deposit sucessfull") 
                with open ("money.json","w") as fp:
                    json.dump(data,fp)
            else:
                await message.reply("you dont have enough money") 
        else:
            await message.reply("you dont have enough space")    
    
    elif type(message.message.content) == str:
        if message.message.content == "max":
            if space_left == 0:
                await message.reply("Bank is Full")

            elif data[str_auth]["wallet"] <= space_left:
                await message.reply(f'deposited ${data[str_auth]["wallet"]}')
                data[str_auth]["bank"] += data[str_auth]["wallet"]
                data[str_auth]["wallet"] -= data[str_auth]["wallet"]
                with open("money.json","w")as wi:
                    json.dump(data,wi)
                    wi.close()
                    

            elif data[str_auth]["wallet"] >= space_left:
                data[str_auth]["wallet"] -= space_left
                data[str_auth]["bank"] += space_left
                with open("money.json","w")as wi:
                    json.dump(data,wi)
                    await message.reply(f'deposited ${space_left}')
                    wi.close()

        else:
            await message.reply("please only use values like max and 1000 , empty spaces not allowed")
    else:
        await message.reply("please only use values like max and 1000 , decimal values not allowed")

@bot.command()
async def wth(message):
    with open ("blacklist.json","r") as ri:
        a = json.load(ri)
        for key in a :
            if key == str(message.author.id):
                if a[str(key)] == "blacklisted":
                    await message.reply("you have been banned from using this bot")
                    return

    message.message.content = message.message.content.replace("?wth ","")
    try: 
        message.message.content = int(message.message.content)
    except:
        pass
    auth = message.author.id
    str_auth = str(auth)
    with open("money.json","r") as ri:
        data = json.load(ri)
        ri.close()

    if type(message.message.content) == int:
        if message.message.content <= data[str_auth]["bank"]:
            data[str_auth]["wallet"] += message.message.content
            data[str_auth]["bank"] -= message.message.content
            await message.reply("withdraw sucessfull") 
            with open ("money.json","w") as fp:
                json.dump(data,fp)
        else:
            await message.reply("you dont have enough money in da bank")     
    
    elif type(message.message.content) == str:
        if message.message.content == "all":
                await message.reply(f'took ${data[str_auth]["bank"]} out of bank')
                data[str_auth]["wallet"] += data[str_auth]["bank"]
                data[str_auth]["bank"] -= data[str_auth]["bank"]
                with open("money.json","w")as wi:
                    json.dump(data,wi)
                    wi.close()

        else:
            await message.reply("please only use values like all and 1000 , empty spaces not allowed ")
    else:
        await message.reply("please only use values like all and 1000 , decimal values not allowed")

#dev commands
@bot.command()
async def blacklist(message):
    auth = message.author.id
    
    if auth == bot_author:
     for mentioned in message.message.mentions:
        with open ("blacklist.json","r") as bi:
            blk = json.load(bi)
            blk[str(mentioned.id)] = "blacklisted"
        
     with open("blacklist.json","w") as w:
        json.dump(blk,w)
     await message.reply("user has been blacklisted")
    
    else:
        await message.reply("this command is only for the bot developer")
        return
        
@bot.command()
async def whitelist(message):
    auth = message.author.id
    
    if auth == bot_author:
     for mentioned in message.message.mentions:
        with open ("blacklist.json","r") as bi:
            blk = json.load(bi)
            blk[str(mentioned.id)] = "whitelisted"
        
     with open("blacklist.json","w") as w:
        json.dump(blk,w)
     await message.reply("user has been whitelisted")
    
    else:
        await message.reply("this command is only for the bot developer")
        return

bot.run(token)