low = 0
high = 100
ans = "no"
print("Please think of a number between 0 and 100!")
while(ans!="c"):
    mid = (low+high)/2
    print("Is your secret number "+str(mid))
    print("Enter 'h' to indicate the guess is too high."),
    print("Enter 'l' to indicate the guess is too low."),
    print("Enter 'c' to indicate I guessed correctly."),
    ans = raw_input()
    if(ans=="h"):
        high = mid
    elif(ans=="l"):
        low = mid
    elif(ans=="c"):
        print("Game over. Your secret number was: "+str(mid))
    else:
        print("Sorry, I did not understand your input.")
        