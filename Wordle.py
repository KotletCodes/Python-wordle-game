
import random
words = open("WORDS.txt","r")
word = []
num = random.randint(0,3000)
for x in range(0,3000):
    word.append(words.readline())

chosenword = word[num]

letterscorrect = 0
count = 5
guess = ""
while count != 0 and letterscorrect != 5 :
    guess = input("enter your guess!")
    count = count -1
    
   
        
    
    for i in range(0,len(guess)):
        if guess[i] == chosenword[i]:
                print("the",i+1,"letter is in the correct place")
                letterscorrect = letterscorrect +1
                
        elif guess[i] in chosenword and guess[i] != chosenword[i]:

                print("the",i+1,"letter is in the word but in the wrong place")
                
        else:
                print("this letter",[i+1]," is not in the word")
    print(count,"tries left")
   

        
if count == 0:
    print("Try again")
else:
    print("well done, took you",count,"tries")

                   
