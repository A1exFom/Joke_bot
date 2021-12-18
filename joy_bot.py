import discord
import random

from discord.ext import commands
bot = commands.Bot(command_prefix='!')
'''Указываем префикс команды. Он позволит отличать обычный текст от команды для нашего бота'''
@bot.command()
async def about(ctx):
    await ctx.send('Joy_bot для Discord сервера. \nДанный бот содержит в себе как развлекательные функции, так и полезные для обучения.\nПодробнее все команды можно найти в !help_bot')
    '''Функция about - команда для бота. Бот описывает себя.'''
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
                   '!attention - - отмечает всех пользователей сервера и передает им сообщение\n'
                   .upper())
    '''Фунция help_bot содержит в себе команду для бота, в которой он перечисляет все свои "умения" (список имеющихся команд)
    Также все выводится большими буквами, чтобы облегчить восприятие текса пользователем'''
@bot.command()
async def cat(ctx):
    cat_pictures = ['https://clck.ru/ZP9TQ', 'https://clck.ru/ZP9Tk', 'https://clck.ru/ZP9UZ', 'https://clck.ru/ZP9V4', 'https://clck.ru/ZP9X6', 'https://clck.ru/ZP9Yy']
    cat_1 = random.choice(cat_pictures)
    await ctx.send(str(cat_1))
    '''Cat выводи рандомное(случайное) изображение кота или кошки. В списке содержится несколько url ссылок, которые отправляются в чат, превращаясь в картинку'''
@bot.command()
async def coin(ctx):
    coin_pot = ['орел', 'решка', 'орел', 'решка', 'неудачно, монетка укатилась']
    coin2 = random.choice(coin_pot)
    if coin2 == 'орел':
        coin2 = 'выпал ' + coin2
    elif coin2 == 'решка':
        coin2= 'выпала ' + coin2
    await ctx.send(str(coin2))
    '''!coin - команда, вызванная функцией coin, позволяет боту выводить случайное название части монеты. Также предусмотрена развлекательная функция в виде ошибки броска - "монетка укатилась" '''
@bot.command()
async def rand(ctx):
    await ctx.send ('Введите команду и промежуток до которого нужно вывести число (используйте пробел)')
    '''random команда для вывода случайного числа'''
@bot.command()
async def random_number(ctx, arg2):
    a=int(arg2)
    res = random.randint(0, a)
    await ctx.send (str(res))
    '''Данная функция (random_number) позволяет пользователю задать вторую часть интервала, чтобы бот вывел случайное число из полученного промежутка'''
@bot.command()
async def dec_to_bin(ctx, arg2):
    a=int(arg2)
    res = bin(a)
    await ctx.send (str(res))
    '''dec_to_bin - функция перевода цисел из 10 в 2 СС'''
@bot.command()
async def dec_to_oct(ctx, arg2):
    a = int(arg2)
    g=''
    while a > 0:
        g = str(a % 8) + g
        a = a // 8
    await ctx.send(str(g))
    '''dec_to_oct - функция перевода цисел из 10 в 8 СС'''
@bot.command()
async def dec_to_hex(ctx, arg2):
    a = int(arg2)
    g=hex(a)
    await ctx.send(str(g))
    '''dec_to_hex - функция перевода цисел из 10 в 16 СС'''
@bot.command()
async def bin_to_dec(ctx, arg2):
    a = ('0b'+ str(arg2))
    g=int(a,2)
    await ctx.send(str(g))
    '''bin_to_dec - функция перевода цисел из 2 в 10 СС. Создана для обратного превода к функции dec_to_bin'''
@bot.command()
async def oct_to_dec(ctx, arg2):
    a = ('0o'+ str(arg2))
    g=int(a,8)
    await ctx.send(str(g))
    '''oct_to_dec - функция перевода цисел из 8 в 10 СС. Создана для обратного превода к функции dec_to_oct'''
@bot.command()
async def hex_to_dec(ctx, arg2):
    arg4= arg2.lower()
    a = ('0x'+ str(arg4))
    g=int(a,16)
    await ctx.send(str(g))
    '''hex_to_dec - функция перевода цисел из 16 в 10 СС. Создана для обратного превода к функции dec_to_hex'''
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
    '''Функция и команда joke позволяет боту прислать случайную шутку, мем, анекдот в чат'''
@bot.command()
async def best_game(ctx):
    await ctx.send ('Tarkov')
    '''best_game - функция, выводящая заранее заданное текстовое значение на определенную команду'''
@bot.command()
async def start_game_party(ctx, *, arg):
    await ctx.send ('@here'+arg)
    '''функция start_game_party создана для быстрого создания группы для общения. Она заключается в отметке всех пользователей, находящихся online в момент активации команды.
     Также после упоминания будет размещен текст сообщения, отправленного пользователем к этой команде.'''
@bot.command()
async def attention(ctx, *, arg):
    await ctx.send ('@everyone'+arg)
    '''функция attention создана для упоминания всех пользователей как в сети, так и вне сети .
         Также после упоминания будет размещен текст сообщения, отправленного пользователем к этой команде.'''
if __name__=='__main__':
    bot.run('Token')
'''bot.run должно содержать токен бота. Токен - это цифровое значение, привязанное к боту. Из-за параметров безопасности Discord токен нельзя выкладывать в сеть, 
так как при попадении в нее он сразу же обнуляется автоматически'''
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
