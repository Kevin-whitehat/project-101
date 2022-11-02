import random
response = str("y")
while response =="y":
    no = random.randint(1,6)
    if(no==1):
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    elif(no==2):
        print("[0    ]")
        print("[     ]")
        print("[    0]")
    elif(no==3):
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
    elif(no==4):
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    elif(no==5):
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    else:
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
    response = str(input("enter y to continue, enter n to stop"))