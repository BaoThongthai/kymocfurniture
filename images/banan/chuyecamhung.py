import os

# Đường dẫn thư mục chứa video
folder_path = r"F:\lamlaikymoc\carbook-master\images\banan"  # ← Thay bằng đường dẫn thực tế

# Lọc các file .mp4 và sắp xếp theo thứ tự
mp4_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.jpg')])

# Đổi tên từng file
for idx, filename in enumerate(mp4_files, start=1):
    old_path = os.path.join(folder_path, filename)
    new_filename = f"SanPham-{idx}.jpg"
    new_path = os.path.join(folder_path, new_filename)

    os.rename(old_path, new_path)
    print(f"✅ Đã đổi: {filename} → {new_filename}")
