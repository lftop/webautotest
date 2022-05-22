import time

from base.BaseWeb import BaseWeb
from utils.Speaker import *


class CustomerTeam(BaseWeb):
    def __init__(self):
        super(CustomerTeam, self).__init__()

    def function__close(self):
        self.close_browser()

    def prediction(self, params):
        flag = 1
        try:
            ele = params.get("ele")
            event = params.get("event")
            print("ele:", ele, "\n")
            while True:
                for item in ele:
                    if len(item) == 3:
                        even, po_str, way = tuple(item)
                        str_for = "even:{0} way:{1} po_str:{2}".format(even, way, po_str)
                        print(str_for)
                        getattr(self, even)(getattr(self, way), po_str)
                    if len(item) == 4:
                        even, po_str, way, v = tuple(item)
                        if v == "input":
                            speak()
                            while True:
                                v = input("请输入验证码...")
                                if v != "":
                                    break
                        str_for = "even:{0} way:{1} po_str:{2} value:{3}".format(even, way, po_str, v)
                        print(str_for)
                        getattr(self, even)(getattr(self, way), po_str, v)
                    time.sleep(2)
                time.sleep(5)
                for eve in event:
                    evet, postr, way = eve
                    getattr(self, evet)(getattr(self, way), postr)
                    time.sleep(2)
                if "验证码不匹配" in self.driver.page_source:
                    super(CustomerTeam, self).__init__()
                    self.prediction(params)
                else:
                    break
        except Exception as e:
            flag = 0
            print(e)
        return flag

    def add_team(self, params):
        flag = 1
        try:
            event, ele = params.get('event'), params.get('ele')
            print(event, '\n', ele)
            # 导航项
            for ditem in event:
                eve, postr, way = ditem
                getattr(self, eve)(getattr(self, way), postr)
                time.sleep(2)

            # 表单提交
            for bitem in ele:
                if len(bitem) == 4: eve, postr, way, v = bitem
                if len(bitem) == 3: eve, postr, way = bitem
                getattr(self, eve)(getattr(self, way), postr, v)

        except Exception as e:
            flag = 0
            print("Error for Code:", e)
        time.sleep(4)
        return flag

    def editteam(self, params):
        flag = 1
        try:
            even = params.get("event", "None")
            ele = params.get("ele", "None")
            # 操作步骤
            for ev in even:
                eve, postr, way = ev
                getattr(self, eve)(getattr(self, way), postr)
                time.sleep(2)
            # 文本框输入
            for txts in ele:
                # print("txts:", txts)
                # print("len:", len(txts))
                if len(txts) == 3:
                    t, p, w = txts
                    print("t:{0} p:{1} w:{1}".format(t, p, w))
                    getattr(self, t)(getattr(self, w),p)
                if len(txts) == 4:
                    T1, postr1, way, T2 = txts
                    T2 = T2.split("=")
                    print(T2)
                    print("e1:{0} postr:{1} way:{2} e2:{3}".format(T1, postr1, way, T2))
                    P_FLG = getattr(self, T2[0])(getattr(self, way), postr1, T2[1])
                    print(P_FLG)
                    if P_FLG != T2[2]:
                        getattr(self, T1)(self, way, postr1)

                if len(txts) == 5:
                    eve1, postr2, way, v, eve2 = txts
                    print("eve1:{0} postr:{1} way:{2} v :{3} eve2:{4} ".format(eve1, postr2, way, v, eve2))
                    getattr(self, eve2)(getattr(self, way), postr2)
                    getattr(self, eve1)(getattr(self, way), postr2, v)
                time.sleep(2)
        except Exception as e:
            flag = 0
            print("Error for Code:", e)  # 后期改成log
        return flag

    def deleteteam(self, params):
        flag = 1
        try:
            even = params.get("event", "None")
            for e in even:
                eve, postr, way = e
                print("eve:",eve,"postr:",postr,"way:",way)
                getattr(self, eve)(getattr(self, way), postr)
                time.sleep(2)
        except Exception as e:
            flag = 0
            print("Error for Code:", e)
        return flag
