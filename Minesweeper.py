from random import randint
def create():
    global value_matrix, game_matrix, opened, chk_flag
    value_matrix=[[0 for i in range(12)] for j in range(12)]
    game_matrix=[[' ' for i in range(12)] for j in range(12)]
    opened=[[False for i in range(12)]for j in range(12)]
    chk_flag=[[False for i in range(12)]for j in range(12)]

def mine_place():
    for x in range(15):
        r=randint(1,10)
        c=randint(1,10)
        while value_matrix[r][c]=='M' or (r,c) in store_values:
            r=randint(1,10)
            c=randint(1,10)
        value_matrix[r][c]='M'

def place_values():
    for r in range(1,11):
        for c in range(1,11):
            if value_matrix[r][c]=='M':
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if value_matrix[i][j]!='M':
                            value_matrix[i][j]+=1
def disp():
    print()
    st = "   "
    for i in range(10):
        st = st + "     " + str(i + 1)
    print(st)
 
    for r in range(10):
        st = "     "
        if r==0:
            for col in range(10):
                st=st + "______" 
            print(st)
 
        st = "     "
        for col in range(10):
            st = st + "|     "
        print(st + "|")

        if r == 9:
            st = " " + str(r + 1) + "  "
        else:
            st = "  " + str(r + 1) + "  "
        for col in range(10):
            st = st + "|  " + str(game_matrix[r+1][col+1]) + "  "
        print(st + "|") 
 
        st = "     "
        for col in range(10):
            st = st + "|_____"
        print(st + '|')
    print()
   

def click_value(r,c):
    opened[r][c]= True
    value=value_matrix[r][c]
    game_matrix[r][c]=value_matrix[r][c]
    if value=='M':
        disp_mines()
    elif value==0:
        click_value_zero(r,c)
    

def click_value_zero(r,c):
    if 0<r<11 and 0<c<11:
        opened[r][c]= True
        game_matrix[r][c]=value_matrix[r][c]
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                if value_matrix[i][j]==0 and opened[i][j]==False and chk_flag[i][j]==False:
                    click_value_zero(i,j)
                elif value_matrix[i][j]!=0 and opened[i][j]==False and chk_flag[i][j]==False:
                    click_value(i,j)

def disp_mines():
    for i in range(1,11):
        for j in range (1,11):
            if value_matrix[i][j]=='M':
                game_matrix[i][j]='M'
                opened[i][j]=True
def game_status():
    for i in range(1,11):
        for j in range(1,11):
            if value_matrix[i][j]=='M' and opened[i][j]==True:
                print('\t\t\tGAME OVER')
                return True
    for i in range(1,11):
        for j in range(1,11):
            if value_matrix[i][j]!='M' and opened[i][j]== False:
                return False
    else:
                print('\t\t\tGAME WON!!!')
                return True

def place_flag(r,c):
    game_matrix[r][c]='F'
    chk_flag[r][c]=True
    

create()
disp()

move=0
store_values=[]
while game_status()==False:
    r=int(input("Enter Row Number; "))
    c=int(input("Enter Column Number; "))
    while r<1 or r>10 or c<1 or c>10:
        print("Invalid Input")
        r=int(input("Enter Row Number; "))
        c=int(input("Enter Column Number; "))
    F=str(input("Place Flag(y/n)"))
    if F=='y':
        place_flag(r,c)
    elif F=='n':
        move+=1
        if move==1:
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    store_values+=[(i,j)]
            mine_place()
            place_values()
        elif chk_flag[r][c]==True:
            print("TILE ALREADY FLAGGED")
            open_tile=str(input("Place Flag(y/n)"))
            if open=='y':
                pass
            if open=='n':
                chk_flag[r][c]==False
                continue
        click_value(r,c)
    disp()



