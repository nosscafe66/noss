from rpg import Rpg
from Enemy import Enemy
from Item import Item
from Street import street_1
from Damage import Damage
import random

rpg_1 = Rpg('魔法使い', 1000, 300)
rpg_2 = Rpg('剣士', 800, 800)
rpg_3 = Rpg('武闘家', 900 ,600)
rpg_4 = Rpg('僧侶', 500 ,1000)

enemy_1 = Enemy('スライム' , 500 , 200)
enemy_2 = Enemy('魔女' , 900 , 500)
enemy_3 = Enemy('剣術士' , 600 , 700)
enemy_4 = Enemy('ドラゴン' ,1500 , 1000)

item_1 = Item('双剣' , 600)
item_2 = Item('マジックポーション' , 500)
item_3 = Item('ハンマー' , 900)
item_4 = Item('爆弾' , 800)

street_1_1 = street_1('普通の道')
street_1_2 = street_1('獣道')

damage_1 = Damage('ファイア' , 800)
damage_2 = Damage('フリーズ' , 500)
damage_3 = Damage('リッパー' , 700)
damage_4 = Damage('ストーム' , 1000)


#上記のインスタンスしたモノをリスト化する
rpg_s = [rpg_1 , rpg_2 , rpg_3 , rpg_4]
index = 0
print('----------------------------------------')
for rpg in rpg_s :
    #print(str(index) +':'+ rpg.info())
    index += 1


enemy_s = [enemy_1 , enemy_2 , enemy_3 , enemy_4]
index = 0
print('-------------------以下は敵キャラの一覧ですがあなたは選択できません---------------------')
for Enemy in enemy_s :
    print(str(index) + ':' + Enemy.info())
    index += 1


select_c = int(input('プレイヤーを選択してください(0:魔法使い, 1:剣士, 2:武闘家, 3:僧侶);{敵キャラは自動で選択されます}:'))
character = rpg_s[select_c]
print('選択したプレイヤーは:' + character.player)


select_n = random.randint(0 , 3)
select_e = select_n
character_e = enemy_s[select_e]
print('選択された敵は:' + character_e.ename)




item_s = [item_1 , item_2 , item_3 , item_4] 
index = 0


print('----------------------------------------')
for Item in item_s :
    #print(str(index) + ':' + Item.info())
    index += 1 

select_i = int(input('あなたは４つのうちどの武器を選択しますか？;(0:双剣 , 1:マジックポーション ,2:ハンマー, 3:爆弾)'))
y = item_s[select_i]
print('あなたが選択した道は' + y.iname)


street_1_s = [street_1_1 , street_1_2]
index = 0


print('----------------------------------------')
for Street in street_1_s :
    #print(str(index) + ':' + Street.info())
    index += 1


select_st = int(input('どちらの道を選択しますか？;(0:普通の道 , 1:獣道)'))
x = street_1_s[select_st]

print('あなたが選択した道は' + x.stname)

damage_s = [damage_1 , damage_2 , damage_3 , damage_4] 
index = 0

select_d = random.randint(0 , 3)
select_dn = select_d
damage_e = damage_s[select_dn]

if select_st == 1:
    print('しばらく' + x.stname + 'を歩いていると' + character_e.ename + 'が出現')

   
    print(character_e.ename + "は" + damage_e.dname + "で" + character.player + 'を攻撃した')

elif select_st == 0:
    print('しばらく' + x.stname + 'を歩いていると落し物を見つけた')