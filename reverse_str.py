#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   reverse_str.py
@Time    :   2023/09/19 19:03:29
@Author  :   Cunwang ZHANG 
@Version :   1.0
@Contact :   zhangcwbuaa@qq.com
@Content :   设计一个图灵机，识别逆串
'''
from TMClass import TM

class TM_reverse_str(TM):
    def __init__(self):
        super().__init__()
        self.states = [f"q{i}" for i in range(8)]
        self.alpha = ["a","b"]
        self.alpha_all = ["a","b","B"]
        self.end = {"q6","q7"}
        self.trans_table = {
             "q0":[("q1","B","R"),("q2","B","R"),("q7","B",None)],
             "q1":[("q1","a","R"),("q1","b","R"),("q3","B","L")],
             "q2":[("q2","a","R"),("q2","b","R"),("q5","B","L")],
             "q3":[("q4","B","L"),("q6","b",None),(None,None,None)],
             "q4":[("q4","a","L"),("q4","b","L"),("q0","B","R")],
             "q5":[("q6","a",None),("q4","B","L"),(None,None,None)],
             "q6":[(None,None,None),(None,None,None),(None,None,None)],
             "q7":[(None,None,None),(None,None,None),(None,None,None)]
        }

if __name__=="__main__":
    input_str = "abba"
    tm = TM_reverse_str()
    tm.run(input_str)
    print(tm.tape,tm.state)