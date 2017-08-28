import discord
import keys
import asyncio
from aioconsole import ainput
import string
import datetime
import time
from pytz import timezone
import pytz


def main():


  k = keys.keys()
  c = discord.Client()


  @c.event
  async def on_ready():
    print('Ready!')
    await run(c)


  c.run(k.token)


async def run(c):
  print(c.get_server("244098799222521866"))
  discord.opus.load_opus("/usr/local/lib/libopus.so")

  general = None
  v = None
  currentPlayer = None

  for channel in c.get_all_channels():
    if channel.name == "general":
      general = channel
    if channel.name == "General":
      v = await c.join_voice_channel(channel)
    #print(channel.name, channel.id)

  print(c.is_voice_connected(c.get_server("244098799222521866")))

  async def get_input():
    while 1:
      line = await ainput("")
    #   if line.split()[0] == "send":
      await c.send_message(general, line)



  @c.event
  async def on_message(message):
    if str(message.author) != 'hawaiian-snowbot#3575':
      print("%s [%s]: %s" %(message.author, datetime.datetime.now(timezone('America/Chicago')).strftime('%m.%d.%Y %I:%M:%S %p'), message.content))
    if message.content.split()[0] == "!delall" and str(message.author) == "Cam#6101":
      deleted = await c.purge_from(general, limit=100, check=is_me)
      await c.send_message(general, 'Deleted {} message(s)'.format(len(deleted)))
    if message.content.split()[0] == "!roll" and str(message.author) == "Cam#6101":
      currentPlayer = await v.create_ytdl_player("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
      currentPlayer.start()
    if message.content.split()[0] == "!stop" and str(message.author) == "Cam#6101":
      currentPlayer.stop()

  @c.event
  async def on_voice_state_update(before, after):
    if not after.voice.voice_channel:
      await c.send_message(general, "Bye %s" % before.name)



  def is_me(m):
    return m.author == c.user

  await get_input()





if __name__ == '__main__':
    main()
