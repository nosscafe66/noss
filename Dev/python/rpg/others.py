'''
#person_n = Person('登場人物',HP , '攻撃力')
person_1 = Person('魔法使い', 1000, 300)
person_2 = Person('剣士', 800, 800)
person_3 = Person('武闘家', 900, 600)
person_4 = Person('僧侶', 500, 1000)

persons = [person_1, person_2, person_3, person_4]

#登場人物関数の定義

def player(player_n, player_hp, player_a):
    print(player_n +'のHPは' + str(player_hp) + 'で攻撃力は' + str(player_a) + 'です')

player('剣士', 800, 800)


#武器関数の定義
def item(item_n , item_a):
    print(item_n + 'の威力は' + str(item_a) + 'です')

item('双剣' , 400)

def enemy():


persons = {'魔法使い':1000 , '剣士':800 , '武闘家':900, '僧侶':500}

items = {'双剣':400, '杖':200, '短剣':300, '大剣':500}

for person_n in persons :
    print('-------------------------------------------') 
    print(person_n + 'のHPは' + str(persons[person_n]) + 'です')

select_c = input('冒険する' + person_n + 'と')



#print('----------------------------------------')




select_c = int(input('キャラクターを選択してください(敵キャラは自動で選択されます):'))
character = rpg_s[select_c]
print('選択したキャラクターは:' + character.player)





#インスタンスの生成 インスタンス変数 player,hp,a,item(追加したければする
#インスタンス変数に関しては自分が開発しようとしている物に何が必要かを把握していないとわからない。
#上記の__init__()へ代入しているため以下の３つは削除
rpg_1.player = '魔法使い'
print(rpg_1.player)

rpg_1.hp = 1000
print(rpg_1.hp)

rpg_1.a = 300
print(rpg_1.a)



rpg_2 = rpg()
rpg_2.player = '剣士'
print(rpg_2.player)

rpg_2.hp = 800
print(rpg_2.hp)

rpg_2.a = 800
print(rpg_2.a)

print(rpg_2.info()) #インスタンスメソッドの構築をして出力
damge = rpg_2.buttle(500)
print(rpg_2.player + 'へのダメージは' + str(damage) + 'でした')



rpg_3 = rpg()
rpg_3.player = '武闘家'
print(rpg_3.player)

rpg_3.hp = 900
print(rpg_3.hp)

rpg_3.a = 600
print(rpg_3.a)

print(rpg_3.info()) #インスタンスメソッドの構築をして出力
damage = rpg_3.buttle(700)
print(rpg_3.player + 'へのダメージは' + str(damage) + 'でした')



rpg_4 = rpg()
rpg_4.player = '僧侶'
print(rpg_4.player)

rpg_4.hp = 500
print(rpg_4.hp)

rpg_4.a = 1000
print(rpg_4.a)

print(rpg_4.info()) #インスタンスメソッドの構築をして出力
damage = rpg_4.buttle(300)
print(rpg_4.player + 'へのダメージは' + str(damage) + 'でした')



#バトル用の関数を作成しておく
def buttle(self,enemy_a):
      buttle = self.a - enemy_a
      return buttle
      '''

