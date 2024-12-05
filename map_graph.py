from settings import *

graph = {'wolf' : ['slime'],
         'slime' : ['demon'],
         'demon' : ['wolf', 'slime']}

def get_edges(vertex):
    edges = []
    for adj_vertex in graph[vertex]:
        edges.append((vertex, adj_vertex))
    return edges

edge_coordinates = {('wolf', 'slime') : (((SCREEN_WIDTH//2), 150), (SCREEN_WIDTH//3, 350)),
                    ('wolf', 'demon') : (((SCREEN_WIDTH//2), 150), ((SCREEN_WIDTH//3)*2, 350)),
                    ('slime', 'wolf') : (((SCREEN_WIDTH//2), 150), (SCREEN_WIDTH//3, 350)),
                    ('slime','demon') : ((SCREEN_WIDTH//3, 350), ((SCREEN_WIDTH//3)*2, 350)),
                    ('demon', 'wolf') : (((SCREEN_WIDTH//2), 150), ((SCREEN_WIDTH//3)*2, 350)),
                    ('demon','slime') : ((SCREEN_WIDTH//3, 350), ((SCREEN_WIDTH//3)*2, 350))}

def draw_edge(screen, edge):
    info = edge_coordinates[edge]
    start = info[0]
    end = info[1]
    pygame.draw.line(screen, (255, 0, 0), start, end)
    
    

if __name__ == "__main__":
    
    print(get_edges('wolf'))

