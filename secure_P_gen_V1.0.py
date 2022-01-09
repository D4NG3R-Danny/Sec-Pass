import secrets, string, time, sys
#Author:D4NG3R-D4NNY Github:D4NG3R-D4NNY

'''Password generator: length of password [int] , 
                       amounts of password [int],
                       additional characters to passwords'''
print("")
print("                     ▌║█║▌│║▌│║▌║▌█║sec-pass▌│║▌║▌│║║▌█║▌║█")
time.sleep(1)
print(" A Password Generator which uses the secrets and string library from python")
print("")
print("")
time.sleep(1)

#Input-block
numlet = string.ascii_letters + string.digits #a-z,A-Z,0-9
extra = str(input("What special characters do you want?(e.g. % () ? \ | _ - = )\n")).replace(" ", "") #extra removes space
length = int(input("How long should your password be? Give me a number...(0,1,2 --> 256)\n")) #Currently no barrier of how long or how many
amount = int(input("How many passwords you wanna have? Give me a number...(0,1,2 --> 100)\n")) 
print("\n")

#Prints every elements of the list seperatly in a line (used at the end)
def takein_list(x:list):
    for elements in x:
        print(*elements)

passlist = []
#Generate Password. First loop for amounts of passwords. Second for length of password.
def pass_gen(numlet: str,length: int,extra: str, amount: int)-> list:
    for i in range(0,amount): 
        password = ""
        for i in range(0,length):
            password += secrets.choice(numlet + extra)
        passlist.append(password)
    return passlist

def visual_gen(take:list): #Output of password and erasing for visual entertainment
    sleepy = 0.2
    if len(take) > 500:
        sleepy = 0.001
    elif len(take) > 100:
        sleepy = 0.01
    for index in take:
        print(*index,end="",flush=True)
        time.sleep(sleepy)
        sys.stdout.write("\b"*length*2)
    print("Generated",amount,"Passwords.                          ")
    #sys.stdout.write("\b"*length*2)

def my_enumerate(take:list):
    for i in range(1,len(take)+1):
        if i > 9:
            print(f"{i}:{take[i - 1]}")
        else:
            print(f"{i}: {take[i - 1]}")

result = pass_gen(numlet,length,extra,amount)

visual_gen(result)
time.sleep(1)
print("",end="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#sys.stdout.write("\b" * 50) 
#^^^^^^^^
#why doesn't this works
my_enumerate(result)
#alternativ = takein_list(enumerate(result,1))
