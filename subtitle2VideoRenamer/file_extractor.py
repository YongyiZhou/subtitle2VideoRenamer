# -*- coding: utf-8 -*-

"""
@author: YongyiZhou
@file: file_extractor.py
@time: 2021/2/10
"""
import os
from subtitle2VideoRenamer.constant import config
from subtitle2VideoRenamer.utils import name_util


def get_videos_and_subtitles(path):
    """
    遍历当前目录及其所有子目录，获取视频文件和字幕文件
    :return: video_map, subtitles
    """
    files = []
    for root, _, file_list in os.walk(path):
        for file in file_list:
            files.append(os.path.join(root, file))
    return _file_classifier(files)


def _file_classifier(files):
    """
    将文件中的视频和字幕进行分组
    :param files: 所有文件
    :return: video_map(S02E02->file), subtitles
    """
    video_map = {}
    subtitles = []
    # 进行文件分类和剧集分集
    for file in files:
        suffix = file.split('.')[-1]  # 截取后缀
        # 获取视频文件
        if suffix in config.VIDEO_SUFFIX:
            print(f"video found: \t{file}")
            key = name_util.key_for_episode_file(file)
            if key in video_map.keys():  # 若在目录中发现重复的key则会停止运行
                print(f"find duplicate key of episode [{key}], please fix it.")
                exit(-1)
            video_map[key] = file
        # 获取字幕文件
        elif suffix in config.SUBTITLE_SUFFIX:
            subtitles.append(file)
        # 遇到了未定义的后缀则跳过
        else:
            print(f"\t\t--> file [{file}] with unknown suffix.")
            continue
    return video_map, subtitles
