
n = input("Enter a number")

dic = {
    "1" : "ones",
    "2" : "twos",
    "3" : "threes",
    "4" : "fours",
    "5" : "fives",
    "6" : "sixes",
    "7" : "sevens",
    "8" : "eights",
    "9" : "nines",
    "10": "tens"
}
current_num = ""
for i in range(1,11):
    mult = i*int(n)
    current_num = str(i) + " " +dic[n] + " are " + str(mult) +"\n"
    print(current_num)