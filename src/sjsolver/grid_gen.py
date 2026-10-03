from sjsolver.node import Node

DEFAULT = ["a", "l", "p", "u", "t", "h", "l", "n", "v", "e", "e", "r", "l", "u", "i", "o"]

def generate_grid(h=4, w=4, chars=DEFAULT)->list:
    '''
    Generates a playing grid based on given values, return the list of nodes

    Arguments:
        h (int): height of map
        w (int): width of map
        chars (list): list of node values

    Returns:
        nodes (list): 2D list of generated nodes
    '''
    assert isinstance(h, int)
    assert isinstance(w, int)
    assert isinstance(chars, list)
    assert len(chars) == h*w 

    grid = [[Node() for _ in range(w)] for _ in range(h)]
   
    for y in range(h):
        for x in range(w):
            node = grid[y][x]
            node.pos = [x, y]
            node.char = chars[y * w + x]
            
            # Link cardinal neighbors (N, E, S, W)
            if y > 0:
                node.n = grid[y - 1][x]
            if y < h - 1:
                node.s = grid[y + 1][x]
            if x > 0:
                node.w = grid[y][x - 1]
            if x < w - 1:
                node.e = grid[y][x + 1]

            # Link diagonal neighbors (NE, SE, SW, NW)
            if y > 0 and x < w - 1:
                node.ne = grid[y - 1][x + 1]
            if y < h - 1 and x < w - 1:
                node.se = grid[y + 1][x + 1]
            if y < h - 1 and x > 0:
                node.sw = grid[y + 1][x - 1]
            if y > 0 and x > 0:
                node.nw = grid[y - 1][x - 1]

    return grid


if __name__ == "__main__":
    grid = generate_grid()

    # Print the positions and neighbors of each node
    for row in grid:
        for node in row:
            print(f"Node at {node.pos}:")
            print(f"  N: {node.n.pos if node.n else None}")
            print(f"  E: {node.e.pos if node.e else None}")
            print(f"  S: {node.s.pos if node.s else None}")
            print(f"  W: {node.w.pos if node.w else None}")
            print(f"  NE: {node.ne.pos if node.ne else None}")
            print(f"  SE: {node.se.pos if node.se else None}")
            print(f"  SW: {node.sw.pos if node.sw else None}")
            print(f"  NW: {node.nw.pos if node.nw else None}")
    
