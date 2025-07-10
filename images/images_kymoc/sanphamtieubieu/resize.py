from PIL import Image
import os

def resize_and_rename_images(input_folder, output_folder=None, target_size=(1000, 664), name_prefix="Sofa"):
    """
    Resize và đổi tên tất cả ảnh trong folder thành kích thước target_size và format Sofa-1.jpg, Sofa-2.jpg...
    
    :param input_folder: Thư mục chứa ảnh gốc
    :param output_folder: Thư mục lưu ảnh đã resize (None = ghi đè)
    :param target_size: Kích thước mới (width, height)
    :param name_prefix: Prefix đặt tên mới cho file
    """
    # Nếu output_folder không có thì ghi đè
    if output_folder:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    else:
        output_folder = input_folder

    # Đọc tất cả file hợp lệ trong folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff'))]
    image_files.sort()  # Sắp xếp để rename theo thứ tự

    for idx, filename in enumerate(image_files, start=1):
        input_path = os.path.join(input_folder, filename)
        new_filename = f"{name_prefix}-{idx}.jpg"  # Tên file mới
        output_path = os.path.join(output_folder, new_filename)

        try:
            img = Image.open(input_path)
            img_resized = img.resize(target_size, Image.LANCZOS)
            img_resized.save(output_path, "JPEG", quality=95)
            print(f"✅ Đã resize & rename: {new_filename}")
        except Exception as e:
            print(f"❌ Lỗi với {filename}: {e}")

    print("🎉 Hoàn tất! Tất cả ảnh đã resize & đổi tên.")

# 📝 Sử dụng:
input_folder = "F:/lamlaikymoc/carbook-master/images/images_kymoc/sanphamtieubieu"          # <-- Folder ảnh gốc
output_folder = "F:/lamlaikymoc/carbook-master/images/images_kymoc/sanphamtieubieu/output"    # <-- Folder lưu ảnh mới (None = ghi đè)
resize_and_rename_images(input_folder, output_folder)
