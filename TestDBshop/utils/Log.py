# -*-coding:utf-8-*-
import logging
from common.common_path import *
import os

# 因为控制台的级别设置为WARNING，所有WARNING以下的级别并没有输出。


class Log():
    def __init__(self, type, **kwargs):
        self.type = type
        self.msg = kwargs
        '''添加一个日志器'''
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.stream_control()

    def fomt(self):
        '''设置格式器'''
        self.for1 = logging.Formatter(fmt='[%(name)s]  [%(levelname)s]  [%(asctime)s] ------->>>>[%(message)s ]')
        self.for2 = logging.Formatter(
            fmt='[%(name)s]  [%(levelname)s]  [%(asctime)s] [%(filename)s]------->>>>[%(message)s ]')
        return self.for1, self.for2

    def hand(self):
        '''添加一个处理器'''
        self.h = logging.StreamHandler()
        self.h.setLevel(logging.NOTSET)
        self.h.setFormatter(self.fomt()[0])  # 将格式器添加到处理器
        self.logger.addHandler(self.h)  # 将处理器添加到格式器

    def add_file(self, file):
        '''设置文件输出控制台'''
        self.f = logging.FileHandler(filename=file, mode='a', encoding='UTF-8')
        self.f.setLevel(logging.DEBUG)
        self.f.setFormatter(self.fomt()[1])
        self.logger.addHandler(self.f)  # 将文件输出控制台添加到日志器

    @property
    def info(self):
        self.hand()
        self.add_file(log_path)
        return self.logger

    def stream_control(self):
        massage = "用力名称：{casename} 预期结果：{expected} 实际结果：{actual} 测试结果：{result}".format(**self.msg)
        getattr(self.info, self.type)(massage)


# class Logs:
#     # 控制台打印格式：添加格式器 添加日志器名字 日志级别 时间，日志信息
#     format_console = '[%(name)s]  [%(levelname)s]  [%(asctime)s] ------->>>>[%(message)s]'
#     # log文件输出的格式器
#     format_log = '[%(name)s]  [%(levelname)s]  [%(asctime)s] [%(filename)s]------->>>>[%(message)s ]'
#     # 日志级别
#     M_WARNING = logging.WARNING
#     M_DEBUG = logging.DEBUG
#     M_INFO = logging.INFO
#     M_ERROR = logging.ERROR
#
#     def __init__(self):
#         self.logger = logging.getLogger()
#
#     def Log_Run(self, type: str = "debug/info/warning/error", **msg):
#         """
#         :param type: debug/info/warning/error
#         :param msg: :param msg:[case name][expected result][Actual result][finally result:Pass or Fail]
#         :return:
#         """
#         # 设置日志器等级
#         self.logger.setLevel(self.M_DEBUG)
#         # 添加格式器 添加日志器名字 日志级别 时间，日志信息
#         format = logging.Formatter(fmt=self.format_console)
#
#         # 添加控制台处理器
#         hander = logging.StreamHandler()
#         # 设置控制台处理级别
#         hander.setLevel(self.M_WARNING)
#         # 将格式添加至控制台处理器
#         hander.setFormatter(format)
#         # 添加控制台处理器到logger
#         self.logger.addHandler(hander)
#         # 添加文件输出的格式器
#         format2 = logging.Formatter(fmt=self.format_log)
#         # 添加一个文件处理器  输入需要生成的文件名
#         file = logging.FileHandler(filename=log_path, mode='a', encoding='utf-8')
#         # 设置日志输出等级
#         file.setLevel(logging.INFO)
#         # 将格式器添加到日志器
#         file.setFormatter(format2)
#         # 将处理器添加到日志器
#         self.logger.addHandler(file)
#
#         massage = "用力名称：{casename} 预期结果：{expected} 实际结果：{actual} 测试结果：{result}".format(**msg)
#         print(massage)
#         # self.stream_log(type=type, msg=msg)
#         self.logger.debug(massage)
#
#     def stream_log(self, type: str = "debug", **msg):
#         massage = "用力名称：{casename} 预期结果：{expected} 实际结果：{actual} 测试结果：{result}".format(**msg.get('msg'))
#         print(massage)
#         self.logger.debug(massage)


if __name__ == "__main__":
    log = Log(type="debug", casename="A", expected="b", actual="b", result=True)
