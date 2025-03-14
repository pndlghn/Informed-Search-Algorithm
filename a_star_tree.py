from queue import PriorityQueue

# Fungsi untuk algoritma A* Tree Search
def a_star_tree_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()  # Antrian prioritas berdasarkan f(n) = g(n) + h(n)
    frontier.put((0, start, []))  # (total_cost, node, path)
    
    while not frontier.empty():
        current_cost, current_node, path = frontier.get()  # Ambil simpul dengan prioritas terendah
        
        path = path + [current_node]  # Tambahkan simpul ke jalur
        
        if current_node == goal:
            print("\nSimpul tujuan ditemukan!")
            print("Jalur yang ditemukan:", " → ".join(path))
            print("Total biaya jalur:", current_cost)
            return path, current_cost
        
        for neighbor, cost in graph[current_node].items():
            total_cost = current_cost + cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
            frontier.put((total_cost, neighbor, path))  # Masukkan simpul ke frontier
    
    print("\nSimpul tujuan tidak ditemukan!")
    return None, float("inf")  # Jika simpul tujuan tidak ditemukan

# Daftar heuristik untuk setiap simpul
heuristic = {
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'S': 7,
    'G': 0  # Simpul tujuan memiliki nilai heuristik 0
}

# Graf berbobot dalam bentuk adjacency list
graph = {
    'S': {'A': 3, 'E': 2},
    'A': {'B': 3, 'C': 4},
    'B': {'D': 5},
    'C': {'G': 7},
    'D': {'G': 3},
    'E': {'D': 6}
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi A* Tree Search
a_star_tree_search(graph, start_node, goal_node, heuristic)
