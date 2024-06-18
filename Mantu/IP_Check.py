import psutil

def get_process_connections(process_name):
    connections = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.pid and psutil.Process(conn.pid).name() == process_name:
            connections.append(conn)
    return connections

process_name = input("Your_process_name: ")  # Replace with your process name
connections = get_process_connections(process_name)
for conn in connections:
    print(f"Local Address: {conn.laddr.ip} - Remote Address: {conn.raddr.ip}")