print(""""
***********************************************************************
TOOTHPICKS GAME
This is a two player game.
We start with 13 toothpicks
Each player takes turns removing 1, 2, or 3 toothpicks at a time.  
The person who removes the last toothpick wins.
**********************************************************************
""")

toothpicks = 13

p_1 = input("Enter player one's name: ")
p_2 = input("Enter player two's name: ")
current = p_1

while toothpicks > 0:
    p_pick = int(input(f"{current}, how many toothpicks do you take? "))
    while p_pick >= 4:
        p_pick = int(input("You can only take 1, 2 or 3:"))
    toothpicks -= p_pick
    if toothpicks <= 0:
        print(f"\n{current} wins!")
    else:
        print(f"\nThere are {toothpicks} toothpicks left")
        print("| " * toothpicks)
    if current == p_1:
        current = p_2
    else:
        current = p_1

print("\nGAME OVER!")