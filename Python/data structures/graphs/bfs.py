'''
bfs
'''
def bfs(adj, src, visited, res):
    V  = len(adj)
    
    from collections import deque
    q = deque()
    visited[src] = True
    q.append(src)
    
    while q:
        currElement = q.popleft()
        res.append(currElement)
        
        neighbours = adj[currElement]
        for neighbour in neighbours:
            # this is to eliminate the cycles
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)

    return res

def bfs_init(adj):
    V  = len(adj)
    res = []
    visited = [False] * V
    # this will ensure all the disconnected components are also traversed
    for vertex in range(len(adj)):
        if not visited[vertex]:
            bfs(adj, vertex, visited, res)
    
    return res
    
if __name__ == '__main__':
    adj = [ [2, 3, 1], [0], [0, 4], [0], [2] ]
    
    src = 0
        
    ans = bfs_init(adj)
    
    print(ans)