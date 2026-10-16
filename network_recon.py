import socket

def get_ip(domain):
    try:
        # Melakukan DNS Lookup (menerjemahkan nama domain ke IP)
        ip_address = socket.gethostbyname(domain)
        print(f"[+] Target terdeteksi  : {domain}")
        print(f"[+] Alamat IP (IPv4) : {ip_address}")
    except socket.gaierror:
        print(f"[-] Gagal: Domain '{domain}' tidak ditemukan atau tidak valid.")

print("=== Basic DNS Reconnaissance ===")
# Meminta input langsung dari pengguna di terminal
target_domain = input("Masukkan target domain (contoh: target.com): ")
get_ip(target_domain)
print("================================")