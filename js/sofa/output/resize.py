from PIL import Image
import os

def resize_and_rename_images(target_size=(1000, 664), name_prefix="SanPham"):
    """
    Resize và đổi tên tất cả ảnh trong thư mục chứa file .py hiện tại.
    Tất cả ảnh được lưu vào thư mục con 'output' ngay tại đó.
    Format tên file: Sofa-1.jpg, Sofa-2.jpg, ...
    """
    # Lấy đường dẫn thư mục chứa file .py
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = script_dir
    output_folder = os.path.join(script_dir, "output")

    # Tạo folder output nếu chưa có
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lọc danh sách file ảnh hợp lệ
    image_files = [f for f in os.listdir(input_folder)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff'))]
    image_files.sort()  # Đảm bảo thứ tự đặt tên

    if not image_files:
        print("⚠️ Không tìm thấy ảnh hợp lệ trong thư mục!")
        return

    # Resize và rename
    for idx, filename in enumerate(image_files, start=1):
        input_path = os.path.join(input_folder, filename)
        new_filename = f"{name_prefix}-{idx}.jpg"
        output_path = os.path.join(output_folder, new_filename)

        try:
            img = Image.open(input_path)
            img_resized = img.resize(target_size, Image.LANCZOS)
            img_resized.save(output_path, "JPEG", quality=95)
            print(f"✅ Đã resize & rename: {new_filename}")
        except Exception as e:
            print(f"❌ Lỗi với {filename}: {e}")

    print(f"🎉 Hoàn tất! Ảnh đã lưu vào: {output_folder}")

# 📝 Sử dụng:
if __name__ == "__main__":
    resize_and_rename_images()
