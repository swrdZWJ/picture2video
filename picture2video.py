#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:28:26 2019

@author: zhu
"""

"""
how to use:
    python picture2video.py uav0000023_00870_s/*.jpg -v -r 25 -o uav0000023_00870_s
"""


import argparse
import glob
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='+', help='Input file(s)')
    parser.add_argument('--outdir', '-o', action='store', help='Output directory path. Default: same directory.')
    parser.add_argument('--video', '-v', action='store_true', help='Compile as video using ffmpeg.')
    parser.add_argument('--framerate', '-r', type=int, help='Frames per second of the video.')


    args = parser.parse_args()

    if type(args.input) == list: 
        files = args.input
    else:
        files = glob.glob(args.inglob.split('\n')[0])
    print(files)
    print("> Rendering images [.png] from the flows [.flo]")

    

    if args.video:
        print("> Compiling [.mp4] video from the flow images [.png]")
        if args.framerate == None:
            args.framerate = 24
        if args.outdir == None:
            out = files[0] + '.mp4'
            files = os.path.join(os.path.dirname(files[0]), '*.jpg')
        else:
            out = os.path.join(args.outdir, os.path.basename(files[0]) + '.mp4')
#            print(out)
            files = os.path.join(args.outdir, '*.jpg')
        print(files)    

        print("> Saving video as: " + out)

        os.system("ffmpeg -r {} -loglevel panic -pattern_type glob -i '{}' {} ".format(
            args.framerate,
            files,
            out
        ))