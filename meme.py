import praw
import discord
from discord.ext import commands
import random
import os
client= commands.Bot(command_prefix='oi ')
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Danking around"))
    print("Works")
reddit = praw.Reddit(client_id = 'Db06qqPd7w7SGg', 
                    client_secret = '_5wYenAB9v7uMCA1DBgwryl4PFL3pA', 
                    user_agent = 'Nomto memes')
@client.command()
async def meme(ctx):
    subc= ["memes","dankmemes"]
    sub= random.choice(subc)
    meme= reddit.subreddit(sub)
    posts = meme.hot(limit=20)
    p=[]
    for post in posts:
        p.append(post)
    rand= random.choice(p)
    url= rand.url
    title= rand.title
    upvotes=rand.score
    embed= discord.Embed(title=title)
    embed.set_image(url=url) 
    await ctx.send(embed=embed)
client.run("ODI1MjI2MDQ5NDk5NDMwOTMy.YF61pg.Hvbnkb4yFZA02axsaCZtpYE8jDI")
