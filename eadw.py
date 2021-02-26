
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
      aa = message.content.split()
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
          aa1= aa[1]
          aa2= aa[2]
          aa3= aa[3]
          aa4= aa[4]
          aa5= aa[5]
          aa6= aa[6]
          aa7= aa[7]
          aa8= aa[8]
          aa9= aa[9]
          aa10= aa[10]
          팀 = [1,1,1,1,1,2,2,2,2,2]
          랜덤 = random.shuffle(팀)
          team = open('team.txt','w')
          for i in range (1):
              team.write('-------------')
              team.write('\n')
              team.write(str(aa1))
              team.write('\t')
              team.write(str(팀[0]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa2))
              team.write('\t')
              team.write(str(팀[1]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa3))
              team.write('\t')
              team.write(str(팀[2]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa4))
              team.write('\t')
              team.write(str(팀[3]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa5))
              team.write('\t')
              team.write(str(팀[4]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa6))
              team.write('\t')
              team.write(str(팀[5]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa7))
              team.write('\t')
              team.write(str(팀[6]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa8))
              team.write('\t')
              team.write(str(팀[7]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa9))
              team.write('\t')
              team.write(str(팀[8]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa10))
              team.write('\t')
              team.write(str(팀[9]))
              team.write("팀")
              team.write('\n')
              team.write('-------------')
          team.close()
          flie = open('team.txt')
          await message.channel.send(flie.read())
          flie.close()    
      except:
          await message.channel.send("이름을 !팀설정 옆에 10명 띄어 적어주세요(팀설정 1 2 3 ...)")
          return


  if message.content==("팀 재설정"):
          팀 = [1,1,1,1,1,2,2,2,2,2]
          랜덤 = random.shuffle(팀)
          team = open('team.txt','w')
          for i in range (1):
              team.write('-------------')
              team.write('\n')
              team.write(str(aa1))
              team.write('\t')
              team.write(str(팀[0]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa2))
              team.write('\t')
              team.write(str(팀[1]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa3))
              team.write('\t')
              team.write(str(팀[2]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa4))
              team.write('\t')
              team.write(str(팀[3]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa5))
              team.write('\t')
              team.write(str(팀[4]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa6))
              team.write('\t')
              team.write(str(팀[5]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa7))
              team.write('\t')
              team.write(str(팀[6]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa8))
              team.write('\t')
              team.write(str(팀[7]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa9))
              team.write('\t')
              team.write(str(팀[8]))
              team.write("팀")
              team.write('\n')
              team.write(str(aa10))
              team.write('\t')
              team.write(str(팀[9]))
              team.write("팀")
              team.write('\n')
              team.write('-------------')              
          team.close()
          flie = open('team.txt')
          await message.channel.send(flie.read())
          flie.close()

bot.run(os.environ['token'])
