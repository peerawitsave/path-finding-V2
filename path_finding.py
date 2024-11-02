import pygame
import sys
import heapq
from collections import deque

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graph Traversal Visualization")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Dictionary
graph = {
    'A': [('B', 1), ('C', 1)],
    'B': [('D', 1), ('E', 1)],
    'C': [('F', 1)],
    'D': [('H', 1)],
    'E': [('F', 1)],
    'F': [('G', 1)],
    'G': [],
    'H': []
}

node_positions = {
    'A': (100, 100),
    'B': (200, 200),
    'C': (200, 50),
    'D': (300, 250),
    'E': (300, 150),
    'F': (400, 100),
    'G': (500, 300),
    'H': (600, 160)
}

def draw_graph(path=[]):
    window.fill(WHITE)
    for node in graph:
        for neighbor, _ in graph[node]:
            pygame.draw.line(window, BLACK, node_positions[node], node_positions[neighbor], 2)
    for node, position in node_positions.items():
        color = RED if node in path else BLUE
        pygame.draw.circle(window, color, position, 20)
        font = pygame.font.Font(None, 24)
        text = font.render(node, True, BLACK)
        window.blit(text, (position[0] - 10, position[1] - 10))
    pygame.display.update()

# DFS
def depth_first_search(graph, start):
    stack = [start]
    visited = set()
    path = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            path.append(current)
            draw_graph(path)  # Visualize step
            pygame.time.delay(500)
            for neighbor, _ in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return path

# BFS
def breadth_first_search(graph, start):
    queue = deque([start])
    visited = set()
    path = []
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            path.append(current)
            draw_graph(path)  # Visualize step
            pygame.time.delay(500)
            for neighbor, _ in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return path

# Dijkstra
def dijkstra(graph, start):
    priority_queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    path = []
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node not in path:
            path.append(current_node)
            draw_graph(path)
            pygame.time.delay(500)
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

def main():
    running = True
    while running:
        draw_graph()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    depth_first_search(graph, 'A')
                if event.key == pygame.K_2:
                    breadth_first_search(graph, 'A')
                if event.key == pygame.K_3:
                    dijkstra(graph, 'A')
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
