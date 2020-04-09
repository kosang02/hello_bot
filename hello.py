
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("일")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")



    if message.content.startswith("!아임뚜렛"):
        await message.channel.send("아잇 어 아잇 푸르르르르 12번!")


    if message.content.startswith("!그냥명령어"):
        await message.channel.send("!　그냥명령어,!채널정보")


    if message.content.startswith("!봇제작자"):
        await message.channel.send("kosang02")


    if message.content.startswith("!채널정보"):
        await message.channel.send(
              "2020-04-08에 처음 만들어짐 처음맴버는 집사,고상혁,에코,정우재,김민서 로 시작했으며 대장은 집사이다.")


    if message.content.startswith("!채널의고비"):
        await message.channel.send(
                    "2020-04-08: 혼란  방이 처음만들어지고 모두가 서로 다른말을 하면서 시작됨 근데 20분만에 끝남")


    if message.content.startswith("!날씨"):
        await message.channel.send("직접 찾아보세요")


    if message.content.startswith("!혼란"):
        await message.channel.send(
                                                                    "2020-04-08에 방이 처음생기자 모두가 서로 다른말을 한 사건. 아임뚜렛을 따라하는 사람도 있었고 엄준식의 뜻이 엄마가 준비한 식단이라고 하던 사람도 있었으며 전 여기서 일하고 싶어요를 반복하는 전여일빌런도 있었지만"
                                                                    "핵심인원인 정우재가 자러가면서 혼란이 끝났다. ")



    if message.content.startswith("!쓸대없는명령어"):
        await message.channel.send(
                                                                            " !　아임뚜렛,!채널의고비,!날씨,!혼란,!봇 제작자,!안녕")



    if message.content.startswith("!봇태스트"):
        await message.channel.send(
                                                                                    "Hello, I'am 'Helloworld_bot'.고상혁 making me in 2020-04-09  This is test mod ")



    if message.content.startswith("!모든명령어"):
        await message.channel.send("!　안녕,!아임뚜렛,!채널의고비,!날씨,!혼란,!봇제작자,!그냥명령어,!쓸대없는명령어,!채널정보")


client.run("Njk3ODAwNzM2Njc0ODA3ODQ4.Xo81Cw.T3ZHzdqZ-LfGTg3je62ImP4mcgg")