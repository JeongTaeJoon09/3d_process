import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"{path} 파일을 찾을 수 없습니다.")
    return image

def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def detect_edges(image):
    return cv2.Canny(image, 100, 200)

def generate_depth_map(image):
    gray = convert_to_gray(image)
    depth_map = cv2.GaussianBlur(gray, (21, 21), 0)  # 깊이 부드럽게
    depth_map = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX)
    return depth_map

def apply_3d_effect(image, depth_map):
    h, w = depth_map.shape
    depth_3d = np.zeros((h, w, 3), dtype=np.uint8)
    depth_3d[:, :, 0] = depth_map
    depth_3d[:, :, 1] = depth_map // 2
    depth_3d[:, :, 2] = 255 - depth_map
    return cv2.addWeighted(image, 0.6, depth_3d, 0.4, 0)

# 3D 포인트 클라우드 생성
def generate_point_cloud(image, depth_map, step=5):
    h, w = depth_map.shape
    points = []
    colors = []

    for y in range(0, h, step):
        for x in range(0, w, step):
            z = depth_map[y, x]
            points.append((x, y, z))
            colors.append(image[y, x] / 255.0)  # 색상 정규화

    return np.array(points), np.array(colors)

def visualize_point_cloud(points, colors):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    ax.scatter(points[:, 0], points[:, 1], points[:, 2],
               c=colors, s=1)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Depth")
    plt.title("3D Point Cloud")
    plt.show()

if __name__ == "__main__":
    print("▶ 이미지 처리 및 3D 변환 시작")

    img = load_image("sample_3d.jpg")
    depth = generate_depth_map(img)
    result = apply_3d_effect(img, depth)

    cv2.imwrite("depth_map.jpg", depth)
    cv2.imwrite("3d_result.jpg", result)

    # 포인트 클라우드 생성 및 시각화
    points, colors = generate_point_cloud(img, depth)
    visualize_point_cloud(points, colors)

    print("✅ 3D 변환 및 포인트 클라우드 생성 완료")
