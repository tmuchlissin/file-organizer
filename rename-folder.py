import os

# Dapatkan daftar nama file dalam folder
folder_path = input('Enter path : ')
file_names = os.listdir(folder_path)

# Buat counter untuk penomoran
counter = 1

# Ubah nama file
for file_name in file_names:
    # Dapatkan nama file dan ekstensi
    file_title, file_extension = os.path.splitext(file_name)

    # Buat nama file baru
    new_file_name = f"doc_{counter:03d}{file_extension}"

    # Ganti nama file
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

    # Tambah counter
    counter += 1

print("Nama file video telah diubah!")