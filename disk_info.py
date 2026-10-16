import shutil

# Get disk usage statistics for the Windows C: drive
total, used, free = shutil.disk_usage("C:\\")

# Convert bytes to Gigabytes (1 GB = 2^30 bytes)
gb = 2**30

print("=== Storage Diagnostics ===")
print(f"Total Space: {total // gb} GB")
print(f"Used Space : {used // gb} GB")
print(f"Free Space : {free // gb} GB")
print("===========================")