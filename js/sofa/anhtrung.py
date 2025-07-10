import os
import hashlib
from PIL import Image
import imagehash

def get_file_hash(file_path):
    """Tính hash SHA256 để tìm ảnh giống 100%"""
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def find_exact_duplicates(folder_path):
    """Tìm ảnh giống nhau 100%"""
    hashes = {}
    duplicates = []

    for file_name in sorted(os.listdir(folder_path)):
        if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            file_path = os.path.join(folder_path, file_name)
            file_hash = get_file_hash(file_path)

            if file_hash in hashes:
                duplicates.append((file_name, hashes[file_hash]))
            else:
                hashes[file_hash] = file_name
    return duplicates

def find_similar_images(folder_path, threshold=5):
    """Tìm ảnh gần giống nhau (hash khác biệt <= threshold)"""
    hashes = {}
    similars = []

    for file_name in sorted(os.listdir(folder_path)):
        if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            file_path = os.path.join(folder_path, file_name)
            try:
                img_hash = imagehash.average_hash(Image.open(file_path))
                for existing_hash, existing_name in hashes.items():
                    if abs(img_hash - existing_hash) <= threshold:
                        similars.append((file_name, existing_name))
                hashes[img_hash] = file_name
            except Exception as e:
                print(f"Lỗi mở file {file_name}: {e}")
    return similars

def save_results_to_file(file_path, header, results, exact=True):
    """Ghi kết quả ra file txt"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + "\n")
        if results:
            for r in results:
                symbol = "===" if exact else "≈"
                f.write(f"{r[0]} {symbol} {r[1]}\n")
        else:
            f.write("✅ Không có kết quả\n")

# 📂 Đường dẫn folder ảnh
folder_path = r"F:\lamlaikymoc\carbook-master\js\sofa"

# 🔥 Tìm ảnh giống 100%
exact_dupes = find_exact_duplicates(folder_path)
print("\n🎯 Ảnh giống nhau 100%:")
if exact_dupes:
    for dup in exact_dupes:
        print(f" - {dup[0]} === {dup[1]}")
else:
    print("✅ Không có ảnh trùng 100%")

# 💾 Ghi ảnh trùng 100% ra file
save_results_to_file("duplicates.txt", "🎯 Ảnh giống nhau 100%:", exact_dupes, exact=True)

# 🔥 Tìm ảnh gần giống
similar_images = find_similar_images(folder_path, threshold=5)
print("\n🎯 Ảnh gần giống nhau (~90%):")
if similar_images:
    for sim in similar_images:
        print(f" - {sim[0]} ≈ {sim[1]}")
else:
    print("✅ Không có ảnh gần giống")

# 💾 Ghi ảnh gần giống ra file
save_results_to_file("similar_images.txt", "🎯 Ảnh gần giống nhau (~90%):", similar_images, exact=False)
