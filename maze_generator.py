import random

def generate_maze_with_obstacles(row, col) :

    maze = [[" "] * col for i in range (row)]
    
    for i in range(row):
        for j in range(col):
            if i==0 or j==0 or j==col-1 or i == row-1:
                maze[i][j]= "#" 
                
    for _ in range (1, (row+col)*2):
        i, j = random.randrange(0,row-1), random.randrange(0,col-1)
        maze[i][j] = "#"
        
    return maze
        
        
def set_start_and_end(maze, startRow, startCol, endRow, endCol):
    maze[startRow][startCol]= "O"
    maze[endRow][endCol]= "X"
    return maze
    
