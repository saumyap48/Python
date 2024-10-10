print("Welcome to saumya game!")
name=input("what is your name? ")
age=int(input("What is your age? "))
health=15
if age>=18:
    print("you are old enough to play!")

    wants_to_play=input("do you want to play ?").lower()
    if wants_to_play=="yes":
         print("you are starting with", health,"health")
         print("lets play !")
      
         left_or_right=input("first choice.... left or Right(left/Right) ?")
         if left_or_right== "left":
             ans=input("Nice,you follow the path and reach a lake.... do you swim across or go around (across/around)? ")
      
             if ans == "around":
                 print("you went around and reached the other side of the lake")
             elif ans =="across":
                 print("you managed to get across,but were but by a fish and lost 5 health. ")
                 health-=5
                 ans = input("You notice a house and a river.Which do you want to go(river/house)?")

                 if ans=="house":
                     print("You got to the house and are greted by the owner he does not like you and you lost the health")
                     health-=5

                     if health<=0:
                      print("you now have 0 health and you lost the game")
                     
                     else:
                      print("you have survived you win")

                 else:
                    print("you fell in the river and lost....game")
         else:
           print("you fell down lost the game")

    else:
      print("see you later")
else:
      print("you are not old enough to play....")
     