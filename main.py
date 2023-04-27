#modules
import time
import random
import webbrowser

#variables
clear_screen='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
def endless_mode():
   score=0
   lives=5
   endless_mode_instructions='\n\n\n\nEndless Mode Rules And Gameplay!!!!\n1• In This Mode Words Pop Up Infinite Time.\n2• You Have To Type The Exact Word Showed On Screen.\n3• If You Type It Correctly Then You Will Get A Score Credit.\n4• If You Failed To Type Then You Will Lose A Life.\n5• The Score Will Be According To Your Time Taken.\n6• Type Fast If You Want To Make More Scores.\n7• You Have Total 5 Lives\n\n '
   print(endless_mode_instructions)
   startt=input('\n Press Any Key To Start')
   if startt=='wi8wdhhdwjiwjxhshuwiwudhdhdgey2u2iy3gdhxbdnwjejdhhdbdhehehehshshs':
       exit()
   else:
       print("\nGame Starts!!!! Type The Word Showed Below")   
        
   while lives > -1:
        x=random.randint(0,370099)
        f=open("words_alpha.txt",'r')
        all_words=f.read()
        words=all_words.split()
        word=words[x].lower()
        print(f'\n\t\tScore - {score}\tLives={lives}\n{word}\n')
        start=time.time()
        f.close()
            
        answer=input().lower()
        if answer==word:
            end=time.time()
            float_time=end-start
            str_time=str(float_time)
            time_took_str=str_time[0:5]  
            time_took=float(time_took_str)
            print(f'You Took {time_took} Seconds')
            if time_took<3.0:
                score+=5
                print('Score + 5')
            elif time_took>3.0 and time_took<6.0:
                score+=3
                print('Score + 3')
            elif time_took>6.0 and time_took<10.0:
                score+=2
                print('Score + 2')
            else:
                score+=1
                print('Score + 1')
                
        else:
            lives-=1
            if lives>0:
                print('\nYou Lose A Live\n')
            if lives<0:
                print(clear_screen)
                print('You Lose All Your Lives Better Luck Next Time!!')
                print('\n\n')
                print('**********GAME OVER**********')
                replay=input('Type R To Restart !!\nType Yt To Visit YouTube Channel').lower()
                if "r" in replay:
                    endless_mode()
                elif "yt" in replay:
                    webbrowser.open("https://youtube.com/@RedEndGamers")
            




def gamemode_selection():
    global clear_screen
    
    mode_selection=input('Available Gamemodes:--\n\n1• Endless Mode\n2• Visit YouTube Channel\n')
    if "1" in mode_selection:
        print(clear_screen,'You Selected Endless Mode')
        endless_mode()
    elif "2" in mode_selection:
        webbrowser.open("https://youtube.com/@RedEndGamers\n")



print('\t\tWelcome To Typing Speed Tester \n Made By Sukhman Majri !!!\n\n\t\tThe Game Is Simple\n\nYou Have To Type The Word Generated Below As Fast As You Can !!! Type In Whatever Manner Case Sensitive Is Off\n\n\nHave A Good Game!!\n\n \n\n')

gamemode_selection()