Create a Environment

```

virtualenv env\
.env\Scripts\activate

```

Curses Introduction

```


def main (stdscr) : # stdscr is standard output screen
    
    
    # How to initialize colors 
    
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) # (id, foreground color , background color)
    blue_and_black = curses.color_pair(1)
    
    # How the curses module work
    
    stdscr.clear()
    stdscr.addstr(5 , 0, "Hello World !", blue_and_black) # (row, column, text, color)
    stdscr.refresh()
    stdscr.getch() # get character
    
wrapper(main) # pass function what this does is initializes curses module and passes stdscr object and executes it
    

```

[Resource To Learn about DFS Algorithm](https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/)

[Resource To Learn about BFS Algorithm](https://www.geeksforgeeks.org/depth-first-traversal-dfs-on-a-2d-array/)

[Resource To Learn about Curses (Tech With Tim)](https://www.youtube.com/watch?v=Db4oc8qc9RU&ab_channel=TechWithTim)
