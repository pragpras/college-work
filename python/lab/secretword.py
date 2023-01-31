password="secret"
i=10
while i>0:
    word=input("enter the secret word: ")
    if word==password:
        print("congratulations! you guessed correctly!")
        break
    else:
        i=i-1
        print("incorrect guess. you have",i,"guesses left.")
if i==0:
    print("sorry, you have run out of guesses.")   
        