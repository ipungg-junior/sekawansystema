import os, psutil

def analyze_system_storage():

    # Menggunakan os.statvfs untuk mendapatkan informasi tentang sistem file
    statvfs = os.statvfs('/')
    # Menghitung total storage menggunakan formula
    total_storage = (statvfs.f_frsize * statvfs.f_blocks) / 1_000_000_000
    # Menggunakan psutil untuk mendapatkan informasi penggunaan storage
    used_storage = (psutil.disk_usage('/').used) / 1_000_000_000
    space = (total_storage - used_storage)
    percent = (used_storage / total_storage) * 100
    space = f'{space:.2f}'
    total_storage = f'{total_storage:.1f}'
    used_storage = f'{used_storage:.1f}'
    stats = {'decimal': used_storage, 'total': total_storage, 'space':space, 'percent':percent}
    return stats


