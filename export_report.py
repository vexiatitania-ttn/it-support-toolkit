import platform
import shutil
import datetime

# 1. Ambil waktu saat ini untuk nama file (Format: Tahun-Bulan-Tanggal_Jam-Menit-Detik)
waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nama_file = f"sys_report_{waktu_sekarang}.txt"

# 2. Kumpulkan data
os_info = f"OS: {platform.system()} {platform.release()} ({platform.machine()})"

total, used, free = shutil.disk_usage("C:\\")
gb = 2**30
disk_info = f"Sisa Disk: {free // gb} GB (Dari total {total // gb} GB)"

# 3. Buat dan tulis ke file TXT
with open(nama_file, 'w') as file:
    file.write("=== Laporan Diagnostik Sistem ===\n")
    file.write(f"Waktu Dibuat: {waktu_sekarang}\n")
    file.write("=================================\n\n")
    file.write(f"[1] Informasi Sistem\n{os_info}\n\n")
    file.write(f"[2] Status Penyimpanan (Drive C)\n{disk_info}\n")

print(f"[+] Laporan berhasil diekspor dan disimpan sebagai: {nama_file}")