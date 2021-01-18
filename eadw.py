
import discord, asyncio
import random
import string

from discord.ext import commands


bot = commands.Bot (command_prefix='prefix')

z=0
s=0
d=0

@bot.event
async def on_ready():
    print('실행완료')

@bot.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == ('팀 설정'):
        embed = discord.Embed(title="5대5팀 설정",description="참가 하실분은 👌눌러주세요")
        aas= await message.channel.send(embed=embed)        
        await aas.add_reaction("👌")

@bot.event
async def on_reaction_add(reaction, user):
    유저 = (user)
    if user.bot == 1:
        return None
    await reaction.message.channel.send(user.name + "님 참여") and print (유저)
    global z
    z = z + 1
    if z == 1:
       team = open('team.txt','w')
       for i in range (1):
           팀 = [1,2]
           랜덤 = random.choice(팀)
           if 랜덤 == 1:
               global d
               d = d + 1
               print (d)
           if 랜덤 == 2:
               global s
               s = s + 1
               print (s)
           team.write(str(유저))
           team.write('\t')
           team.write(str(랜덤))
           team.write('팀')
       team.close()
    if z == 2:
       team = open('team.txt','a')
       for i in range (1):
           team.write('\n')
           팀 = [1,2]
           랜덤 = random.choice(팀)
           if 랜덤 == 1:
               d = d + 1
               print (d)
           if 랜덤 == 2:
               s = s + 1
               print (s)
           team.write(str(유저))
           team.write('\t')
           team.write(str(랜덤))
           team.write('팀')
       team.close()
    if z == 3:
       team = open('team.txt','a')
       for i in range (1):
           team.write('\n')
           팀 = [1,2]
           랜덤 = random.choice(팀)
           if 랜덤 == 1:
               d = d + 1
               print (d)
           if 랜덤 == 2:
               s = s + 1
               print (s)
           team.write(str(유저))
           team.write('\t')
           team.write(str(랜덤))
           team.write('팀')
       team.close()
    if z == 4:
       team = open('team.txt','a')
       for i in range (1):
           team.write('\n')
           팀 = [1,2]
           랜덤 = random.choice(팀)
           if 랜덤 == 1:
               d = d + 1
               print (d)
           if 랜덤 == 2:
               s = s + 1
               print (s)
           team.write(str(유저))
           team.write('\t')
           team.write(str(랜덤))
           team.write('팀')
       team.close()
    if z == 5:
       team = open('team.txt','a')
       for i in range (1):
           team.write('\n')
           팀 = [1,2]
           랜덤 = random.choice(팀)
           if 랜덤 == 1:
               d = d + 1
               print (d)
           if 랜덤 == 2:
               s = s + 1
               print (s)
           team.write(str(유저))
           team.write('\t')
           team.write(str(랜덤))
           team.write('팀')
       team.close()
    if z == 6:
       team = open('team.txt','a')
       for i in range (1):
           team.write('\n')
           팀 = [1,2]
           랜덤 = random.choice(팀)
           print (랜덤)
           if d == 5:
               team.write(str(유저))
               team.write('\t')
               team.write('2팀')
               print ('1팀 끝')
               continue
           elif 랜덤 == 1:
               d = d + 1
               print (d)
               team.write(str(유저))
               team.write('\t')
               team.write(str(랜덤))
               team.write('팀')
               continue
           if s == 5:
               team.write(str(유저))
               team.write('\t')
               team.write('1팀')
               print ('2팀 끝')
               continue
           elif 랜덤 == 2:
               s = s + 1
               print (s)
               team.write(str(유저))
               team.write('\t')
               team.write(str(랜덤))
               team.write('팀')
               continue
    if z == 7:
       team = open('team.txt','a')
       for i in range (1):
           team.write('\n')
           팀 = [1,2]
           랜덤 = random.choice(팀)
           print (랜덤)
           if d == 5:
               team.write(str(유저))
               team.write('\t')
               team.write('2팀')
               print ('1팀 끝')
               continue
           elif 랜덤 == 1:
               d = d + 1
               print (d)
               team.write(str(유저))
               team.write('\t')
               team.write(str(랜덤))
               team.write('팀')
           if s == 5:
               team.write(str(유저))
               team.write('\t')
               team.write('1팀')
               print ('2팀 끝')
               continue
           elif 랜덤 == 2:
               s = s + 1
               print (s)
               team.write(str(유저))
               team.write('\t')
               team.write(str(랜덤))
               team.write('팀')
    if z == 8:
       team = open('team.txt','a')
       for i in range (1):
           team.write('\n')
           팀 = [1,2]
           랜덤 = random.choice(팀)
           print (랜덤)
           if d == 5:
               team.write(str(유저))
               team.write('\t')
               team.write('2팀')
               print ('1팀 끝')
               continue
           elif 랜덤 == 1:
               d = d + 1
               print (d)
               team.write(str(유저))
               team.write('\t')
               team.write(str(랜덤))
               team.write('팀')
               continue
           if s == 5:
               team.write(str(유저))
               team.write('\t')
               team.write('1팀')
               print ('2팀 끝')
               continue
           elif 랜덤 == 2:
               s = s + 1
               print (s)
               team.write(str(유저))
               team.write('\t')
               team.write(str(랜덤))
               team.write('팀')
               continue
    if z == 9:
       team = open('team.txt','a')
       for i in range (1):
           team.write('\n')
           팀 = [1,2]
           랜덤 = random.choice(팀)
           print (랜덤)
           if d == 5:
               team.write(str(유저))
               team.write('\t')
               team.write('2팀')
               print ('1팀 끝')
               continue
           elif 랜덤 == 1:
               d = d + 1
               print (d)
               team.write(str(유저))
               team.write('\t')
               team.write(str(랜덤))
               team.write('팀')
               continue
           if s == 5:
               team.write(str(유저))
               team.write('\t')
               team.write('1팀')
               print ('2팀 끝')
               continue
           elif 랜덤 == 2:
               s = s + 1
               print (s)
               team.write(str(유저))
               team.write('\t')
               team.write(str(랜덤))
               team.write('팀')
               continue
    if z == 10:
       team = open('team.txt','a')
       for i in range (1):
           team.write('\n')
           팀 = [1,2]
           랜덤 = random.choice(팀)
           print (랜덤)
           if d == 5:
               team.write(str(유저))
               team.write('\t')
               team.write('2팀')
               print ('1팀 끝')
               continue
           elif 랜덤 == 1:
               d = d + 1
               print (d)
               team.write(str(유저))
               team.write('\t')
               team.write(str(랜덤))
               team.write('팀')
               continue
           if s == 5:
               team.write(str(유저))
               team.write('\t')
               team.write('1팀')
               print ('2팀 끝')
               continue
           elif 랜덤 == 2:
               s = s + 1
               print (s)
               team.write(str(유저))
               team.write('\t')
               team.write(str(랜덤))
               team.write('팀')
               continue
       team.close()
       z=0
       s=0
       d=0
       flie = open('team.txt')
       await reaction.message.channel.send('-------------------------')
       await reaction.message.channel.send(flie.read())
       flie.close()
       print (z,s,d)



        
    



    
    

     


    

      


        
bot.run(os.environ['token'])
