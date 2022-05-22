# -*-coding:utf-8-*-
import allure
import pytest

from PageModel.dbadmin.CustomerTeam import CustomerTeam
from utils.GetFileData import ExcelCase, YamlData

condition = "冒烟测试"


# @pytest.mark.skipif(condition == "冒烟测试", reason="smoke_test")
@allure.feature("用户组模块")
class Test_case01:
    Teat = CustomerTeam()
    excel1_obj = ExcelCase(filename="DBTESTCASE.xlsx", sheetname="DBSHOPADMIN")
    yam_obj = YamlData("usermoduledata.yaml")
    Index = 0

    def getdata(self, e_index, y_key):
        excel = self.excel1_obj.get_items()[e_index]
        print("excel:", excel)
        yaml = self.yam_obj.get_case_data(excel.get(y_key))
        print("yaml", yaml)
        return yaml

    def setup_class(self):
        """打开浏览器"""
        print("打开浏览器")
        self.Teat

    def teardown_class(self):
        """关闭浏览器"""
        self.Teat.function__close()
        print("关闭浏览器")

    @pytest.mark.run(order=1)
    @allure.story("添加用户组")
    @pytest.mark.dependency()
    def test_addteam(self):
        # excel = self.excel1_obj.get_items()[self.Index]
        # print("excel:", excel)
        # yaml = self.yam_obj.get_case_data(excel.get(self.excel1_obj.TESTDATA))
        # print("yaml", yaml)
        with allure.step("登录成功"):
            assert self.Teat.prediction(self.getdata(self.Index,self.excel1_obj.TESTDATA).get("prediction").get('login')) == True
        with allure.step("导航至用户组界面添加成功"):
            assert self.Teat.add_team(self.getdata(self.Index,self.excel1_obj.TESTDATA).get("payload")) == True
        assert True

    @pytest.mark.run(order=2)
    @allure.story("编辑用户组")
    # @pytest.mark.dependency(depends=["Test_case01::test_addteam"])
    def test_edit(self):
        self.Index += 1
        print(self.Index)
        with allure.step("导航至用户组界面添加成功"):
           self.Teat.editteam(self.getdata(self.Index,self.excel1_obj.TESTDATA).get("payload"))

    @pytest.mark.run(order=3)
    @allure.story("删除用户组")
    @pytest.mark.dependency(depends=["Test_case01::test_addteam"])
    def delete(self):
        self.Index+=1
        with allure.step("用户组删除操作"):
            payload=self.Teat.editteam(self.getdata(self.Index,self.excel1_obj.TESTDATA).get("payload"))
            assert self.Teat.deleteteam(payload)
