import os
import asyncio
import discord
import subprocess
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)
file = open('token.txt', 'r')
token = file.readline()
file.close()

# 當機器人完成啟動時
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

# 載入指令程式檔案
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def check(ctx):
    try:
        process = subprocess.Popen(f"./check_host.sh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(timeout=15)
        status = process.returncode # 獲取伺服器狀態
        if status == 0:
            await ctx.send("Web Server Status:\n```\nUP\n```")
        else:
            await ctx.send("Web Server Status:\n```\nDOWN\n```")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# 卸載指令檔案
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

# 重新載入程式檔案
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())
