print("Welcome to the GC Fruit Market!")
name = input("What's your name? ")
answer = "y"
apple_num = 0
grape_num = 0
orange_num = 0
while answer == "y":
    print("Welcome " + str(name) +"! ")
    print("1. Apple $2")
    print("2. Grape $1")
    print("3. Orange $3")
    fruit = input("Which fruit would you like to buy? ")
    if fruit == "1":
        print("You bought 1 apple at $2")
        apple_num += 1
    if fruit == "2":
        print("You bought 1 grape at $1")
        grape_num += 1
    if fruit == "3":
        print("You bought 1 orange at $3")
        orange_num += 1
    buy_more = input("Would you like to buy another piece of fruit? y/n ")
    answer = buy_more
print("Order for " + str(name))
print(str(apple_num) + " apple(s) at $2 apiece")
print(str(grape_num) + " grape(s) at $1 apiece")
print(str(orange_num) + " orange(s) at $3 apiece")
sub_total = (apple_num * 2) + (grape_num * 1) + (orange_num * 3)
print("Sub Total: $" + str(sub_total))
tax = sub_total/20
print("5% Tax: $" + str(tax))
total = sub_total + tax
print("Total: $" + str(total))
