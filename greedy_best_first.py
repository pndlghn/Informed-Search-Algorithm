from queue import PriorityQueue

# Fungsi untuk algoritma Greedy Best-First Search
def greedy_best_first_search(graph, start, goal):
    frontier = PriorityQueue()  
    frontier.put((heuristic[start], start))
    explored = set() 
    visited_order = []  

    while not frontier.empty():
        _, current_node = frontier.get() 
        visited_order.append(current_node)
        print("Mengunjungi simpul:", current_node)

        if current_node == goal:
            print("\nSimpul tujuan ditemukan!")
            print("Urutan kunjungan simpul:", " → ".join(visited_order))
            return True  # Berhenti jika simpul tujuan ditemukan

        explored.add(current_node)  # Tandai sebagai sudah dieksplorasi

        for neighbor in graph[current_node]:
            if neighbor not in explored:
                priority = heuristic[neighbor]  # Nilai heuristik sebagai prioritas
                frontier.put((priority, neighbor))  # Tambahkan ke antrian

    print("\nSimpul tujuan tidak ditemukan!")
    print("Urutan kunjungan simpul:", " → ".join(visited_order))
    return False  # Jika simpul tujuan tidak ditemukan

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

# Graf berbentuk adjacency list
graph = {
    'S': {'A', 'E'},
    'A': {'B', 'C'},
    'B': {'D'},
    'C': {'G'},
    'D': {'G'},
    'E': {'D'}
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi Greedy Best-First Search
greedy_best_first_search(graph, start_node, goal_node)