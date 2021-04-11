import random
import itertools

marks = ['○', '×']
number_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-' ]
my_list = []
enemy_list = []
all_list = []
my_name = ''

def name_input():
    global my_name
    print('3目並べを始めます')
    name_message = 'あなたの名前を入力してください'
    my_name = input(name_message)
    return my_name
    
def play_janken():
    print('あなたの名前は' + my_name + 'です')
    hands = ['グー', 'チョキ', 'パー']
    janken = input('じゃんけんをしてください（0:グー, 1:チョキ, 2:パー）')
    while not enable_hand(janken):
        janken = input('じゃんけんをしてください（0:グー, 1:チョキ, 2:パー）')
    print(hands[int(janken)])
    
def enable_hand(string):
    if string.isdigit():
        number = int(string)
        if number >= 0 and number <= 2:
            return True
        else:
            return False
    else:
        return False

def decide_1or2(my_name):
    one = random.randint(0,1)
    #自分が勝ちの場合
    if one == 0:
        print(my_name + 'がジャンケンに勝ちました')
        message = '先攻か後攻か選んでください(1:先攻, 2:後攻)'
        turn_choice = int(input(message))
        if turn_choice == 1:
            print(my_name + 'は先攻を選びました')
        elif turn_choice == 2:
            print(my_name + 'は後攻です')
    #相手が勝ちの場合
    elif one == 1:
        print('ジャンケンに負けました')
        turn_choice = random.randint(1,2)
        if turn_choice == 2:
            print('相手は先攻を選びました')
            print(my_name + 'は後攻です')
        elif turn_choice == 1:
            print('相手は後攻を選びました')
            print(my_name + 'が先攻です')
    return one, turn_choice

def show_table():
  print('｜' + str(number_list[0]) + '｜' + str(number_list[1]) + '｜' + str(number_list[2]) + '｜' + '   ' + '｜0｜1｜2｜')
  print('｜' + str(number_list[3]) + '｜' + str(number_list[4]) + '｜' + str(number_list[5]) + '｜' + '...' + '｜3｜4｜5｜')
  print('｜' + str(number_list[6]) + '｜' + str(number_list[7]) + '｜' + str(number_list[8]) + '｜' + '   ' + '｜6｜7｜8｜')  

def my_choice():
    print(my_name + 'の番です')
    if len(all_list) == 0:
        message = '0~8のマスを選んでください'
    else:
        message = str(sorted(all_list)) + '以外の0~8のマスを選んでください' 
    choice_number = input(message)
    while not enable_choice_table(choice_number):
      choice_number = input(message)
  
    print(my_name + 'は「' + str(choice_number) + '」に入れました。')
    number_list[int(choice_number)] = choice_mark
    my_list.append(int(choice_number))
    my__list = sorted(my_list)
    all_list.append(int(choice_number))
    show_table()
    if len(all_list) == 9 and not add_list(my_list):
        print('引き分けです。初めからやり直します。')
        shokika()
        second_time()
    else:
        pass
      
    if not add_list(my__list):
        enemy_choice()
    else:
        print(my_name + 'が勝ちました！！')
     
def enable_choice_table(string):
    if string.isdigit():
        number = int(string)
        if number >= 0 and number <=8:
            if number in my_list or number in enemy_list:
                return False
            else:
                return True
            return True
        else:
            return False
    else:
            False

def enemy_choice():
    print('相手の番です')
    choice_number = random.randint(0, 8)
    while choice_number in my_list or choice_number in enemy_list:
        choice_number = random.randint(0, 8)
    print('相手は「' + str(choice_number) + '」に入れました。')
    number_list[int(choice_number)] = enemy_mark
    enemy_list.append(choice_number)   
    enemy__list = sorted(enemy_list)
    all_list.append(choice_number)
    show_table()
    if len(all_list) == 9 and not add_list(enemy__list):
        print('引き分けです。初めからやり直します。')
        shokika()
    else:
        pass
    
    if not add_list(enemy__list):
        my_choice()
    else:
        print('相手が勝ちました')    

def add_list(list):
    for pair in itertools.combinations(list, 3):
        list.append(pair)
    if (0, 1, 2) in list or (3, 4, 5) in list or (6, 7, 8) in list or (0, 3, 6) in list or (1, 4, 7) in list or (2, 5, 8) in list or (0, 4, 8) in list or (2, 4, 6) in list:
        return True
    else: 
        return False

def shokika():
    global number_list
    number_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    my_list.clear()
    enemy_list.clear()
    all_list.clear()

def second_time():
    show_table()
    my_choice()

def check(choice_turn):
    global choice_mark
    global enemy_mark
    if choice_turn[0] == 0:
        choice_mark_number = int(input('「○」「×」どちらにしますか？(0:○, 1:×)'))
        choice_mark = marks[choice_mark_number]
        print(my_name + 'は「' + choice_mark + '」を選びました.')
        if choice_mark_number == 0:
            enemy_mark_number = 1
            enemy_mark = marks[enemy_mark_number]
            print('相手は「' + enemy_mark + '」です')                 
        else:
            enemy_mark_number = 0
            enemy_mark = marks[enemy_mark_number]
            print('相手は「' + enemy_mark + '」です')        
    elif choice_turn[0] == 1:
        enemy_mark_number = random.randint(0, 1)
        enemy_mark = marks[enemy_mark_number]
        print('相手は「' + enemy_mark + '」を選びました.')
        if enemy_mark_number == 0:
            choice_mark_number = 1
            choice_mark = marks[choice_mark_number]
            print(my_name + 'は「' + choice_mark + '」を使います')
        else:
            choice_mark_number = 0
            choice_mark = marks[choice_mark_number]
            print(my_name + 'は「' + choice_mark + '」を使います')
    if choice_turn[1] == 1:
        show_table()
        my_choice()
    elif choice_turn[1] == 2:
        enemy_choice()

def play():
    my_name = name_input()
    play_janken()
    choice_turn = decide_1or2(my_name)
    check(choice_turn)

play()


