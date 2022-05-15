import os

# 项目目录
Dir_Project = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 配置文件目录
config_dir = os.path.join(Dir_Project, "config/config.ini")
# 测试用例目录
test_case_dir = os.path.join(Dir_Project, "data/testcase")
# 测试用例数据目录
test_case_data_dir = os.path.join(Dir_Project, "data/testcase_data")
#log文件生成地址
log_path=os.path.join(Dir_Project,"results/log/log1.log")

print(log_path)