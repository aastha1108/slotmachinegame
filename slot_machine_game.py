import random
print("Welcome to the slot machine game")
while True:
    amount=float(input("Enter your starting balance: $"))
    if amount<=0:
        print("Please enter a amount>0")
        continue
    else:
        break
bet=0
earned=0
current_balance=amount
spins = 0
while True:
    print(f"Total spins: {spins}")
    print(f"You start with a balance of ${current_balance}")
    
    bet=float(input("Enter your betting amount: "))
    if bet>current_balance :
        print("Not enough balance for this bet")
        continue
    if bet<=0:
        print("Enter a positive bet")
        continue
    spins+=1
    emojis=["💔","🥀","😭","🥰","😂","✨"," 💫"]
    list_emoji=[]

    for i in range(3):
        list_emoji.append(random.choice(emojis))
    print("|".join(list_emoji))
    set_emoji=set(list_emoji)
    if len(list_emoji)-len(set_emoji)==0:
        earned=0
        print("You won nothing")
    elif len(list_emoji)-len(set_emoji)==1:
        earned=2*bet
        print(f"You earned {earned}")
    else:
        earned=10*bet
        print(f"You earned {earned}")
    current_balance=current_balance-bet+earned
    if current_balance<=0:
        print("You areout of money")
        print(f"Total spins: {spins}")
        break
    again = input("Play again? (y/n): ").strip().lower()

    if again != "y":
        print(f"Total spins: {spins}")
        print(f"You leave with ${current_balance}")
        break