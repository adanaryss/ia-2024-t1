import heapq

def dijkstra(graph, start, goal):
    dist = {node['id']: float('inf') for node in graph}
    prev = {node['id']: None for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if cur_node == goal:
            break
        if cur_dist > dist[cur_node]:
            continue
        for next_node_id, edge_weight in graph[cur_node]['edges']:
            alt = cur_dist + edge_weight
            if alt < dist[next_node_id]:
                dist[next_node_id] = alt
                prev[next_node_id] = cur_node
                heapq.heappush(pq, (alt, next_node_id))

    path = []
    cur_node = goal
    while cur_node is not None:
        path.append(cur_node)
        cur_node = prev[cur_node]
    path.reverse()

    return len(dist), dist[goal], path

def get_length_path(graph, path):
    length_path = 0
    for index in range(len(path) - 1):
        latitude1, longitude1 = get_lat_long(graph, path[index])
        latitude2, longitude2 = get_lat_long(graph, path[index + 1])
        length_path += haversine(latitude1, longitude1, latitude2, longitude2)
    return length_path

def get_lat_long(graph, vertex_id):
    for node in graph:
        if node['id'] == vertex_id:
            return node['latitude'], node['longitude']
    return None, None
