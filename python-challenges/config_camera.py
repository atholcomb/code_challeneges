#!/usr/bin/python3
# written by: atholcomb
# config_camera.py
# Prompts user for a frame rate value and 
# configues each camera with given value

import json

def config_camera():
  camera_defaults = {"camera 1": 0, "camera 2": 1, "camera 3": 2}
  frame_rates = []

  for i in range(3):
    camera_frames = int(input("Enter video frame rate: "))
    frame_rates.append(camera_frames) 

  for k, v in camera_defaults.items():
    camera_defaults[k] = frame_rates[v]

  return json.dumps(camera_defaults, indent=3)

print(config_camera())
