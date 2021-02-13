# -*- coding: utf-8 -*-

"""
@author: YongyiZhou
@file: name_util.py
@time: 2021/2/10
"""
import re


def key_for_episode_file(file):
    """
    获取唯一标识某一集的key，一般为S02E01这种格式
    :param file: 视频或字幕文件
    :return: key
    """
    left, right = re.search(r"S\d{1,2}E\d{1,2}", file).span()
    return file[left:right]