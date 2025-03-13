from queue import PriorityQueue

# Fungsi untuk algoritma A* Search
def a_star_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()  # Antrian prioritas untuk menyimpan simpul yang akan dieksplorasi
    frontier.put((0, start))  # Menambahkan simpul awal ke dalam antrian dengan nilai prioritas 0
    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi

    while not frontier.empty():
        current_priority, current_node = frontier.get()  # Mengambil simpul dengan nilai prioritas terendah

        if current_node == goal:
            print("Simpul tujuan sudah ditemukan!")
            return True  # Mengembalikan True jika simpul tujuan sudah ditemukan

        explored.add(current_node)  # Menandai simpul saat ini sebagai sudah dieksplorasi

        for neighbor in graph[current_node]:
            if neighbor not in explored:
                priority = heuristic[neighbor] + graph[current_node][neighbor]
                # Menambahkan nilai heuristik dan biaya langkah
                frontier.put((priority, neighbor))
                # Menambahkan simpul tetangga ke dalam antrian dengan nilai prioritas A*

    print("Simpul tujuan tidak ditemukan!")
    return False  # Mengembalikan False jika simpul tujuan tidak ditemukan


# Daftar heuristik untuk setiap simpul
heuristic = {
    'A': 9,
    'B': 4,
    'C': 5,
    'D': 5,
    'E': 3,
    'S': 7,
    'G': 0
}

# Graf (dalam bentuk daftar kejadian)
graph = {
    'S': {'A': 2, 'E': 2},
    'A': {'B': 7, 'C': 3},
    'B': {'G': 4},
    'C': {'G': 6},
    'D': {'G': 6},
    'E': {'D': 6}
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi A* Search
a_star_search(graph, start_node, goal_node, heuristic)
