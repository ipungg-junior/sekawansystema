
from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.conf import settings
import os, json, psutil

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


def read_json(filename):
    # Buat path lengkap ke file JSON
    file_path = os.path.join(settings.BASE_DIR, f'{filename}')
    
    # Baca file JSON
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    else:
        print("Error when try unpacking configuration file.")
        return {}