import time
print("An ivy covered manor. The stench of blood and betrayal hangs in the still mountain air. A death was discovered at Rook Estate.")
print("Open wounds gasping for air, his marred body was laid on the bed. The Lord of the Manor, Sir William Crawley, was murdered.")
print("You, a consulting detective, arrive at the estate the following morning at the Lady's behest.")
print("Butler: Welcome, detective. What should we call you?")
name=input("Type your name: ")
print("Butler: Lady Crawley awaits your presence in the parlour.")
print("You go up to the parlour. You find Lady Crawley seated there, crying into a handkerchief.")
print("Do you:")
print("1. Give your condolences, 2. Accuse her of killing her husband")
c1=int(input("Enter your choice: "))
if c1==1:
    print("Lady Crawley thanks you and invites you to start taking the statements of the manor's inmates.")
else:
    print("Lady Crawley cries even harder and leaves the room, leaving you to call upon each person of the house in turn to take their statements.")
print("Before the investigation here's the facts of the case: ")
print("The Lord died of a heart attack in the evening at 5 pm. He was alone and reading in bed when he felt the attack coming and cried out. No one heard him.")
print("He was only discovered when the butler came up an hour later to bring him his tea.")
time.sleep(4)
print("The investigation begins, select the suspect to know their alibis.  ")
print("1. Kids, 2. Lady Crawley, 3. Butler, 4. Cook, 5. Gardener, 6. Lady's maid, 7. Two servants, 8. Chauffeur, 9. Tutor")
print('choose option 10 to proceed to the motives.')
#maybe add classes for each choice to make it seem more sophisticated
def alibi():
    global x
    x=[
 "The kids were dressing up in armour in the armory at 5 pm. The Lady's maid can back this up because she heard a crash around 5.30 pm",
 "Lady Crawley was stitching clothes in the parlour. Nobody can back this alibi up.",
 "The Butler was reading the newspaper in his room. Nobody can back this alibi up.",
 "The cook was in the kitchen preparing supper. Both the servants can back this up as they were helping her.",
 "The gardener was in the backyard fields pruning some bushes. Lady Crawley can back this up as she saw him from her window from time to time.",
 "The Lady's maid was getting her Lady tea from the kitchen. Lady Crawley can back this up as she saw her around 5.15 pm.",
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
    print("Now that we know the various alibis, let's investigate their motives.")
    print("1. Kids, 2. Lady Crawley, 3. Butler, 4. Cook, 5. Gardener, 6. Lady's maid, 7. Two servants, 8. Chauffeur, 9. Tutor")
    print("Choose option 10 if you are finished with the motives.")

def motives():
    #some storyline about whatever happened after the alibi thingy
    y=['The Lord was abusive and violent when drunk but it was hushed up',
       'The Lord was abusive and violent when drunk and also she’d get all his money', 
       'The Lord was very rude to him most of the time',
       'None',
       'None',
       'Hates the Lord bc he’s abusive to her Lady',
       'None',
       'None',
       "The Lord never paid him on time"
]
    c3=int(input("Enter your choice:"))
    if c3==1:
        print(y[0])
        motives()
    elif c3==2:
        print(y[1])
        motives()
    elif c3==3:
        print(y[2])
        motives()
    elif c3==4:
        print(y[3])
        motives()
    elif c3==5:
        print(y[4])
        motives()
    elif c3==6:
        print(y[5])
        motives()
    elif c3==7:
        print(y[6])
        motives()
    elif c3==8:
        print(y[7])
        motives()
    elif c3==9:
        print(y[8])
        motives()
    elif c3==10:
        return
    else:
        print("Invalid choice. Please enter a number from 1-9")
        motives()

alibi()
motives()

print("One of the children rushes into the room, crying. You ask what happened calmly.")
print("The child silently points to the Great Hall and runs out crying.")
print("You follow her out into the Hall. You see a glint of silver from one of the potted plants.")

def choicenew():    
 print("Do you, 1. Check the stem or 2. Check the root?")
 c4=int(input("Enter your choice: "))
 if c4==1:
    print("You find blood on the leaves but nothing else.")
    choicenew()
 else: 
    print("You find a long, silver dagger buried among the roots, with blood still crusted on its blade. This is your murder weapon.")

choicenew()