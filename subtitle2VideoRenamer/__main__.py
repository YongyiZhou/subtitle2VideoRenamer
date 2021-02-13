# -*- coding: utf-8 -*-

"""
@author: YongyiZhou
@file: __main__.py
@time: 2021/2/10
"""
import os
import sys
from subtitle2VideoRenamer import file_extractor
from subtitle2VideoRenamer import file_matcher


def main():
    path = ""
    # path先尝试取传的参数
    if len(sys.argv) > 1:
        path = sys.argv[1]
        os.chdir(path)
    else:
        path = input("请输入视频文件所在的目录，若为空则默认当前目录：").strip()
    # 若不传递参数给脚本，则默认要处理的文件在命令行当前所在目录
    path = path if bool(path) else os.getcwd()
    print(f"Work path is: {path}")
    # 拉取文件
    video_map, subtitles = file_extractor.get_videos_and_subtitles(path)
    file_matcher.match_and_rename_subtitle(video_map, subtitles)


if __name__ == '__main__':
    main()
