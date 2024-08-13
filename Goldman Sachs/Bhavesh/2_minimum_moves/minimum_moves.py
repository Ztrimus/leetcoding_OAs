'''
-----------------------------------------------------------------------
File: Bhavesh/minimum_moves.py
Creation Time: Aug 13th 2024, 2:36 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

from collections import deque

def getMinimumMoves(maze, k):
    n, m = len(maze), len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Check if the start or end cell is an obstacle
    if maze[0][0] == 1 or maze[n-1][m-1] == 1:
        return -1
    
    # BFS initialization
    queue = deque([(0, 0, 0)])  # (row, col, moves)
    visited = set((0, 0))
    
    while queue:
        i, j, moves = queue.popleft()
        
        # If we reached the end cell
        if (i, j) == (n-1, m-1):
            return moves
        
        # Explore all possible moves
        for di, dj in directions:
            for x in range(1, k+1):
                ni, nj = i + di*x, j + dj*x
                
                # Check if the new position is within bounds and not an obstacle
                if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == 0:
                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        queue.append((ni, nj, moves + 1))
                else:
                    break  # Stop if we hit an obstacle or go out of bounds
    
    return -1

# Example usage
for k, maze, anser in [
    [2, [[0,0],[1,0]], 2],
    [5, [[0,0,0],[1,0,0]], 2],
    [5, [[0,1,0],[1,0,0]], -1],
]:
    print(f"{getMinimumMoves(maze, k)} == {anser}")