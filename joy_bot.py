import discord
import random
a=['f','g']
b=random.choice(a)
print(b)

from discord.ext import commands
bot = commands.Bot(command_prefix='!')
@bot.command()
async def about(ctx):
    await ctx.send('Joy_bot для Discord сервера. \nДанный бот содержит в себе как развлекательные функции, так и полезные для обучения.\nПодробнее все команды можно найти в !help')
@bot.command()
async def help_bot(ctx):
    await ctx.send('Доступные функции бота:\n'
                   '!coin - бот подбрасывает монетку \n'
                   '!random - выводит случайное число в заданном диапазоне \n'
                   '!cat - фотогравия кота\n'
                   '!joke - анекдот\n'
                   '!dec_to_bin - перевод между СС\n'
                   '!dec_to_oct - перевод между СС\n'
                   '!dec_to_hex - перевод между СС\n'
                   '!bin_to_dec - перевод междуСС\n'
                   '!oct_to_dec - перевод междуСС\n'
                   '!hex_to_dec - перевод междуСС\n'
                   '!start_game_party - отмечает пользователей онлайн и передает им сообщение\n'
                   .upper())
@bot.command()
async def cat(ctx):
    cat_pictures = ['https://clck.ru/ZP9TQ', 'https://clck.ru/ZP9Tk', 'https://clck.ru/ZP9UZ', 'https://clck.ru/ZP9V4', 'https://clck.ru/ZP9X6', 'https://clck.ru/ZP9Yy']
    cat_1 = random.choice(cat_pictures)
    await ctx.send(str(cat_1))
@bot.command()
async def coin(ctx):
    coin_pot = ['орел', 'решка', 'орел', 'решка', 'неудачно, монетка укатилась']
    coin2 = random.choice(coin_pot)
    if coin2 == 'орел':
        coin2 = 'выпал ' + coin2
    elif coin2 == 'решка':
        coin2= 'выпала ' + coin2
    await ctx.send(str(coin2))
@bot.command()
async def random(ctx):
    await ctx.send ('Введите команду и промежуток до которого нужно вывести число (используйте пробел)')
@bot.command()
async def random_number(ctx, arg2):
    a=int(arg2)
    res = random.randint(0, a)
    await ctx.send (str(res))
@bot.command()
async def dec_to_bin(ctx, arg2):
    a=int(arg2)
    res = bin(a)
    await ctx.send (str(res))
@bot.command()
async def dec_to_oct(ctx, arg2):
    a = int(arg2)
    g=''
    while a > 0:
        g = str(a % 8) + g
        a = a // 8
    await ctx.send(str(g))
@bot.command()
async def dec_to_hex(ctx, arg2):
    a = int(arg2)
    g=hex(a)
    await ctx.send(str(g))
@bot.command()
async def bin_to_dec(ctx, arg2):
    a = ('0b'+ str(arg2))
    g=int(a,2)
    await ctx.send(str(g))
@bot.command()
async def oct_to_dec(ctx, arg2):
    a = ('0o'+ str(arg2))
    g=int(a,8)
    await ctx.send(str(g))
@bot.command()
async def hex_to_dec(ctx, arg2):
    a = ('bx'+ str(arg2))
    g=int(a,16)
    await ctx.send(str(g))
@bot.command()
async def joke(ctx):
    joke_store = ['Чем больше должен, тем хуже память.',
                  'Купил самоклеящиеся обои. Сижу. Жду.',
                  'Плох тот таксист, который выбирает короткий маршрут.',
                  'https://clck.ru/ZPGLN',
                  'Так приятно себе ни в чём не отказывать целый день после зарплаты.',
                  'Каждый думает, что он незаменим, пока он не заменён.']
    joke_1= random.choice(joke_store)
    await ctx.send(str(joke_1))
@bot.command()
async def best_game(ctx):
    await ctx.send ('Tarkov')
@bot.command()
async def start_game_party(ctx, *, arg):
    await ctx.send ('@here'+arg)
@bot.command()
async def attention(ctx, *, arg):
    await ctx.send ('@everyone'+arg)

bot.run('OTIxMjI1MzM4OTg0NDc2Nzc1.Ybvz9A.x0fEP6nXs1i9VUpxlZY9bALEFgM')

# import discord
# import random
# from discord import utils
#
# 'Роли, доступные пользователю на тестовм сервере'
# roles = {
#     '🤓': 921578755711983657 , #студент
#     '🎮': 921579055172690021, #игрок
# }
# exeption = {
#     '': 921226384951640105
# }
# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(self.user, 'activated')
#     async def on_message(self, message):
#         if message.author == self.user:
#             return
#
#         if message.content.endswith('подбрось монетку') or message.content == ('!coin') :
#             coin_pot = ['орел', 'решка', 'орел', 'решка', 'неудачно, монетка укатилась']
#             coin = random.choice(coin_pot)
#             if coin == 'орел':
#                 coin= 'выпал ' + coin
#             elif coin == 'решка':
#                 coin= 'выпала ' + coin
#             await message.channel.send( str(coin))
#         if message.content == ('!cat') :
#             cat_pictures = ['https://clck.ru/ZP9TQ', 'https://clck.ru/ZP9Tk', 'https://clck.ru/ZP9UZ', 'https://clck.ru/ZP9V4', 'https://clck.ru/ZP9X6', 'https://clck.ru/ZP9Yy']
#             cat = random.choice(cat_pictures)
#             await message.channel.send( str(cat))
#
#         if message.content == ('!random') or message.content.endswith('назови случайное число'):
#             await message.channel.send('Укажите промежуток (<50 to 100>)')
#         if message.content.startswith('<10 to 100>'):
#             random_res = random.randint(0, 100)
#             await message.channel.send(str(random_res))
#
#     async def on_raw_reaction_add(self, payload):
#         if payload.message_id == 921580091740418109:
#             channel = self.get_channel(payload.channel_id)  # получаем объект канала
#             message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
#             member = utils.get(message.guild.members, id=payload.user_id)  # получаем объект пользователя который поставил реакцию
#             try:
#                 emoji = str(payload.emoji)  # эмоджик который выбрал юзер
#                 role = utils.get(message.guild.roles, id=roles[emoji])  # объект выбранной роли (если есть)
#
#                 if (len([i for i in member.roles if i.id not in exeption]) <= 4):
#                     await member.add_roles(role)
#                     print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
#                 else:
#                     await message.remove_reaction(payload.emoji, member)
#                     print('[ERROR] Too many roles for user {0.display_name}'.format(member))
#
#             except KeyError as e:
#                 print('[ERROR] KeyError, no role found for ' + emoji)
#             except Exception as e:
#                 print(repr(e))
#
#
# client = MyClient()
# client.run('OTIxMjI1MzM4OTg0NDc2Nzc1.Ybvz9A.BuJpm9UpbGkBH1kjdvFSw1sv4Yw')
# import discord
# import random
#
# from discord.ext import commands
# bot = commands.Bot(command_prefix='!')
# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')
# @bot.command()
# async def cat(ctx):
#     cat_pictures = ['https://clck.ru/ZP9TQ', 'https://clck.ru/ZP9Tk', 'https://clck.ru/ZP9UZ', 'https://clck.ru/ZP9V4', 'https://clck.ru/ZP9X6', 'https://clck.ru/ZP9Yy']
#     cat_1 = random.choice(cat_pictures)
#     await ctx.send(str(cat_1))
#
# @bot.command()
# async def coin(ctx):
#     coin_pot = ['орел', 'решка', 'орел', 'решка', 'неудачно, монетка укатилась']
#     coin = random.choice(coin_pot)
#     if coin == 'орел':
#         coin = 'выпал ' + coin
#     elif coin == 'решка':
#         coin= 'выпала ' + coin
#     await ctx.send(str(coin))
# bot.run('OTIxMjI1MzM4OTg0NDc2Nzc1.Ybvz9A.BuJpm9UpbGkBH1kjdvFSw1sv4Yw')
