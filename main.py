import os

def show_menu():
    print("\n=== 🛠️ IT Support & Recon Toolkit ===")
    print("1. Cek Informasi Sistem Dasar")
    print("2. Cek Kapasitas & Sisa Disk")
    print("3. DNS Reconnaissance (Cari IP Target)")
    print("4. Ekspor Laporan Sistem ke TXT")
    print("0. Keluar")
    print("======================================")

while True:
    show_menu()
    # Validasi input dengan .strip() agar spasi tidak membuat program error
    pilihan = input("Pilih menu (0-4): ").strip()

    if pilihan == '1':
        os.system('python system_info.py')
    elif pilihan == '2':
        os.system('python disk_info.py')
    elif pilihan == '3':
        os.system('python network_recon.py')
    elif pilihan == '4':
        os.system('python export_report.py')
    elif pilihan == '0':
        print("[+] Keluar dari toolkit. Terima kasih!")
        break
    else:
        print("[-] Pilihan tidak valid. Silakan ketik angka 0, 1, 2, 3, atau 4.")