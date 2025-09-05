import gdown
import os

# Download the pose estimation model (FastPose ResNet50)
pose_model_path = 'pretrained_models/fast_res50_256x192.pth'
if not os.path.exists(pose_model_path):
    print("Downloading Pose Estimation Model...")
    gdown.download(id='1kQhnMRURFiy7NsdS8EFL-8vtqEXOgECn', output=pose_model_path, quiet=False)
else:
    print("Pose estimation model already exists.")

# Download the YOLOv3 person detector model
detector_model_path = 'detector/yolo/data/yolov3-spp.weights'
if not os.path.exists(detector_model_path):
    print("Downloading Person Detector Model...")
    gdown.download(id='1D47msNOOiJKvPOXlnpyzdKA3k6E97NTC', output=detector_model_path, quiet=False)
else:
    print("Person detector model already exists.")