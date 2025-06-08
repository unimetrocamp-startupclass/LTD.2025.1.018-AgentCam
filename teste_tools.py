from custom_tools import VideoTool

det = VideoTool(max_frames=50)
print(det.run(camera_url='http://72.43.190.171:81/mjpg/video.mjpg?size=1'))