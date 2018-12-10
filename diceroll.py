import random
min = 1
max = 6

roll_again = "Sure!"

while roll_again == "Sure!" or roll_again == "sure":
    print "Rolling dice..."
    print "You got...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll again?")
