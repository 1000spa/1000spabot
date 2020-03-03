import discord
import datetime
import random
from captcha.image import ImageCaptcha
import tokeno as tk

now = datetime.datetime.now()
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("?!?help(DM) 아니면 ?!?help(CHANNEL)해보셈"))
    print('READY')

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == '?!?help(DM)':
        await message.channel.send('헬프치신분 DM 확인해주세요!')

        embed = discord.Embed(colour = discord.Colour.red())
        embed.set_author(name = "?!?help(DM)")
        embed.add_field(name = "프리픽스",value = "제 프리픽스는 '?!?'입니다 삐빅",inline=False)
        embed.add_field(name = "일반 명령어",value = "?!?help(DM), ?!?help(CHANNEL), ?!?천슾아유튜브, ?!?천슾아는?, ?!?지금시각, ?!?캡챠")
        await message.author.send(embed=embed)

    if message.content == '?!?help(CHANNEL)':
        embed = discord.Embed(colour = discord.Colour.red())
        embed.set_author(name = "?!?help(CHANNEL)")
        embed.add_field(name = "프리픽스",value = "제 프리픽스는 '?!?'입니다 삐빅",inline=False)
        embed.add_field(name = "일반 명령어",value = "?!?help(DM), ?!?help(CHANNEL), ?!?천슾아유튜브, ?!?천슾아는?, ?!?캡챠")
        await message.channel.send(embed=embed)
    
    if message.content == '?!?천슾아유튜브':
        await message.channel.send('천슾아유튜브 링크입니다 삐빅\nhttps://www.youtube.com/channel/UC8F-M2wolcAIisN55gwrwrw')

    if message.content == '?!?천슾아는?':
        await message.channel.send('음......')
        await message.channel.send('일단 착함\nㅇㅈ?')
    
    if message.content == 'ㅇㅈ':
        await message.channel.send('ㅇㅇ')

    if message.content == '인정':
        await message.channel.send('ㅇㅇ')
    
    if message.content == '노인정':
        await message.channel.send('그래?')

    if message.content == 'ㄴㅇㅈ':
        await message.channel.send('그래?')
    
    if message.content == '노ㅇㅈ':
        await message.channel.send('그래?')
    
    if message.content == 'ㄴ인정':
        await message.channel.send('그래?')

    if message.content == '?!?캡챠':
        Image_captcha = ImageCaptcha()
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send('시간초과입니다 삐빅')
            return
        if msg.content == a:
            await message.channel.send('정답입니다 삐빅')
        else:
            await message.channel.send('오답입니다 삐빅')

client.run(tk.tok)