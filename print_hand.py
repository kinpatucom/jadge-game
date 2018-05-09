import utils
import random

print('じゃんけんをしよう！！')
player_name=input('名前はなに？')
select_hand=int(input('何を出すか数字で決めてね！(0:ぐー 1:チョキ 2:パー)'))

if utils.validate(select_hand):
    computer_hand=random.randint(0,2)
    if player_name=='':
        utils.print_hand(select_hand)
    else:
        utils.print_hand(select_hand,player_name)
    utils.print_hand(computer_hand,'コンピューター')
    result=utils.judge(select_hand,computer_hand)
    print('結果は'+result+'でした')
else:
    print('正しい値を入力してください')
