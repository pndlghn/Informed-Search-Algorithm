from queue import PriorityQueue

# Fungsi untuk algoritma Greedy Search
def greedy_search(graph, start, goal):
    frontier = PriorityQueue()  # Antrian prioritas untuk menyimpan simpul yang akan dieksplorasi
    frontier.put((0, start))  # Menambahkan simpul awal ke dalam antrian dengan nilai prioritas 0
    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi

    while not frontier.empty():
        _, current_node = frontier.get()  # Mengambil simpul dengan nilai prioritas terendah dari antrian

        if current_node == goal:
            print("Simpul tujuan sudah ditemukan!")
            return True  # Mengembalikan True jika simpul tujuan sudah ditemukan

        explored.add(current_node)  # Menandai simpul saat ini sebagai sudah dieksplorasi

        for neighbor in graph.get(current_node, []):
            if neighbor not in explored:
                priority = heuristic[neighbor]  # Menggunakan nilai heuristik untuk menentukan prioritas
                frontier.put((priority, neighbor))  # Menambahkan simpul tetangga ke dalam antrian dengan nilai prioritas heuristik

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
    'S': {'A', 'E'},
    'A': {'B', 'C'},
    'B': {'G'},
    'C': {'G'},
    'E': {'D'},
    'D': {'G'}
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi greedy search
greedy_search(graph, start_node, goal_node)
