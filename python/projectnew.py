# Import module 
from tkinter import *
from PIL import ImageTk, Image
  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("400x400")
  
# Add image file
#bg = PhotoImage(file = "istockphoto-520643683-612x612.png")
  
# Create Canvas
canvas1 = Canvas( root, width = 400, height = 400)
  
canvas1.pack(fill = "both", expand = True)

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("final_bg.png")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(resized)
   canvas1.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
root.bind("<Configure>", resize_image)

#main

import time

points = 0

print("Every decision made by you has consequences.")
print("Each right one gets you additional points. Each wrong one however brings you closer to the escape of the real murderer.")
print("Let the mystery begin...")
print("---------------------------------------------------------------------------------------------------------------------------")
print("An ivy covered manor. The stench of blood and betrayal hangs in the still mountain air. A death was discovered at Rook Estate.")
print("Open wounds gasping for air, his marred body was laid on the bed. The Lord of the Manor, Sir William Crawley, was murdered.")
print("You, a consulting detective, arrive at the estate the following morning at the Lady's behest.")
print("Butler: Welcome, detective. What should we call you?")

name = input("Type your name: ")

print("Butler: Lady Crawley awaits your presence in the parlour,",name,"!")
print("You go up to the parlour. You find Lady Crawley seated there, crying into a handkerchief.")
print("Do you:")
print("1. Give your condolences, 2. Accuse her of killing her husband")

c1=int(input("Enter your choice: "))
if c1==1:
    print("Lady Crawley thanks you and invites you to start taking the statements of the manor's inmates.")
else:
    print("Lady Crawley cries even harder and leaves the room, leaving you to call upon each person of the house in turn to take their statements.")
    
print("---------------------------------------------------------------------------------------------------------------------------")
time.sleep(5)
print("Before the investigation here's the facts of the case: ")
print("The Lord died of multiple stab wounds in the evening at 5 pm. He was alone and asleep in bed when he was killed in his sleep. No one heard him.")
print("He was only discovered when the butler came up an hour later to bring him his tea.")
print("No finger prints were found around the room")
print("---------------------------------------------------------------------------------------------------------------------------")
time.sleep(15)
print("The investigation begins, select the suspect to know their alibis.  ")
print("1. The twins, 2. Lady Crawley, 3. Butler, 4. Cook, 5. Gardener, 6. Lady's maid, 7. Two servants, 8. Chauffeur, 9. Tutor")
print('choose option 10 to proceed to the motives.')

def alibi():
    global x
    x=[
 "The twins, age 15, were dressing up in armour in the armory at 5 pm. The Lady's maid heard a crash around 5.30 pm.",
 "Lady Crawley was stitching clothes in the parlour. Nobody can back this alibi up.",
 "The Butler was reading the newspaper in his room. Nobody can back this alibi up.",
 "The cook was in the kitchen preparing supper. Both the servants can back this up as they were helping her.",
 "The gardener was in the backyard fields pruning some bushes. Lady Crawley can back this up as she saw him from her window from time to time.",
 "The Lady's maid was getting her Lady tea from the kitchen. She was last seen by Lady Crawley after getting the tea.",
 "Servants were helping the cook make supper. The cook can back this alibi up.",
 "The chauffeur took the car to get repaired. The car repairman down the road can back this alibi up.",
 "The tutor was reading in his room. No one can back this alibi up."
 ]
    c2=int(input("Enter your choice: "))
    if c2==1:
        print(x[0])
        alibi()
    elif c2==2:
        print(x[1])
        alibi()
    elif c2==3:
        print(x[2])
        alibi()
    elif c2==4:
        print(x[3])
        alibi()
    elif c2==5:
        print(x[4])
        alibi()
    elif c2==6:
        print(x[5])
        alibi()
    elif c2==7:
        print(x[6])
        alibi()
    elif c2==8:
        print(x[7])
        alibi()
    elif c2==9:
        print(x[8])
        alibi()
    elif c2==10:
        storyline()
    else:
        print("Invalid choice. Please enter a number from 1-9")
        alibi()

def storyline():
    #the choices that will get the points
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("You now get to hear the motives of any 5 members. Choose wisely.")
    print("1. The twins, 2. Lady Crawley, 3. Butler, 4. Cook, 5. Gardener, 6. Lady's maid, 7. Two servants, 8. Chauffeur, 9. Tutor")
    motives()
    
def motives():
    y=['The Lord was abusive and violent when drunk but it was hushed up',
       'The Lord was abusive and violent when drunk and also she would get all his money', 
       'The Lord was very rude to him most of the time',
       'None',
       'None',
       'Hates the Lord bc he is abusive to her Lady',
       'None',
       'None',
       "The Lord never paid him on time"
]
    pointc = [1,2,3,6,9]
    for i in range(5):
        c3=int(input("Enter your choice:"))
        if c3 in pointc:
            global points
            points += 1
        if c3==1:
            print(y[0])
        elif c3==2:
            print(y[1])
        elif c3==3:
            print(y[2])
        elif c3==4:
            print(y[3])
        elif c3==5:
            print(y[4])
        elif c3==6:
            print(y[5])
        elif c3==7:
            print(y[6])
        elif c3==8:
            print(y[7])
        elif c3==9:
            print(y[8])
        else:
            print("Invalid choice. Please enter a number from 1-9")
            motives()

def murderweapon():
    time.sleep(7)
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("One of the twins rushes into the room, crying. You ask what happened calmly.")
    print("The child silently points to the Great Hall and runs out.")
    print("You follow her out into the Hall. You see a glint of silver from one of the potted plants.")
    print("Do you, 1. Check the stem or 2. Check the root?")
    c4=int(input("Enter your choice: "))
    if c4==1:
        print("You find blood on the leaves but nothing else.")
        c4=2
    elif c4==2:
        print("You find a long, silver dagger buried among the roots, with blood still crusted on its blade. This is your murder weapon.")
        print("No prints were obtained from the weapon.")
        global points
        points += 1
    else:
        print('invalid')
        murderweapon()
        
def room_search():
    print("---------------------------------------------------------------------------------------------------------------------------")
    time.sleep(8)
    print("You had just finished examining the plant when all of a sudden, you hear a loud crash and the lights turn off.")
    print(" You raise your voice and tell everyone present in the room to stay where they are.")
    print("A few minutes later, the lights turn back on.")
    print("Around you, you see everyone's face riddled with fear and anxiety, and you realize you don't have much time left.")
    print("You have to make a decision. You can search only 4 people's rooms before making the final call.")
    print("1. The twins, 2. Lady Crawley, 3. Butler, 4. Cook, 5. Gardener, 6. Lady's maid, 7. Two servants, 8. Chauffeur, 9. Tutor")
    pointc = [1,2,3,6]
    for i in range(4):
        c5 = int(input("Enter your choice: "))
        if c5 in pointc:
            global points
            points += 1
        if c5 == 1:
            print("At first, nothing seems off. But as you keep searching, you find an almost full bottle of turpentine sitting next to the oil paints.")
        elif c5 == 2:
            print("This room was more decadent. Nothing seems out of the blue.")
            print("But out of the corner of your eyes, you notice a worn out black leather belt, hanging on the coat rack next to the bed.")
        elif c5 == 3:
            print("You enter a small room in which the Butler stays. You search the room thoroughly.")
            print("Under the bed, you find a carved out book, in which lay a huge bundle of cash and the Lady Crawley's diamond ring.")
        elif c5 == 4:
            print("You search the entire quarters and the kitchen but are unable to find anything.")
        elif c5 == 5:
            print("You ran down the entire garden and searched his room to no avail.")
        elif c5 == 6:
            print("This room was the best out of the staff.")
            print("Upon searching, you find a small toolkit containing a wrench, a hammer, and a pair of wire cutting pliers.")
        elif c5 == 7:
            print("After searching the servant's quarter, you find nothing useful.")
        elif c5 == 8:
            print("There was nothing out of the ordinary in this room.")
        elif c5 == 9:
            print("There was nothing apart from a bunch of books.")
          
#best case points: 10  
def choice1():
    global name
    global points
    print("---------------------------------------------------------------------------------------------------------------------------")
    time.sleep(5)
    print("Your phone rings. Its a call from your superviser.")
    print("He says that you only have until the next morning to make an arrest, before he puts you on a different case.")
    print("You now have a very difficult choice to make.")
    print("1. The twins, 2. Lady Crawley, 3. Butler, 4. Cook, 5. Gardener, 6. Lady's maid, 7. Two servants, 8. Chauffeur, 9. Tutor")
    c6 = int(input("Select the person you want to arrest: "))
    if c6 == 1:
        points += 1
        print("You place the handcuffs on the little boy and girl and immediately they start crying.")
        print("The twins: We are so sorry! You don't understand, but it was all for a reason, please just hear us out!")
        if points >= 7:
            print("You have found enough evidence to hear their explanation and provide the adequate punishment.")
            print("The twins: It was all our father's fault. He ruined our perfect family. It started about an year ago...")
            print("He started drinking when we were about 10. We heard screams...our mother's screams, everynight.")
            print("It was horrifying. We even fought back once, but he beat us with his black leather belt, and threatened us.")
            print("He said that he would send us away from our mother if we told anyone. He mistreated everybody.")
            print("The last time this happened, we had had enough, we had to protect her...")
            print("We stayed in the armory until 5pm, and found the perfect weapon to use, a long silver dagger.")
            print("We then waited for the perfect oppurtunity, our father's evening nap.")
            print("We didnt mean to stab him so many times, but our emotions got the better of us.")
            print("But we had to clear the evidence, so we used turpentine from our art supplies, to wipe down everything we had touched, including the murder weapon.")
            print("We then hid the dagger in the plant and while I cried and pointed you towards the weapon, to remove suspicion, my brother powered off the lights to dispose off a dirty cloth.")
            print("We are genuinly hurt, but would do it all over again to protect our mother...")
            print("You can feel their pain and hurt, and take them into custody. After a few days of deliberation, the twins were let off with juvenile prison and social work to redeem themselves in a just period of time.")
            print("CONGRATS", name, "! YOU HAVE SOLVED THE MURDER MYSTERY")
            print("---------------------------------------------------------------------------------------------------------------------------")
        else:
            print("You have not collected enough evidence to hear their explanation and give a just punishment.")
            print("You arrest the twins and they are eventually sentenced to many many years in prison...")
            print("CONGRATS", name, "! YOU HAVE SOLVED THE MURDER MYSTERY")
            print("---------------------------------------------------------------------------------------------------------------------------")
            
    else:
        print("You arrest the suspect, but get a call at midnight...")
        print("It is a call from your superviser saying that the decision you took was incorrect as the suspect has a valid alibi.")
        choice2()
        
def choice2():
    global name
    global points
    print("---------------------------------------------------------------------------------------------------------------------------")
    time.sleep(7)
    print("A bead of sweat runs down your forehead. You have only one more shot at this.")
    print("You now have a very difficult choice to make.")
    print("1. The twins, 2. Lady Crawley, 3. Butler, 4. Cook, 5. Gardener, 6. Lady's maid, 7. Two servants, 8. Chauffeur, 9. Tutor")
    c7 = int(input("For the last time, select the person you want to arrest: "))
    if c7 == 1:
        print("You place the handcuffs on the little boy and girl and immediately they start crying.")
        print("The twins: We are so sorry! You don't understand, but it was all for a reason, please just hear us out!")
        if points >= 7:
            print("You have found enough evidence to hear their explanation and provide the adequate punishment.")
            print("The twins: It was all our father's fault. He ruined our perfect family. It started about an year ago...")
            print("He started drinking when we were about 10. We heard screams...our mother's screams, everynight.")
            print("It was horrifying. We even fought back once, but he beat us with his black leather belt, and threatened us.")
            print("He said that he would send us away from our mother if we told anyone. He mistreated everybody.")
            print("The last time this happened, we had had enough, we had to protect her...")
            print("We stayed in the armory until 5pm, and found the perfect weapon to use, a long silver dagger.")
            print("We then waited for the perfect oppurtunity, our father's evening nap.")
            print("We didnt mean to stab him so many times, but our emotions got the better of us.")
            print("But we had to clear the evidence, so we used turpentine from our art supplies, to wipe down everything we had touched, including the murder weapon.")
            print("We then hid the dagger in the plant and while I cried and pointed you towards the weapon, to remove suspicion, my brother powered off the lights to dispose off a dirty cloth.")
            print("We are genuinly hurt, but would do it all over again to protect our mother...")
            print("You can feel their pain and hurt, and take them into custody. After a few days of deliberation, the twins were let off with juvenile prison and social work to redeem themselves in a just period of time.")
            print("CONGRATS", name, "! YOU HAVE SOLVED THE MURDER MYSTERY")
            print("---------------------------------------------------------------------------------------------------------------------------")
        else:
            print("You have not collected enough evidence to hear their explanation and give a just punishment.")
            print("You arrest the twins and they are eventually sentenced to many many years in prison...")
            print("CONGRATS", name, "! YOU HAVE SOLVED THE MURDER MYSTERY")
            print("---------------------------------------------------------------------------------------------------------------------------")
            
    else:
        print("After making the final arrest, you take a good night's rest")
        print("In the morning, you go to gather everyone to give them the news, when you notice, one of the rooms are empty.")
        print("All the stuff has been cleared out, possibly escaped at night after the second arrest.")
        time.sleep(6)
        print("It was the twins' room. They had escaped into the night without a trace, and their motive and reasoning was left to imagination...")
        print("SORRY", name, "! YOU WERE UNABLE TO FIND THE KILLERS")
        print("---------------------------------------------------------------------------------------------------------------------------")
        
alibi()
murderweapon()
room_search()
choice1()

#ending

root2 = Tk()
   
root2.geometry("400x400")
canvas2 = Canvas( root2, width = 400, height = 400)
  
canvas2.pack(fill = "both", expand = True)

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   image = Image.open("Ending.png")
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(resized)
   canvas2.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
root2.bind("<Configure>", resize_image)


root.mainloop()
root2.mainloop()