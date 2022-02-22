#!/usr/bin/env python3
# -*- coding:utf-8-*-
# global variable management module
# 全局变量


def init():
    """初始化全局变量对象"""
    global GLOBALS_DICT
    GLOBALS_DICT = {}


def set_item(name, value):
    """设置变量"""
    try:
        GLOBALS_DICT[name] = value
        return True
    except KeyError:
        return False


def get_item(name):
    """获取变量的值"""
    try:
        return GLOBALS_DICT[name]
    except:
        return None


def has_item(name=None):
    """是否存在变量"""
    return name is not None and hasattr(GLOBALS_DICT, name)


def remove(name=None):
    """移除指定变量"""
    try:
        del GLOBALS_DICT[name]
        return True
    except:
        return False
