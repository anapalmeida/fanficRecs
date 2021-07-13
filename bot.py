import os
from ao3 import AO3
import discord
from discord.ext import tasks, commands
import random

client = discord.Client()
api = AO3()

replies = [
    'Coming right up!',
    'Sure thing!',
    'Hmmm, naughty'
    'On it!',
    'Of course!',
    'Sure!',
    'In a sec',
    'Wait up!',
    'One of those days, huh?'
]

r = random.choice(replies)

def listToString(s): 
    str = " " 
    return (str.join(s))

@client.event
async def on_ready():
  print('We have logged in as  {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.content == "--rec a fic":
    await message.reply(r)

    work = api.work(id='31934125')

    summary = work.summary
    summary = summary.replace("<p>","").replace("</p>","").replace("</br>", " ").replace("<br>", " ").replace("<br/>", " ")

    fandoms_o = work.fandoms
    fandoms_o = listToString(fandoms_o)

    rating = work.rating
    rating = listToString(rating)

    relationship_o = work.relationship
    relationship_o = listToString(relationship_o)

    masked_link_embed = discord.Embed(
      title=work.title,
      url=work.url, 
      description=summary,
      color=discord.Colour.dark_red()
  )

  masked_link_embed.set_author(name="Archive of Our Own",icon_url="https://archiveofourown.org/images/ao3_logos/logo_42.png")

  masked_link_embed.add_field(name="Author", value=work.author, inline=True)
  masked_link_embed.add_field(name="Fandom", value=fandoms_o, inline=True)
  masked_link_embed.add_field(name="Rating", value=rating, inline=True)
  masked_link_embed.add_field(name="Pairing", value=relationship_o, inline=True)

  masked_link_embed.add_field(name = chr(173), value = chr(173), inline=False)

  masked_link_embed.add_field(name="Hits", value=work.hits, inline=True)
  masked_link_embed.add_field(name="Kudos", value=work.kudos, inline=True)
  masked_link_embed.add_field(name="Comments", value=work.comments, inline=True)

  masked_link_embed.set_footer(text="Happy reading!")


  await message.channel.send(embed=masked_link_embed)
  pass

  test.start()

@tasks.loop(minutes=1)
async def test():
    channel = client.get_channel(os.environ['TEST_CHANNEL'])
    
    await channel.send("test")    
    
client.run(os.environ['FANFICRECS_BOT_TOKEN'])