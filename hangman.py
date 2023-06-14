
def hangman(word):
    wrong=0
    stages=["",
            "_______          ",
            "|                ",
            "|      |         ",
            "|      0         ",
            "|     /|\        ",
            "|     / \        ",
            "|                ",
            ]
    rletters=list(word)#答えをリスト化
    board=["_"]*len(word)
    win=False#最後のif not winの判定の時のために設定している
    print("ハングマンへようこそ")
    while wrong < len(stages) - 1:
        print("\n")#\nは改行の意味
        msg="1文字を予想してね:"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char#boardのcind番目がcharに変換する
            rletters[cind]="$"#rlettersの２番目を$に変換、aを入力してももう答えではない
        else:
            wrong+=1
        print(" ".join(board))#見やすいように_の間に半角スペースを入力
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win=True
            break
    if not win:#if ():()がtrueだったら下のコマンドが実行される。今回の場合は"not win"が()の部分にあたる
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

import random
list1=["cat","apple","dog"]
word=random.choice(list1)
hangman(word)