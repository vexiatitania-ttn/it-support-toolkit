import platform

print("=== IT SUPPORT TOOLKIT ===")
print("Informasi Sistem\n")

print(f"Sistem operasi : {platform.system()}")
print(f"Rilis OS       : {platform.release()}")
print(f"Arsitektur     : {platform.machine()}")
print(f"Versi Python   : {platform.python_version()}")
