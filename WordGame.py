from random import randint
import time,sys

# 玩家
class Player:
    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士

# 战士
class Warrior:
    def __init__(self, strength):
        self.strength = strength
    # 用灵石疗伤
    def healing(self, stoneCount):
        if self.strength == self.maxStrength:
            return
        self.strength += stoneCount
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength

# 弓箭兵，战士的子类
class Archer(Warrior):
    typeName = '弓箭兵'
    price = 100 # 雇佣价：100灵石
    maxStrength = 100 # 弓箭兵最大生命值

    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')

# 斧头兵，战士的子类
class Axeman(Warrior):
    typeName = '斧头兵'
    price = 120 # 雇佣价：120灵石
    maxStrength = 120 # 斧头兵最大生命值

    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('''
***************************************
****           游戏开始             ****
***************************************

'''
)


#1、产生森林和妖怪

forest_num = 7# 森林数量
forestList = []# 森林列表
# 为每座森林随机产生鹰妖或者狼妖
notification = '前方森林里的妖怪是：' # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )
    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '

print('请在十秒内记住以下内容：')
# 显示妖怪信息
print(notification,end='')
print('')
time.sleep(10)

for i in range(20):
    print('')


#2、雇佣战士

print('现有1000灵石，请根据你记忆的妖怪种类和数量，选择雇佣弓箭兵和斧头兵的个数，每雇佣一个士兵，给他起一个名字。')
stoneNumber=1000
ArcherNumber=int(input('请输入需要雇佣的弓箭兵的数量：'))
for a in range(ArcherNumber):
    ArcherName=input('请输入弓箭兵的名字：')

AxemanNumber=int(input('请输入需要雇佣的斧头兵的数量：'))
for a in range(AxemanNumber):
    AxemanName=input('请输入斧头兵的名字：')


#3、开始征途

print('开始征途，要通过7座森林，系统不会提示你森林里面是什么妖怪（玩家凭记忆回想），每座森林只能派出一个战士去消灭里面的妖怪,你需要选择派出哪个战士。如果战士生命值损耗完，这个战士就死亡了，如果战士死亡，就得派出另外一名战士杀死妖怪。每次通过森林后，你可以选择是否用灵石给战士补养；如果选择补养，消耗1个灵石可以为生命值加1，但是不可能超过最大生命值。')
print('最后，一定要通过7座森林才算通关。剩余灵石越多，越有机会当选国王。')
for n in range(7):
    while True:
        print('遇到一只妖怪')
        s=input('请选择需要派出的战士名字：')
        print('战斗中...')
        # 和妖怪战斗
        def fightWithMonster(self,monster):
            if monster.typeName== '鹰妖':
                self.strength -= 20
            elif monster.typeName== '狼妖':
                self.strength -= 80
            else:
                print('未知类型的妖怪！！！')
        break
        if Warrior.strength=0:
            break
            print('该战士已死亡，你需要继续派出其他的战士进行战斗。')
            w=input('请选择需要派出的战士名字：')
            print('战斗中...')
            if monster.strength=0:
                print('妖怪已死亡，恭喜你顺利通过该森林！')
                break
                #用灵石疗伤
            def healing(self, stoneCount):
            # 如果已经到达最大生命值，灵石不起作用，浪费了
            if self.strength == self.maxStrength:
                return
            self.strength += stoneCount
            if self.strength > self.maxStrength:
                self.strength = self.maxStrength
                
print('恭喜你通过所有森林，已通关！')
print(stoneNumber) #剩余灵石数量
