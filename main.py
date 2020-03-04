import discord
import datetime
import random
from captcha.image import ImageCaptcha
import tokeno as tk

now = datetime.datetime.now()
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("?!?help해보셈"))
    print('READY')

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == '?!?help':
        await message.channel.send("'?!?help(DM)'이나 '?!?help(CHANNEL)'을 사용해야합니다!")

    if message.content == '?!?help(DM)':
        await message.channel.send('헬프치신분 DM 확인해주세요!')

        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='?!?help(DM)')
        embed.add_field(name='?!?help(DM)', value='도움말을 DM으로 보냅니다.(send help message to DM.)', inline=False)
        embed.add_field(name='?!?help(CHANNEL)', value='도움말을 채널에 보냅니다.(send help message at channel.)', inline=False)
        embed.add_field(name='?!?천슾아유튜브', value="천슾아유튜브의 링크를 보냅니다.(send 1000spa's youtube link.)", inline=False)
        embed.add_field(name='?!?천슾아는?', value="천슾아에 대한 정보를 알려줍니다.(send 1000spa's profiles.)", inline=False)
        embed.add_field(name='?!?캡챠', value='캡챠를 플레이합니다.(play captcha.)')
        await message.author.send(embed=embed)

    if message.content == '?!?help(CHANNEL)':
        embed = discord.Embed(colour = discord.Colour.red())
        embed.set_author(name='?!?help(CHANNEL)')
        embed.add_field(name='?!?help(DM)', value='도움말을 DM으로 보냅니다.(send help message to DM.)', inline=False)
        embed.add_field(name='?!?help(CHANNEL)', value='도움말을 채널에 보냅니다.(send help message at channel.)', inline=False)
        embed.add_field(name='?!?천슾아유튜브', value="천슾아유튜브의 링크를 보냅니다.(send 1000spa's youtube link.)", inline=False)
        embed.add_field(name=':question: ?!?천슾아는?:question:', value="천슾아에 대한 정보를 알려줍니다.(send 1000spa's profiles.)", inline=False)
        embed.add_field(name='?!?캡챠', value='캡챠를 플레이합니다.(play captcha.)', inline=False)
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