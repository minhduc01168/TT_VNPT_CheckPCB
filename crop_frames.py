import cv2
import os

def extract_frames(video_path, output_dir):
    # Kiểm tra xem thư mục đầu ra có tồn tại chưa, nếu chưa thì tạo mới
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Mở video
    video = cv2.VideoCapture(video_path)
    frame_count = 0
    saved_frame_count = 0

    while True:
        # Đọc từng frame
        ret, frame = video.read()

        if not ret:
            break

        # Kiểm tra xem frame hiện tại có đủ điều kiện để cắt và lưu không
        if frame_count % 10 == 0:
            # Đặt tên cho frame theo thứ tự
            frame_name = f"image_1_{saved_frame_count}.jpg"
            output_path = os.path.join(output_dir, frame_name)

            # Lưu frame vào thư mục đầu ra
            cv2.imwrite(output_path, frame)

            saved_frame_count += 1

        frame_count += 1

    # Đóng video
    video.release()

    print(f"Đã cắt và lưu {saved_frame_count} frame từ video.")

# Đường dẫn đến video
video_path = "D:/Learn school/Thuctap_VNPT/mach_sai_4_test.mp4"

# Thư mục đầu ra
output_dir = "D:/Learn school/Thuctap_VNPT/images_data"

# Gọi hàm để cắt frame từ video và lưu vào thư mục
extract_frames(video_path, output_dir)
