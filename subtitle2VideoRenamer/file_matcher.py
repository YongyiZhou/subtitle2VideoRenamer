# -*- coding: utf-8 -*-

"""
@author: YongyiZhou
@file: file_matcher.py
@time: 2021/2/10
"""
import os
from subtitle2VideoRenamer.utils import name_util


def match_and_rename_subtitle(video_map, subtitles):
    """
    将字幕文件重命名为视频文件
    :param video_map: dict{S02E02:file}
    :param subtitles: list
    """
    print("matching subtitles...")
    key_set = video_map.keys()
    for subtitle in subtitles:
        subtitle_partition = subtitle.split('.')
        suffix = subtitle_partition[-1]  # 截取后缀
        key = name_util.key_for_episode_file(subtitle)
        if key not in key_set:
            print(f"\t\t--> subtitle [{subtitle}] with unknown origin video.")
            continue
        # 以视频的名字对字幕重命名
        language = ""
        if len(subtitle_partition) > 1:  # 截取语种
            if key not in subtitle_partition[-2]:  # 处理那些没有语种后缀的情况
                language = subtitle_partition[-2] + "."
        new_name = '.'.join(video_map[key].split('.')[:-1]) + '.' + language + suffix
        os.rename(subtitle, new_name)
        print(f"subtitle renamed: \t{subtitle}")
