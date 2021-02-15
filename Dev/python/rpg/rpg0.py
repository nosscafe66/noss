import random

print('さあ、冒険を始めよう！')
player_name = input("あなたの名前を入力してください")
print('しばらく' + player_name + 'は歩く')

#分かれ道----------------------------------------------
street_1 = '獣道'
street_2 = '普通の道'

Street = int(input('しばらく歩くと目の前に分かれ道、どっちを選択する(1:獣道,2:普通の道)'))

if Street == 1 :
  print(player_name + 'は' + street_1 + 'を選択した')

elif Street == 2:
  print(player_name + 'は' + street_2 + 'を選択した')
  print('そのまままっすぐ進むとお城が見えてきた。', end = "")
#分かれ道----------------------------------------------

#①スライムの出現と攻撃---------------------------------------------
if Street == 1 :
  print('しばらく獣道を歩いているとスライムが出現してきた。',
    end = "")

#②普通の道でお城の前のお供えものを入れる。

item_1 = '剣'
item_2 = '飲み物'
item_3 = '無い'

if Street == 2 :
  print('しばらく歩いているとお城の前にはお供え物を入れるツボがあった')


  Item = int(input('お城のツボにお供え物をするが今の手持ちでできるものは２つしかないがどうする？(1:剣を差し出す,2:飲み物を差し出す,3:引き返してお供え物を探す)'))

#攻撃の種類
damage_1 = 'ファイア'
damage_2 = 'フリーズ'
damage_3 = 'リッパー'
damage_4 = 'ストーム'
#street部門①----------------------------------------------
if Street == 1 :
    print('あなたは攻撃を仕掛けた')
    Damage = int(input('どの攻撃を選択する？(1:ファイア,2:フリーズ,3:リッパー,4:ストーム)'))

#攻撃1
    if Damage == 1 :
            print(player_name + 'は' + damage_1 + '選択した')
            print('返り討ちで'+ player_name +'はゲームオーバー')
            

    elif Damage == 2 :
            print(player_name + 'は' + damage_2 + '選択した')
            print(player_name + 'は' + 'スライムに勝った')


    elif Damage == 3 :
            print(player_name + 'は' + damage_3 + '選択した')
            print('敵はまだ死ななかった、もう一回攻撃を仕掛けよう')

            Damage_2 = int(input('何番の攻撃を選択する？(1:ファイア,2:フリーズ,3:リッパー,4:ストーム)'))

#攻撃2
            if Damage_2 == 1 :
                    print(player_name + 'は' + damage_1 + '選択した')
                    print(player_name + 'は' + 'スライムに勝った')

            elif Damage_2 == 2 :
                    print(player_name + 'は' + damage_2 + '選択した')
                    print(player_name + 'は' + 'スライムに勝った')

            elif Damage_2 == 3 :
                    print(player_name + 'は' + damage_3 + '選択した')
                    print(player_name + 'は' + 'スライムに勝った')

#elif  street == 1 == 2:
        #print(player_name + 'は' + damage_4 + '選択した')


#お供え物をした後---------------------------------------------


if Item == 1 :
        print(player_name + 'は' + item_1 + 'をお供えした')

elif Item == 2 :
        print(player_name + 'は' + item_2 + 'をお供えした')

elif Item == 3 :
        print(player_name + 'はお供え物が' +item_3 + 'ので探すために引き返した。')



