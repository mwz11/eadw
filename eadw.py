
import discord, asyncio
import random
import string
import os 

from discord.ext import commands


bot = commands.Bot (command_prefix='prefix')

z=0
s=0
d=0
zz = 0
xx = 0
aa11 = 0
aa22 = 0
aa33 = 0
aa44 = 0
aa55 = 0
aa66 = 0
aa77 = 0
aa88 = 0
aa99 = 0
aa1010 = 0

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print('실행완료')




@bot.event
async def on_message(message):
  if message.author.bot:
        return None
  if message.content.startswith("!팀설정"):
      msg_l = message.content.split()
      zz = 0
      xx = 0
      aa11 = 0
      aa22 = 0
      aa33 = 0
      aa44 = 0
      aa55 = 0
      aa66 = 0
      aa77 = 0
      aa88 = 0
      aa99 = 0
      aa1010 = 0
      try:
          global aa1
          global aa2
          global aa3
          global aa4
          global aa5
          global aa6
          global aa7
          global aa8
          global aa9
          global aa10
          aa1= msg_l[1]
          aa2= msg_l[2]
          aa3= msg_l[3]
          aa4= msg_l[4]
          aa5= msg_l[5]
          aa6= msg_l[6]
          aa7= msg_l[7]
          aa8= msg_l[8]
          aa9= msg_l[9]
          aa10= msg_l[10]
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if 랜덤 == 1:
              zz = zz + 1
              aa11 = 1
          if 랜덤 == 2:
              xx = xx + 1
              aa11 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if 랜덤 == 1:
              zz = zz + 1
              aa22 = 1
          if 랜덤 == 2:
              xx = xx + 1
              aa22 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if 랜덤 == 1:
              zz = zz + 1
              aa33 = 1
          if 랜덤 == 2:
              xx = xx + 1
              aa33 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if 랜덤 == 1:
              zz = zz + 1
              aa44 = 1
          if 랜덤 == 2:
              xx = xx + 1
              aa44 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if 랜덤 == 1:
              zz = zz + 1
              aa55 = 1
          if 랜덤 == 2:
              xx = xx + 1
              aa55 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if zz == 5:
              aa66 = 2
          elif 랜덤 == 1:
              zz = zz + 1
              aa66 = 1
          if xx == 5:
              aa66 = 1
          elif 랜덤 == 2:
              xx = xx + 1
              aa66 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if zz == 5:
              aa77 = 2
          elif 랜덤 == 1:
              zz = zz + 1
              aa77 = 1
          if xx == 5:
              aa77 = 1
          elif 랜덤 == 2:
              xx = xx + 1
              aa77 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if zz == 5:
              aa88 = 2
          elif 랜덤 == 1:
              zz = zz + 1
              aa88 = 1
          if xx == 5:
              aa88 = 1
          elif 랜덤 == 2:
              xx = xx + 1
              aa88 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if zz == 5:
              aa99 = 2
          elif 랜덤 == 1:
              zz = zz + 1
              aa99 = 1
          if xx == 5:
              aa99 = 1
          elif 랜덤 == 2:
              xx = xx + 1
              aa99 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if zz == 5:
              aa1010 = 2
          elif 랜덤 == 1:
              zz = zz + 1
              aa1010 = 1
          if xx == 5:
              aa1010 = 1
          elif 랜덤 == 2:
              xx = xx + 1
              aa1010 = 2
          team = open('team.txt','w')
          for i in range (1):
              team.write(str(aa1))
              team.write('\t')
              team.write(str(aa11))
              team.write("팀")
              team.write('\n')
              team.write(str(aa2))
              team.write('\t')
              team.write(str(aa22))
              team.write("팀")
              team.write('\n')
              team.write(str(aa3))
              team.write('\t')
              team.write(str(aa33))
              team.write("팀")
              team.write('\n')
              team.write(str(aa4))
              team.write('\t')
              team.write(str(aa44))
              team.write("팀")
              team.write('\n')
              team.write(str(aa5))
              team.write('\t')
              team.write(str(aa55))
              team.write("팀")
              team.write('\n')
              team.write(str(aa6))
              team.write('\t')
              team.write(str(aa66))
              team.write("팀")
              team.write('\n')
              team.write(str(aa7))
              team.write('\t')
              team.write(str(aa77))
              team.write("팀")
              team.write('\n')
              team.write(str(aa8))
              team.write('\t')
              team.write(str(aa88))
              team.write("팀")
              team.write('\n')
              team.write(str(aa9))
              team.write('\t')
              team.write(str(aa99))
              team.write("팀")
              team.write('\n')
              team.write(str(aa10))
              team.write('\t')
              team.write(str(aa1010))
              team.write("팀")
          team.close()
          flie = open('team.txt')
          await message.channel.send('-------------------------')
          await message.channel.send(flie.read())
          await message.channel.send('-------------------------')
          flie.close()    
      except:
          await message.channel.send("이름을 테스트 옆에 한 명씩 띄어 적어 주세요.(10명만 적어 주세요)")
          return





  if message.content == ('팀 재설정'):
          zz = 0
          xx = 0
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if 랜덤 == 1:
              zz = zz + 1
              aa11 = 1
          if 랜덤 == 2:
              xx = xx + 1
              aa11 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if 랜덤 == 1:
              zz = zz + 1
              aa22 = 1
          if 랜덤 == 2:
              xx = xx + 1
              aa22 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if 랜덤 == 1:
              zz = zz + 1
              aa33 = 1
          if 랜덤 == 2:
              xx = xx + 1
              aa33 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if 랜덤 == 1:
              zz = zz + 1
              aa44 = 1
          if 랜덤 == 2:
              xx = xx + 1
              aa44 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if 랜덤 == 1:
              zz = zz + 1
              aa55 = 1
          if 랜덤 == 2:
              xx = xx + 1
              aa55 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if zz == 5:
              aa66 = 2
          elif 랜덤 == 1:
              zz = zz + 1
              aa66 = 1
          if xx == 5:
              aa66 = 1
          elif 랜덤 == 2:
              xx = xx + 1
              aa66 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if zz == 5:
              aa77 = 2
          elif 랜덤 == 1:
              zz = zz + 1
              aa77 = 1
          if xx == 5:
              aa77 = 1
          elif 랜덤 == 2:
              xx = xx + 1
              aa77 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if zz == 5:
              aa88 = 2
          elif 랜덤 == 1:
              zz = zz + 1
              aa88 = 1
          if xx == 5:
              aa88 = 1
          elif 랜덤 == 2:
              xx = xx + 1
              aa88 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if zz == 5:
              aa99 = 2
          elif 랜덤 == 1:
              zz = zz + 1
              aa99 = 1
          if xx == 5:
              aa99 = 1
          elif 랜덤 == 2:
              xx = xx + 1
              aa99 = 2
          팀 = [1,2]
          랜덤 = random.choice(팀)
          print(랜덤)
          print(zz)
          print(xx)
          if zz == 5:
              aa1010 = 2
          elif 랜덤 == 1:
              zz = zz + 1
              aa1010 = 1
          if xx == 5:
              aa1010 = 1
          elif 랜덤 == 2:
              xx = xx + 1
              aa1010 = 2
          team = open('team.txt','w')
          for i in range (1):
              team.write(str(aa1))
              team.write('\t')
              team.write(str(aa11))
              team.write("팀")
              team.write('\n')
              team.write(str(aa2))
              team.write('\t')
              team.write(str(aa22))
              team.write("팀")
              team.write('\n')
              team.write(str(aa3))
              team.write('\t')
              team.write(str(aa33))
              team.write("팀")
              team.write('\n')
              team.write(str(aa4))
              team.write('\t')
              team.write(str(aa44))
              team.write("팀")
              team.write('\n')
              team.write(str(aa5))
              team.write('\t')
              team.write(str(aa55))
              team.write("팀")
              team.write('\n')
              team.write(str(aa6))
              team.write('\t')
              team.write(str(aa66))
              team.write("팀")
              team.write('\n')
              team.write(str(aa7))
              team.write('\t')
              team.write(str(aa77))
              team.write("팀")
              team.write('\n')
              team.write(str(aa8))
              team.write('\t')
              team.write(str(aa88))
              team.write("팀")
              team.write('\n')
              team.write(str(aa9))
              team.write('\t')
              team.write(str(aa99))
              team.write("팀")
              team.write('\n')
              team.write(str(aa10))
              team.write('\t')
              team.write(str(aa1010))
              team.write("팀")
          team.close()
          flie = open('team.txt')
          await message.channel.send('-------------------------')
          await message.channel.send(flie.read())
          await message.channel.send('-------------------------')
          flie.close() 

  if message.content == ('팀 설정'):
        global z, s, d
        z=0
        s=0
        d=0
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
       flie = open('team.txt')
       await reaction.message.channel.send('-------------------------')
       await reaction.message.channel.send(flie.read())
       await reaction.message.channel.send('-------------------------')
       flie.close()
       print (z,s,d)

bot.run(os.environ['token'])
