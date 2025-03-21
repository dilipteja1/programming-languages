'''
    graph practice
'''
def add_edge_mat(mat, i, j):
    mat[i][j] = 1
    mat[j][i] = 1 #undirected    

def add_edge_list(adj_list, i, j):
    adj_list[i].append(j)
    adj_list[j].append(i)
    
def displayList(adj_list):
    for idx, row in enumerate(adj_list):
        print(idx, " ", row)

if __name__ == "__main__":
    V = 4
    mat = [[0] * V for _ in range(V)] # our graph
    
    add_edge_mat(mat, 0, 1)
    add_edge_mat(mat, 0, 2)
    add_edge_mat(mat, 1, 2)
    print(mat)
    
    adj_list = [[] for _ in range(V)]
    add_edge_list(adj_list, 0,1 )
    add_edge_list(adj_list, 0,2 )
    add_edge_list(adj_list, 1,2 )
    
    displayList(adj_list)