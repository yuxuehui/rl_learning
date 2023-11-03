import os
import sys

import imageio
import numpy as np

import os

class VideoRecorder(object):
    def __init__(self, root_dir, height=256, width=256, fps=10):
        self.save_dir = root_dir
        self.height = height
        self.width = width
        self.fps = fps
        self.frames = []
        self.enabled = True
        self.make_path(root_dir)

    def record(self, env):
        if self.enabled:
            frame = env.render(mode='rgb_array')
            self.frames.append(frame)

    def save(self, file_name):
        if self.enabled:
            path = os.path.join(self.save_dir, file_name)
            imageio.mimsave(path, self.frames, fps=self.fps)
    
    def disable(self):
        self.enabled = False
    
    def reset(self):
        self.frames.clear()

    def make_path(self, root_dir):
        paths = root_dir.split('/')
        for i in range(len(paths)):
            cur_path = '/'.join(paths[:i+1])
            if not os.path.exists(cur_path):
                os.mkdir(cur_path)
