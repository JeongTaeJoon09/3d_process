# test_3d_process.py
import cv2
import numpy as np
from _3d_process import load_image, convert_to_gray, detect_edges, generate_depth_map, apply_3d_effect

IMAGE_PATH = "sample_3d.jpg"

def test_load_image():
    img = load_image(IMAGE_PATH)
    assert img is not None
    assert isinstance(img, np.ndarray)
    assert img.shape[2] == 3

def test_convert_to_gray():
    img = load_image(IMAGE_PATH)
    gray = convert_to_gray(img)
    assert len(gray.shape) == 2

def test_detect_edges():
    img = load_image(IMAGE_PATH)
    gray = convert_to_gray(img)
    edges = detect_edges(gray)
    assert len(edges.shape) == 2
    assert np.any(edges > 0)

def test_generate_depth_map():
    img = load_image(IMAGE_PATH)
    depth = generate_depth_map(img)
    assert depth.shape == convert_to_gray(img).shape
    assert depth.dtype == np.uint8
    assert np.max(depth) <= 255 and np.min(depth) >= 0

def test_apply_3d_effect():
    img = load_image(IMAGE_PATH)
    depth = generate_depth_map(img)
    result = apply_3d_effect(img, depth)
    assert result.shape == img.shape
    assert result.dtype == np.uint8
    assert np.any(result != img)
