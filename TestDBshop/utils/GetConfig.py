import configparser
from common.common_path import config_dir


def getconfig(option="sys", key=""):
    try:
        cf = configparser.ConfigParser()
        cf.read(config_dir, encoding='utf-8')
        return cf.get(option, key) if key != "" else dict(cf.items(option))
    except Exception as e:
        print("文件操作异常%s" % e)
