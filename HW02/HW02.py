import os #下載模組os.py

def main(): #main 主要描述程式的開始。就好比是 Java or C的 main
    print ('Hello world!') #印出Hello world

    print ("This is Alice's greeting.") #印出句子。雙引號也可以引用字串,注意要前後一致。
    print ('This is Bob\'s greeting.') #印出句子。

    foo (5, 10) #函數運用

    print ('=' *10) #複製字串 印出'=========='
    print ('Current working directory is ' + os.getcwd()) #加號連接字串,使用os.getcwd()的模組,返回上一個目錄。


    cornter = 0 #變量先被實際化，以便進行統計。
    counter += 1

    food = ['apples', 'oranges', 'cats'] #內建列表的類型。

    for i in food: #假設i是食物。進入迴圈,冒號即結束說明。
        print ('I like to eat ' + i) #迴圈中i是我設定的food

    print ('Count to ten:')
    for i in range(10): #內建函數,返回0~9的數字列表
        print (i) #印出i


def foo(param1, secondParam): #運用函數,冒號表示結束
    res = param1 + secondParam #字串輸出

    print ('%S plus %S is equal to %S')

    if res < 50: #判斷假設res<50 #判斷句和C語言相同，用冒号结束判断语句，使用if elif else。
        print ('foo') #符合上述條件,即印出foo

    elif (res >= 50) and ((paraml == 42) or (secondParam ==24)): #邏輯運算不使用&&和||
        print ('bar') #符合上述條件,即印出bar

    else:
        print ('moo') #都不符合條件,即印出moo

    return res #This is a one-line comment. #單行註解。
'''A multi-line string, but can also be a multi-line comment.''' #多行註解,使用'''進行縮行即可。

if __name__ == 'main': #一般在程式最後使用主函數main();而且使用内置的運行程式名來判定。
    main() #當程式進行時,並不運行main(),這裡是放置測試的程式代碼。
