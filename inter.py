import heapq
import itertools  # Perbaiki baris ini untuk mengimpor modul itertools
import time
import sys
import os
import subprocess

def ucs(graph, start, goal):
    priority_queue = [(0, start, [])]  # Format: (cost, current_node, path_so_far)
    visited = set()

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node not in visited:
            path = path + [current_node]
            if current_node == goal:
                return path

            visited.add(current_node)
            for neighbor, neighbor_cost in graph[current_node]:
                heapq.heappush(priority_queue, (cost + neighbor_cost, neighbor, path))

    return "Tidak ada jalur yang ditemukan"

# Graf untuk studi kasus Kantin Kampus
kampus_graph = {
    'Gerbang': [('Perpustakaan', 3), ('Aula', 5)],
    'Perpustakaan': [('Gerbang', 3), ('Aula', 2), ('Lab Komputer', 4)],
    'Aula': [('Gerbang', 5), ('Perpustakaan', 2), ('Lab Komputer', 1), ('Kantin', 6)],
    'Lab Komputer': [('Perpustakaan', 4), ('Aula', 1), ('Kantin', 3)],
    'Kantin': [('Aula', 6), ('Lab Komputer', 3)]
}

def print_welcome_animation():
    print("Selamat datang di program UCS")
    time.sleep(0.5)
    sys.stdout.write("\b")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write("\b\b")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write("\b\b\b")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write("\b\b\b\b")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write("\b\b\b\b\b")
    sys.stdout.flush()

def print_loading_animation(duration):
    chars = itertools.cycle(['|', '/', '-', '\\'])
    start_time = time.time()
    while time.time() - start_time < duration:
        sys.stdout.write("\r")
        sys.stdout.write("Proses... " + next(chars))
        sys.stdout.flush()
        time.sleep(0.1)

def print_confirm_loading_animation(duration):
    for i in range(101):
        sys.stdout.write(f"\rMencari... {i}%")
        sys.stdout.flush()
        time.sleep(duration / 100)

def print_stretch_loading_animation(duration):
    for i in range(101):
        sys.stdout.write("\r")
        sys.stdout.write("Proses... [{}{}]".format("=" * i, " " * (100 - i)))
        sys.stdout.flush()
        time.sleep(duration / 100)

if __name__ == "__main__":
    print_welcome_animation()
    print_loading_animation(5) 
    print_stretch_loading_animation(5)
    print("\n")
    print("Loaded selesai!")

    start_state = input("Masukkan lokasi awal (Gerbang/Perpustakaan/Aula/Lab Komputer/Kantin): ")
    goal_state = input("Masukkan tujuan (Gerbang/Perpustakaan/Aula/Lab Komputer/Kantin): ")

    if start_state not in kampus_graph or goal_state not in kampus_graph:
        print("Lokasi awal atau tujuan tidak valid.")
        sys.exit(1)

    result_ucs = ucs(kampus_graph, start_state, goal_state)
    print("\n")
    print_confirm_loading_animation(5)
    print("\n")
    print("Jalur terpendek dari", start_state, "ke", goal_state, "menggunakan UCS adalah:", result_ucs)

    buka_gambar = input("Mau membuka peta kampus? (ya/tidak): ").lower()
    if buka_gambar == 'ya':
        print_stretch_loading_animation(3)
        try:
            subprocess.Popen(['open', 'kampus_map.png'])
        except:
            try:
                subprocess.Popen(['xdg-open', 'kampus_map.png'])
            except:
                os.startfile('kampus_map.png')
