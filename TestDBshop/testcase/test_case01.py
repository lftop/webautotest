# -*-coding:utf-8-*-
import pytest
from base.BaseWeb import BaseWeb
from PageModel.dbadmin import CustomerTeam
from utils.GetConfig import *

class Test_Case01:
    @property
    def getdata(self):
        excel1_obj=ExcelCase(filename="DBTESTCASE.xlsx", sheetname="DBSHOPADMIN")
        yam_obj=YamlData("usermoduledata.yaml")
        return excel1_obj,yam_obj

    def setup_class(self):
        """打开浏览器"""
        pass

    def teardown_class(self):
        """关闭浏览器"""
        pass



