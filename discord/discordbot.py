# インストールした discord.py を読み込む
import discord
import time

import sys
sys.path.append('..')

from firebase import firebase_server

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzAyMTQ2MzAxMjg2MDIzMTc4.Xp70xg.MJnmV8tBlWJn1m0XXn5_uH-dT2Q'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    await send_dm_all_user(client.users, "お前は誰だ")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
#    if firebase_server.check_is_users_registered(

    dm = await message.author.create_dm()
    await dm.send(message.content)


    print(message.content)
    firebase_server.register_user(9997, 'test#0000', '', 'DISCORD', 'test')

    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')


async def send_dm_all_user(users, message):
    for user in users:
        print(user.id)
        print(user.name)
#        await send_dm_to(user, message)

async def send_dm_to(user, message):
    print(user.bot)
    if user.bot:
        return
    dm = await user.create_dm()
    await dm.send(message)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

