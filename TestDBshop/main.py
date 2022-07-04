import pytest
from common.common_path import *
import subprocess

if __name__=="__main__":
    pytest.main(["-s", "-v", "./testcase/test_case01.py", "--alluredir", "./results/report/result"])
    import subprocess

    subprocess.call('allure generate results/report/result/ -o results/report/html --clean', shell=True)
    subprocess.cal1('allure open -h 127.0.0.1 -p  8088 ./results/report/html', shell=True)
# if __name__=="__main__":
      print("Helloword")
#     pytest.main(['-s'])
