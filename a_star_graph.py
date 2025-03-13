from queue import PriorityQueue

# Fungsi untuk algoritma A* Graph Search
def a_star_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()  # Antrian prioritas untuk menyimpan simpul yang akan dieksplorasi
    frontier.put((0, start))  # Menambahkan simpul awal ke dalam antrian dengan nilai prioritas 0
    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi

    while not frontier.empty():
        _, current_node = frontier.get()  # Mengambil simpul dengan nilai prioritas terendah dari antrian

        if current_node == goal:
            print("Simpul tujuan sudah ditemukan!")
            return True  # Mengembalikan True jika simpul tujuan sudah ditemukan

        explored.add(current_node)  # Menandai simpul saat ini sebagai sudah dieksplorasi

        for neighbor in graph[current_node]:
            cost = graph[current_node][neighbor]  # Biaya langkah dari simpul saat ini ke tetangga
            heuristic_cost = heuristic[neighbor]  # Nilai heuristik dari tetangga
            total_cost = cost + heuristic_cost  # Total biaya yang diperlukan untuk mencapai tetangga

            if neighbor not in explored:
                frontier.put((total_cost, neighbor))  # Menambahkan simpul tetangga ke dalam antrian dengan nilai prioritas total_cost

    print("Simpul tujuan tidak ditemukan!")
    return False  # Mengembalikan False jika simpul tujuan tidak ditemukan

# Daftar heuristik untuk setiap simpul
heuristic = {
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'S': 7,
    'G': 0
}

# Graf (dalam bentuk daftar kejadian)
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

# Panggil fungsi A* Search
a_star_search(graph, start_node, goal_node, heuristic)
