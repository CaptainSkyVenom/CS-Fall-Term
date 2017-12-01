'''
Zhi Wei Gan
10/5/17

Spelunking Mania is a game where you are in a cave, and you have to
excape zombies to survive. You have 4 bombs to blow up walls so you
can escape them. The zombies find the shortest path to you no matter
which walls you blow up.

On My Honor, I have not recieved any unauthorized aid.


Curses Syntax and UI alignment from:
https://gist.github.com/claymcleod/b670285f334acd56ad1c


'''


from collections import deque
import sys
import curses
import numpy
import random
import os


width = 0
height = 0
enemies = 0
grid = []

#check if x and y are inbounds
def inbounds(x, y):
    return x >= 0 and x < height and y >= 0 and y < width

'''
Uses a random DFS to generate a tree on the 2d grid.
'''
def mapdraw(state):

    #For easier traversal of graph
    xvar = [0, 1, 0, -1]
    yvar = [1, 0, -1, 0]

    #stack for DFS
    q = []
    #origin
    q.append((0, 0))
    while len(q) != 0:
        cur = q.pop()
        x = cur[0]
        y = cur[1]
        flag = 0
        state[x][y] = 1
        count = 0
        #count = number of paths leading to this node
        for i in range(4):
            #if a cell is inbounds and it is currently a path, count += 1
            if inbounds(x + xvar[i],y + yvar[i]) and state[x+xvar[i]][y+yvar[i]] == 1:
                count += 1
            if count >= 2:
                state[x][y] = 2
                flag = 1

        #if more than 1 path is found, make the current cell a wall so a tree
        #structure is maintained
        if not flag:
            #choose a random direction each time to place on the stack
            randperm = numpy.random.permutation(4)
            for i in randperm:
                #if inbounds and cell has not been traversed, place onto stack
                if inbounds(x + xvar[i],y + yvar[i]) and state[x + xvar[i]][y + yvar[i]] == 0:
                    q.append((x+xvar[i], y+yvar[i]))

    return state

'''
Find shortest distance between enemy and player
'''
def shortestdist(eny, enx, ply, plx, stdscr):
    #For easier graph traversal
    xvar = [0, 1, 0, -1]
    yvar = [1, 0, -1, 0]

    #2d array of size height *  width, with all cells as 0 to check if cell has been visited
    visited = [[0 for i in range(width)] for j in range(height)]
    #2d array of parents for each cell size height *  width, with all cells as (0,0)
    parent = [[(0,0) for i in range(width)] for j in range(height)]

    #queue for BFS
    q = deque([])
    #append enemy position
    q.append((eny,enx))
    #parent of source = (-1,-1)
    parent[eny][enx] = (-1,-1)
    #BFS
    while(len(q) != 0):
        cur = q.popleft()
        y = cur[0]
        x = cur[1]
        #if player found, break
        if y == ply and x == plx:
            break

        visited[y][x] = 1
        for i in range(4):
            #if inbounds, not yet visited, and not a wall
            if inbounds(y + yvar[i],x + xvar[i]) and visited[y + yvar[i]][x + xvar[i]] == 0 and grid[y + yvar[i]][x + xvar[i]] == '*':
                q.append((y + yvar[i],x + xvar[i]))
                parent[y + yvar[i]][x + xvar[i]] = (y,x)

    #backtracking to find the next cell to go to
    par = parent[ply][plx]
    path = (ply,plx)

    while par != (eny,enx):
        path = par
        par = parent[par[0]][par[1]]



    return path

'''
Instruction Screen
'''
def instructionscreen(stdscr):
    k = 0
    stdscr.clear()
    stdscr.refresh()
    heightsc, widthsc = stdscr.getmaxyx()
    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    while (1):

        stdscr.clear()
        # Declaration of instruction strings
        title = "Instructions"
        instruction1 = "You have 4 bombs to blow walls up"
        instruction2 = "If you come within 1 block of a zombie,"
        instruction3 = "You will die"
        instruction4 = "W, A, S, D to place bombs UP, LEFT, DOWN, RIGHT"
        instruction5 = "Arrow Keys to Move"
        instruction6 = "Esc to Go Back"


        #instructions alignment and text
        start_x_title = int((widthsc // 2) - (len(title) // 2) - len(title) % 2)
        start_x_instruction1 = int((widthsc // 2) - (len(instruction1) // 2) - len(instruction1) % 2)
        start_x_instruction2 = int((widthsc // 2) - (len(instruction2) // 2) - len(instruction2) % 2)
        start_x_instruction3 = int((widthsc // 2) - (len(instruction3) // 2) - len(instruction3) % 2)
        start_x_instruction4 = int((widthsc // 2) - (len(instruction4) // 2) - len(instruction4) % 2)
        start_x_instruction5 = int((widthsc // 2) - (len(instruction5) // 2) - len(instruction5) % 2)
        start_x_instruction6 = int((widthsc // 2) - (len(instruction6) // 2) - len(instruction6) % 2)
        start_y = int((heightsc // 2) - 6)


        #writing of text onto instruction screen on Curses
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        stdscr.addstr(start_y, start_x_title, title)

        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        stdscr.addstr(start_y + 1, start_x_instruction1, instruction1)
        stdscr.addstr(start_y + 3, start_x_instruction2, instruction2)
        stdscr.addstr(start_y + 4, start_x_instruction3, instruction3)
        stdscr.addstr(start_y + 6, start_x_instruction4, instruction4)
        stdscr.addstr(start_y + 7, start_x_instruction5, instruction5)
        stdscr.addstr(start_y + 9, start_x_instruction6, instruction6)

        stdscr.refresh()

        k = stdscr.getch()

        #if escape is pressed, return back to the original
        if k == 27:
            return


'''
Main game function
'''
def game(stdscr):
    k = 0
    stdscr.clear()
    stdscr.refresh()
    heightsc, widthsc = stdscr.getmaxyx()
    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    #HAS SPACE BEEN PRESSED?
    flag = 1
    while (k != 32):

        stdscr.clear()
        # Declaration of instructions
        title = "Spelunking Mania"
        subtitle = "Press Space to Continue or Esc to quit."
        instructions = "Press M for Instructions"

        #alignment of titles
        start_x_title = int((widthsc // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((widthsc // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_instructions = int((widthsc // 2) - (len(instructions) // 2) - len(instructions) % 2)
        start_y = int((heightsc // 2) - 2)

        #writing of text
        stdscr.attron(curses.color_pair(1))
        stdscr.attron(curses.A_BOLD)

        stdscr.addstr(start_y, start_x_title, title)

        stdscr.attroff(curses.color_pair(1))
        stdscr.attroff(curses.A_BOLD)

        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 2, start_x_instructions, instructions)

        stdscr.refresh()

        k = stdscr.getch()
        #if m is pressed, then go to instructionscreen until it is returned.
        if k == ord('m') or k == ord('M'):
            instructionscreen(stdscr)

        if k == 27:
            return

    #game variables
    time = 0
    bombs = 4
    curpos = [0,0]
    start_x = int((widthsc // 2) - (width // 2) - width % 2)
    start_y = 3
    curpos[1] = start_x
    curpos[0] = start_y

    #spawn enemies at unique locations
    enemiesval = []
    for i in range(enemies):
        enemyypos = random.randint(height//2, height-1)
        enemyxpos = random.randint(width//2, width-1)

        while(grid[enemyypos][enemyxpos] != '*' and (enemyypos, enemyxpos) not in enemiesval):
            enemyypos = random.randint(height//2, height-1)
            enemyxpos = random.randint(width//2, width-1)

        enemiesval.append((enemyypos, enemyxpos))

    #main game loop
    while (flag):
        stdscr.clear()
        stdscr.refresh()
        #status messages and printing
        status = "You have survived for " + str(time) + " steps"
        bombstatus = "You have " + str(bombs) + " bombs!"

        #NUMBER OF STEPS
        time += 1

        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        stdscr.addstr(0, 0, status)
        stdscr.addstr(0, widthsc-len(bombstatus)-2, bombstatus)

        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        #print grid
        stdscr.attron(curses.color_pair(3))
        for i in range(height):
            stdscr.addstr(start_y+i, start_x, grid[i])

        stdscr.attroff(curses.color_pair(3))


        #keypress action flow
        if True:
            if k == curses.KEY_DOWN and inbounds(curpos[0]+1-start_y, curpos[1]-start_x) and grid[curpos[0]+1-start_y][curpos[1]-start_x] == "*":
                curpos[0] += 1
            elif k == curses.KEY_UP and inbounds(curpos[0]-1-start_y, curpos[1]-start_x) and grid[curpos[0]-1-start_y][curpos[1]-start_x] == "*":
                curpos[0] -= 1
            elif k == curses.KEY_RIGHT and inbounds(curpos[0]-start_y, curpos[1]+1-start_x) and grid[curpos[0]-start_y][curpos[1]+1-start_x] == "*":
                curpos[1] += 1
            elif k == curses.KEY_LEFT and inbounds(curpos[0]-start_y, curpos[1]-1-start_x) and grid[curpos[0]-start_y][curpos[1]-1-start_x] == "*":
                curpos[1] -= 1

            #bomb cardinal directions
            elif k == ord('w') and inbounds(curpos[0]-start_y-1, curpos[1]-start_x) and bombs > 0:
                grid[curpos[0]-start_y-1] = grid[curpos[0]-start_y-1][:curpos[1]-start_x] + "*" + grid[curpos[0]-start_y-1][curpos[1]-start_x+1:]
                bombs -= 1
            elif k == ord('a') and inbounds(curpos[0]-start_y, curpos[1]-start_x-1) and bombs > 0:
                grid[curpos[0]-start_y] = grid[curpos[0]-start_y][:curpos[1]-start_x-1] + "*" + grid[curpos[0]-start_y][curpos[1]-start_x:]
                bombs -= 1
            elif k == ord('s') and inbounds(curpos[0]-start_y+1, curpos[1]-start_x) and bombs > 0:
                grid[curpos[0]-start_y+1] = grid[curpos[0]-start_y+1][:curpos[1]-start_x] + "*" + grid[curpos[0]-start_y+1][curpos[1]-start_x+1:]
                bombs -= 1
            elif k == ord('d') and inbounds(curpos[0]-start_y, curpos[1]-start_x+1) and bombs > 0:
                grid[curpos[0]-start_y] = grid[curpos[0]-start_y][:curpos[1]-start_x+1] + "*" + grid[curpos[0]-start_y][curpos[1]-start_x+2:]
                bombs -= 1


        stdscr.attron(curses.color_pair(1))

        #Add enemies to their locations
        for i in range(enemies):
            stdscr.addstr(start_y+enemiesval[i][0], start_x+enemiesval[i][1], "█")

        #Check if player is dead
        for i in range(enemies):
            if abs(curpos[0]-start_y - enemiesval[i][0]) <= 1 and abs(curpos[1]-start_x - enemiesval[i][1]) == 0:
                flag = 0
            if abs(curpos[0]-start_y - enemiesval[i][0]) == 0 and abs(curpos[1]-start_x - enemiesval[i][1]) <= 1:
                flag = 0

        #Next Location for Enemies
        for i in range(enemies):
            (pos1, pos2) = shortestdist(enemiesval[i][0], enemiesval[i][1],curpos[0]-start_y, curpos[1]-start_x, stdscr)
            enemiesval[i] = (pos1, pos2)
        stdscr.attroff(curses.color_pair(1))



        stdscr.move(curpos[0], curpos[1])

        stdscr.refresh()

        k = stdscr.getch()

        if k == 27:
            flag = 0


    #endscreen
    flag = 1
    while (flag):

        #DISPLAYING DATA
        stdscr.clear()
        title = "Spelunking Mania"
        subtitle = "Your Score was " + str(time)
        instructions = "Thanks for Playing! Press Esc to Exit"

        start_x_title = int((widthsc // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((widthsc // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_instructions = int((widthsc // 2) - (len(instructions) // 2) - len(subtitle) % 2)
        start_y = int((heightsc // 2) - 2)

        stdscr.attron(curses.color_pair(1))
        stdscr.attron(curses.A_BOLD)

        stdscr.addstr(start_y, start_x_title, title)

        stdscr.attroff(curses.color_pair(1))
        stdscr.attroff(curses.A_BOLD)

        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 2, start_x_instructions, instructions)

        stdscr.refresh()

        k = stdscr.getch()
        #if ESC is pressed, return to main, and quit.
        if k == 27:
            return 0


'''
ERROR CHECKING
'''
def check(a,b,c, widthsc, heightsc):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        return not (a > 0 and a <= widthsc and b > 0 and b <= heightsc and c > 0 and c <= 5)
    except ValueError:
        print("Wrong Data Type")
        return 1


def main():
    global width
    global height
    global enemies
    global grid


    '''

    ERROR CHECKING

    '''
    heightsc, widthsc = os.popen('stty size', 'r').read().split()
    heightsc = int(heightsc)
    widthsc = int(widthsc)
    width2 = input("Please enter the width of the grid less than " + str(widthsc - 10) + " and more than 0: ")
    height2 = input("Please enter the width of the grid less than " + str(heightsc - 10) + " and more than 0: ")
    enemies2 = input("Please enter the width of the grid less than 5 and more than 0: ")
    while(check(width2, height2, enemies2, widthsc-10, heightsc-10)):
        print("Please enter the correct data types within the boundaries")
        width2 = input("Please enter the width of the grid less than " + str(widthsc - 10) + " and more than 0: ")
        height2 = input("Please enter the width of the grid less than " + str(heightsc - 10) + " and more than 0: ")
        enemies2 = input("Please enter the width of the grid less than 5 and more than 0: ")
    width = int(width2)
    height = int(height2)
    enemies = int(enemies2)
    state = [[0 for i in range(width)] for j in range(height)]

    mapdraw(state)
    #make grid
    for i in range(len(state)):
        aa = ""
        for j in state[i]:
            if j == 1:
                aa += "*"
            else:
                aa += "█"
        grid.append(aa)
    #execute game
    curses.wrapper(game)


#FOR PERSONAL CONVENIENCE AND OCD-NESS
try:
    main()
except KeyboardInterrupt:
    sys.exit()
