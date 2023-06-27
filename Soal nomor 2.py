import time

# Fungsi untuk menghitung jalur terpendek menggunakan algoritma TSP
def tsp(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    path = []
    min_distance = float('inf')

    # Rekursi untuk mencari jalur terpendek
    def tsp_util(curr_vertex, count, curr_path, curr_distance):
        nonlocal min_distance

        if count == num_nodes:
            if graph[curr_vertex][start] != 0:
                curr_distance += graph[curr_vertex][start]
                if curr_distance < min_distance:
                    min_distance = curr_distance
                    path.extend(curr_path)
                    path.append(start)
            return

        for v in range(num_nodes):
            if not visited[v] and graph[curr_vertex][v] != 0:
                visited[v] = True
                curr_path.append(v)

                tsp_util(v, count + 1, curr_path, curr_distance + graph[curr_vertex][v])

                visited[v] = False
                curr_path.pop()

    # Menginisialisasi rekursi
    visited[start] = True
    path.append(start)
    tsp_util(start, 1, [], 0)

    return min_distance, path


# Fungsi untuk menghitung jalur terpendek menggunakan algoritma Dijkstra
def dijkstra(graph, start):
    num_nodes = len(graph)
    distance = [float('inf')] * num_nodes
    distance[start] = 0
    shortest_path = [False] * num_nodes

    for _ in range(num_nodes):
        min_dist = float('inf')
        for v in range(num_nodes):
            if not shortest_path[v] and distance[v] < min_dist:
                min_dist = distance[v]
                u = v

        shortest_path[u] = True

        for v in range(num_nodes):
            if not shortest_path[v] and graph[u][v] != 0 and distance[u] + graph[u][v] < distance[v]:
                distance[v] = distance[u] + graph[u][v]

    return distance


# Fungsi untuk menghitung waktu eksekusi
def calculate_execution_time(start_time):
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


# Fungsi untuk menampilkan graf
def print_graph(graph):
    for row in graph:
        print(row)


# Fungsi untuk menampilkan jalur terpendek
def print_shortest_path(shortest_path):
    if shortest_path[0] == float('inf'):
        print("Tidak ada jalur yang tersedia.")
    else:
        print("Jalur terpendek:", shortest_path)


# Fungsi untuk menjalankan program
def run_program():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    print("Graf:")
    print_graph(graph)

    algorithm = input("Pilih algoritma (TSP atau Dijkstra): ")

    if algorithm.lower() == 'tsp':
        start_node = int(input("Masukkan node awal: "))
        start_time = time.time()
        min_distance, path = tsp(graph, start_node)
        execution_time = calculate_execution_time(start_time)

        print("\nHasil iterasi:")
        print("Jarak terpendek:", min_distance)
        print("Path:", path)
        print("Waktu komputasi:", execution_time)
        print("Hasil akhir:")
        print_shortest_path(path)

    elif algorithm.lower() == 'dijkstra':
        start_node = int(input("Masukkan node awal: "))
        start_time = time.time()
        shortest_distance = dijkstra(graph, start_node)
        execution_time = calculate_execution_time(start_time)

        print("\nHasil iterasi:")
        print("Jarak terpendek:", shortest_distance)
        print("Waktu komputasi:", execution_time)

    else:
        print("Algoritma yang dipilih tidak valid.")


# Menjalankan program
run_program()