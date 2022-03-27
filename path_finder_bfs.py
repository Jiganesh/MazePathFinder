import curses
import queue
import time 
from maze_generator import *
from curses import wrapper

maze = generate_maze_with_obstacles(15,15)
maze = set_start_and_end( maze, 0, 4, -1, -3)

def find_start(maze, start):    
    for i , row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i,j
        
def find_end(maze, end):    
    for i , row in enumerate(maze):
        for j, value in enumerate(row):
            if value == end:
                return i,j

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    
    for i , row in enumerate(maze):
        for j , value in enumerate(row):
            
            if (i,j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)
                
                
def find_path(maze, stdscr): # bfs Algorithm
    
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    
    q = queue.Queue()
    visited = set()
    
    q.put((start_pos , [start_pos]))
    
    while q:
        current_pos , path = q.get()
        row, col = current_pos
        
        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.05)
        stdscr.refresh()
        
        if maze[row][col]==end:
            return path
        
        neighbors= find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            
            r, c = neighbor
            if maze[r][c] == "#":
                continue
            new_path = path+[neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)


def find_neighbors(maze, row, col):
    
    neighbors =[]
    
    if row >0 :
        neighbors.append((row-1, col))
    if row+1 <len(maze):
        neighbors.append((row+1, col))
    if col>0:
        neighbors.append((row, col-1))
    if col+1< len(maze[0]):
        neighbors.append((row, col+1))
    if row>0 and col>0:
        neighbors.append((row+1, col+1))
    if row+1< len(maze):
        neighbors.append((row-1, col-1))
        
    return neighbors
            
               
def main (stdscr) : # stdscr is standard output screen
    # How to initialize colors 
    
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) # (id, foreground color , background color)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    
    GREEN = curses.color_pair(3)
   
    endAt =  find_end (maze, "X")
    startAt = find_start(maze, "O")
    
    find_path(maze, stdscr)
    stdscr.addstr(endAt[0], endAt[1]*2, "X", GREEN)
    stdscr.addstr(startAt[0], startAt[1]*2,"O", GREEN)
    stdscr.getch()
    
wrapper(main) # pass function what this does is initializes curses module and passes stdscr object and executes it
    
    
    
    