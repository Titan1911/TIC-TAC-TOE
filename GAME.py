import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

slot = [' '] *9
turn = 0



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hear_name():
    with sr.Microphone() as source:
        r = sr.Recognizer()

        r.adjust_for_ambient_noise(source)

        print('Speak up the name of player 1: ')
        speak('Speak up the name of player 1: ')
        print('Listening....')
        audio = r.listen(source)
        print("Processing....")
        player_one = r.recognize_google(audio)
        print(player_one)

        print('Speak up the name of player 2: ')
        speak('Speak up the name of player 2: ')
        print('Listening....')
        audio = r.listen(source)
        print('Processing....')
        player_two = r.recognize_google(audio)
        print(player_two)

    return (player_one,player_two)



def base_board():
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")


def main_board():
    print(f' {slot[0]} | {slot[1]} | {slot[2]} ')
    print("---|---|---")
    print(f' {slot[3]} | {slot[4]} | {slot[5]} ')
    print("---|---|---")
    print(f' {slot[6]} | {slot[7]} | {slot[8]} ')



def voice_recog(player_one,player_two):

    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)

        print('Speak up the slot which you want to fill: ')
        speak('Speak up the slot which you want to fill: ')
        print('Listening....')
        audio = r.listen(source)

        try:
            print("Processing....")
            option = r.recognize_google(audio)
            option = int(option)

        except:
            print("", end='')


    if option in range(1,10) :
        if slot[option-1] == ' ' :
            if chance == player_one :
                slot[option-1] = 'O'

            else :
                slot[option-1] = 'X'

        else :
            print("This slot is already filled, choose a different one")
            speak("This slot is already filled, choose a different one")
            voice_recog(player_one,player_two)

    else :
        print("This is an invalid slot, please enter a slot between 1 to 9")
        speak("This is an invalid slot, please enter a slot between 1 to 9")
        voice_recog(player_one,player_two)


def win_situation():
    print(f'{chance} is the winner!')
    speak(f'{chance} is the winner!')
    exit()


def win_condition():
    for n in [0,3,6]: #horizontal
        if slot[n]==slot[n+1]!=' ' and slot[n+1]==slot[n+2] :
            main_board()
            win_situation()

    for n in [0,1,2]: #vertical
        if slot[n]==slot[n+3]!=' ' and slot[n+3]==slot[n+6] :
            main_board()
            win_situation()

    for n in [0]: #leading diagonal
        if slot[n]==slot[n+4]!=' ' and slot[n+4]==slot[n+8] :
            main_board()
            win_situation()

    for n in [2]: #other diagonal
        if slot[n]==slot[n+2]!=' ' and slot[n+2]==slot[n+4] :
            main_board()
            win_situation()



if __name__ == '__main__':
    player_one, player_two = hear_name()
    while True:

        if turn % 2 == 0:
            chance = player_one

        else:
            chance = player_two

        base_board()
        print('\n')
        main_board()

        print(f"{chance}'s turn")
        speak(f"{chance}'s turn")

        voice_recog(player_one,player_two)

        win_condition()

        turn = turn + 1

        if turn == 9:
            print("The Game is drawn!")
            speak("The Game is drawn!")
            main_board()
            exit()