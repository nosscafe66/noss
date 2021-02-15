class Rpg:
    def info(self):
      return self.player + 'のHPは' + str(self.hp) + 'で攻撃力は' + str(self.a) + 'です'

    def __init__(self , player ,  hp, a):
      #print('自動で生成されます') #returnしてなくても自動でselfが返される

      self.player = player
      self.hp = hp
      self.a = a