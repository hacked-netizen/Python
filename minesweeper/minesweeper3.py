# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:03:52 2019

@author: UTKARSH
"""

#import 
import string
import random
import time as tim
import pickle


#create grid
def create_grid(size,lastcell,numberofmines):
    grid = []
    for i in range(size):
        row = ['0']*size
        grid.append(row)
    mines = create_mines(grid,lastcell,numberofmines,size)
    p = surrounding(grid,size)
    p.numberofsurrounding(grid,size)
    return (grid,mines)


#show the grid 
def showgrid(grid,size):
    horizontal = ' -'+size*'----'
    collum = '   '
    #writes the collmum numbers
    for i in string.ascii_uppercase[:size]:
        collum += (i+ '   ')
    print (collum,'\n',horizontal)
    # writes row numbers
    for idx,i in enumerate(grid, start=1):
        row = str(idx)
        row += '|'
        for j in i:
            row = row+' '+j+' |'
        print (row+'\n'+horizontal)


#generated random cordinates 
def generate_cordinate(size):
    a = random.randint(0,size-1)
    b = random.randint(0,size-1)
    return (a,b)


#class fro surrounding
class surrounding(object):
    def __init__(self,grid,size):
        self.grid = grid
        self.size = size


    #creates a list with the surrounding cell for every cell
    def surrounding_cells(self,row_num,col_num,size):
        surronding = []
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                elif -1<row_num+i<size and -1<col_num+j<size:
                    surronding.append((row_num+i,col_num+j))
        return (surronding)


    #checks how many is mines in the surromding cells
    def numberofsurrounding(self,grid,size):
        for row_num,row in enumerate(grid):
            for col_num,col in enumerate(row):
                if col!='*':
                    #finds value of surrounding cell
                    values = [grid[r][c] for r,c in self.surrounding_cells(row_num, col_num,size)]
                    # counts how many are mines
                    grid[row_num][col_num] = str(values.count('*'))


# Generate mines
def create_mines(grid,lastcell,numberofmines,size):
    mines = []
    for i in range(numberofmines):
        cell = generate_cordinate(size)
        while cell==(lastcell[0],lastcell[1]) or cell in mines:
            cell = generate_cordinate(size)
        mines.append(cell)
    for i,j in mines: grid[i][j] = '*'
    return mines


#"shows the choose cell
def showcell(grid,showngrid,row_num,col_num,size):
    #if you pick already shown cell
    if showngrid[row_num][col_num]!='-':
        return
    #shows the cell
    showngrid[row_num][col_num] = grid[row_num][col_num]
    #if the cells value is 0 controll nearby cells
    if grid[row_num][col_num] == '0':
        p = surrounding(grid,size)
        for r,c in p.surrounding_cells(row_num,col_num,size):
            showcell(grid,showngrid,r,c,size)


# replay
def replay():
    val = input('What to go to mainmenu?(yes or no):')
    if val.lower() == 'yes':
        mainmenu('mainmenu')
    elif val.lower() == 'no':
        print('bye')
        quit()
    else:
        print('\nonly yes or no')
        replay()


#function for flags
def putflag(showngrid,row_num,col_num,flags):
    # adds flag
    if showngrid[row_num][col_num]=='-':
        showngrid[row_num][col_num] = 'F'
        flags.append((row_num,col_num))
    #remove flag
    elif showngrid[row_num][col_num]=='F':
        showngrid[row_num][col_num] = '-'
        flags.remove((row_num,col_num))


#function for picking the size/ number of mines 
def pickvalues():
    size = goodvalues(4,10,message= '\nPick size of grid(4-9):')
    numberofmines = goodvalues(size, ((size**2) -5), message= 'the number of mines has to be between ' + str(size) + ' and '+ str((size**2-6))+ '\nhow many mines::' )
    return size,numberofmines


#checks the values, (size/numberofmines)
def goodvalues(min,max,message):
    a = False
    while a == False:
        try:
            value1 = int(input(message))
            if value1 not in range(min,max):
                a = False
            if value1 in range(min,max):
                a = True
        except ValueError:
            print("\nchoose an integer\n")
            a = False
    return (value1)

def name(message):
    username = input(message)
    if len(username) <= 0 or len(username) >10:
        name('Pick a username:')
    return username


#main programme
def play():
    username = name('pick a username(1-10signs):')
    size,numberofmines = pickvalues()
    start_time = tim.time()
    showngrid = [['-' for i in range(size)] for i in range(size)]        #creates a copy of the playing field without mines
    showgrid(showngrid,size)
    first_round = True
    flags = []
    while True:
        while True:
            flag = False
            lastcell = input('pick cell: ')
            try:
                if lastcell[2].lower() == 'f':
                    flag = True
            except IndexError:
                pass
            try:
                #Convert the coordinates to numbers
                lastcell = (int(lastcell[1])-1,string.ascii_lowercase.index(lastcell[0].lower()))
                break
            except (IndexError,ValueError):
                showgrid(showngrid,size)
                print ("can't choose that cell")

        #creates the playing field after the first round
        if first_round == True:
            first_round = False
            grid,mines = create_grid(size,lastcell,numberofmines)

        row_num = lastcell[0]
        col_num = lastcell[1]

        #adds flags
        if flag == True:
            putflag(showngrid,row_num,col_num,flags)

        else:
            try:
                if grid[row_num][col_num] == '*':
                    result('Game Over',grid,showngrid,start_time,numberofmines,size,username)

                else:
                    showcell(grid,showngrid,row_num,col_num,size)
            except IndexError:
                print("\ncan't choose that cell\n")

        #checks for victory
        controll(grid,showngrid,size,numberofmines,start_time,username,flags,mines)

        showgrid(showngrid,size)

#function to check for victory
def controll(grid,showngrid,size,numberofmines,start_time,username,flags,mines):
    empty_cells = 0
    cellswithmines = 0
    for x in range(len(showngrid)):
        y = (showngrid[x].count('-'))
        empty_cells += y
    for x in range(len(grid)):
        z = (grid[x].count('*'))
        cellswithmines += z
    if empty_cells == cellswithmines or set(flags) == set(mines):
        result('YOU WON',grid,showngrid,start_time,numberofmines,size,username)


#shows the reuslt (lose/win)
def result(result,grid,showngrid,start_time,numberofmines,size,username):
    if result == 'Game Over':
        print('Game Over!')
        showgrid(grid,size)
        replay()
    if result == 'YOU WON':
        print('*********** YOU WON! ************')
        showgrid(showngrid,size)

        score(start_time,numberofmines,size,username)


# calculates the score
def score(start_time,numberofmines,size,username):
    finish_time = tim.time()
    time = start_time - finish_time
    user_score = (int((1000 * ((int(numberofmines))**2 / (int(size))) - (1.5 * time))), username)
    highscore(user_score)


#Opens highscore and adds you on the list (as per scores)
def highscore(user_score):
    
    with open ('high_scorelist.dat','rb') as file:
         high_scorelist = pickle.load(file)
    if user_score[0] > high_scorelist[len(high_scorelist)-1][0]:
        print ("YOU MADE IT!\n\n")
        high_scorelist.append(user_score)
        high_scorelist.sort(reverse=True)
        del high_scorelist[len(high_scorelist)-1]
        with open('high_scorelist.dat','wb') as file:
            pickle.dump(high_scorelist,file)
        show_highscore(high_scorelist)
        return (high_scorelist)
    else:
       show_highscore(high_scorelist)


#prints the highscore table
def show_highscore(high_scorelist):
    print('****highscore***\n\n')
    print('|        name        |    score    |')
    for i in range(10):
        print('| ',high_scorelist[i][1],' '*(17-len(high_scorelist[i][1])), end='|')
        print(high_scorelist[i][0], ' ' *(12- len(str(high_scorelist[i][0]))), end= '|\n')
    replay()


#mainmenu
def mainmenu(message):
    print(message)
    a = str(input('1. Helpmenu\n2. play\n3. Highscore\n4. quit'))
    if a == '1':
        help()
    elif a =='2':
        play()
    elif a =='3':
        highscore(user_score=(0,'test'))
    elif a == '4':
        print('BYE BYE!')
        quit()
    else:
        mainmenu(message='choose 1-4')


#helpmenu
def help():
    print('what can i help you with?')
    while True:
        try:
            x = int(input('1. bla\n2. blar\n3. bla\n4. play'))
            if x == 1:
                a = input(('xyz '))
            elif x == 2:
                a = input(('xyz'))
            elif x == 3:
                a = input('xyz')
            elif x == 4:
                mainmenu(message='here we go')
        except ValueError:
            print('\nchoose\n')


#opens mainmenu
mainmenu(message='MINeSWeeper!')
