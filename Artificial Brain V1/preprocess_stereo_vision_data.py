import cv2
import numpy as np
import skimage.feature

def preprocess_stereo_vision_data(data):
    # Perform stereo rectification and undistortion
    rectified_left = cv2.remap(data['left'], data['left_map_x'], data['left_map_y'], cv2.INTER_LINEAR)
    rectified_right = cv2.remap(data['right'], data['right_map_x'], data['right_map_y'], cv2.INTER_LINEAR)
    
    # Calculate color histogram features for both left and right images
    hsv_left = cv2.cvtColor(rectified_left, cv2.COLOR_BGR2HSV)
    hsv_right = cv2.cvtColor(rectified_right, cv2.COLOR_BGR2HSV)
    hist_left = cv2.calcHist([hsv_left], [0, 1, 2], None, [8, 8, 8], [0, 180, 0, 256, 0, 256])
    hist_right = cv2.calcHist([hsv_right], [0, 1, 2], None, [8, 8, 8], [0, 180, 0, 256, 0, 256])
    hist_left = cv2.normalize(hist_left, hist_left).flatten()
    hist_right = cv2.normalize(hist_right, hist_right).flatten()
    
    # Perform feature detection and matching
    sift = cv2.SIFT_create()
    kp_left, des_left = sift.detectAndCompute(rectified_left, None)
    kp_right, des_right = sift.detectAndCompute(rectified_right, None)
    bf = cv2.BFMatcher()
    matches = bf.match(des_left, des_right)
    
    # Perform stereo matching and depth estimation
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity_map = stereo.compute(rectified_left, rectified_right)
    depth_map = (data['focal_length'] * data['baseline']) / disparity_map
    
    # Perform point cloud generation and filtering
    point_cloud = cv2.reprojectImageTo3D(disparity_map, data['Q'])
    point_cloud = point_cloud[point_cloud[:, :, 2] > data['min_depth']]
    point_cloud = point_cloud[point_cloud[:, :, 2] < data['max_depth']]
    
    # Calculate additional features
    mean_depth = np.mean(depth_map)
    std_depth = np.std(depth_map)
    max_depth = np.max(depth_map)
    min_depth = np.min(depth_map)
    
    # Return preprocessed data
    return {'hist_left': hist_left, 'hist_right': hist_right, 'kp_left': kp_left, 'kp_right': kp_right, 'matches': matches, 'depth_map': depth_map, 'point_cloud': point_cloud, 'mean_depth': mean_depth, 'std_depth': std_depth, 'max_depth': max_depth, 'min_depth': min_depth}
