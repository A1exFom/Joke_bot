import joy_bot
import pytest
import unittest.mock
import asyncio

def test_best_game():
    async def func():
        # with unittest.mock.patch('joy_bot.bot'):
        ctx= unittest.mock.Mock()
        ctx.send = unittest.mock.AsyncMock()
        await joy_bot.best_game(ctx)
        ctx.send.assert_called_with('Tarkov')
    asyncio.run(func())

def test_oct_to_dec():
    async def func():
        # with unittest.mock.patch('joy_bot.bot'):
        ctx= unittest.mock.Mock()
        ctx.send = unittest.mock.AsyncMock()
        await joy_bot.oct_to_dec(ctx, '145')
        ctx.send.assert_called_with('101')
    asyncio.run(func())

def test_dec_to_hex():
    async def func():
        # with unittest.mock.patch('joy_bot.bot'):
        ctx= unittest.mock.Mock()
        ctx.send = unittest.mock.AsyncMock()
        await joy_bot.dec_to_hex(ctx, '14')
        ctx.send.assert_called_with('0xe')
    asyncio.run(func())

def test_hex_to_dec():
    async def func():
        # with unittest.mock.patch('joy_bot.bot'):
        ctx= unittest.mock.Mock()
        ctx.send = unittest.mock.AsyncMock()
        await joy_bot.hex_to_dec(ctx, 'E')
        ctx.send.assert_called_with('14')
    asyncio.run(func())

def test_dec_to_bin():
    async def func():
        # with unittest.mock.patch('joy_bot.bot'):
        ctx= unittest.mock.Mock()
        ctx.send = unittest.mock.AsyncMock()
        await joy_bot.dec_to_bin(ctx, '36735675445555555785555535')
        ctx.send.assert_called_with('0b1111001100011000101001111010011001111011001101010001000000100010110001011111001001111')
    asyncio.run(func())
