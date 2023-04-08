import cv2
import numpy as np
import skimage.feature

def preprocess_stereo_thermal_data(data):
    # Perform stereo rectification and undistortion
    rectified_left = cv2.remap(data['left'], data['left_map_x'], data['left_map_y'], cv2.INTER_LINEAR)
    rectified_right = cv2.remap(data['right'], data['right_map_x'], data['right_map_y'], cv2.INTER_LINEAR)
    # Perform object detection and segmentation
    left_gray = cv2.cvtColor(rectified_left, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(rectified_right, cv2.COLOR_BGR2GRAY)
    detector = cv2.SimpleBlobDetector_create()
    keypoints_left = detector.detect(left_gray)
    keypoints_right = detector.detect(right_gray)
    mask_left = np.zeros_like(left_gray)
    mask_right = np.zeros_like(right_gray)
    for kp in keypoints_left:
        cv2.circle(mask_left, (int(kp.pt[0]), int(kp.pt[1])), int(kp.size / 2), (255, 255, 255), -1)
    for kp in keypoints_right:
        cv2.circle(mask_right, (int(kp.pt[0]), int(kp.pt[1])), int(kp.size / 2), (255, 255, 255), -1)
    segmented_left = cv2.bitwise_and(rectified_left, rectified_left, mask=mask_left)
    segmented_right = cv2.bitwise_and(rectified_right, rectified_right, mask=mask_right)
    # Calculate temperature difference between the two images
    temp_left = cv2.convertScaleAbs(segmented_left, alpha=(255.0 / data['max_temp']), beta=0)
    temp_right = cv2.convertScaleAbs(segmented_right, alpha=(255.0 / data['max_temp']), beta=0)
    temp_diff = cv2.absdiff(temp_left, temp_right)
    # Extract texture features from temperature difference image
    filtered = cv2.medianBlur(temp_diff, 5)
    glcm = skimage.feature.greycomatrix(filtered, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], symmetric=True, normed=True)
    contrast = skimage.feature.greycoprops(glcm, 'contrast').mean()
    energy = skimage.feature.greycoprops(glcm, 'energy').mean()
    homogeneity = skimage.feature.greycoprops(glcm, 'homogeneity').mean()
    correlation = skimage.feature.greycoprops(glcm, 'correlation').mean()
    # Return preprocessed data
    return {'keypoints_left': keypoints_left, 'keypoints_right': keypoints_right, 'temp_diff': temp_diff, 'contrast': contrast, 'energy': energy, 'homogeneity': homogeneity, 'correlation': correlation}
