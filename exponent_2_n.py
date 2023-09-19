#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   exponent_2_n.py
@Time    :   2023/09/19 16:57:31
@Author  :   Cunwang ZHANG 
@Version :   1.0
@Contact :   zhangcwbuaa@qq.com
@Content :   图灵机模型，用来计算2的n次方
'''
from TMClass import TM

class TM_2_n(TM):
    def __init__(self):
        super().__init__()
        self.states = [f"q{i}" for i in range(8)]
        self.alpha = ["0","1","x"]
        self.alpha_all = ["0","1","x","B"]
        self.end = {"q7"}
        self.trans_table = {
             "q0":[("q1","B","R"),("q7","B","R"),(None,None,None),(None,None,None)],
             "q1":[("q1","0","R"),("q2","1","R"),(None,None,None),(None,None,None)],
             "q2":[("q3","x","R"),(None,None,None),(None,None,None),(None,None,None)],
             "q3":[("q3","x","R"),(None,None,None),(None,None,None),("q4","B","L")],
             "q4":[("q4","0","L"),("q6","1","L"),("q5","0","R"),(None,None,None)],
             "q5":[("q5","0","R"),(None,None,None),(None,None,None),("q4","0","L")],
             "q6":[("q6","0","L"),(None,None,None),(None,None,None),("q0","B","R")],
             "q7":[(None,None,None),(None,None,None),(None,None,None),(None,None,None)]
        }

if __name__=="__main__":
    input_str = "00000010"
    tm = TM_2_n()
    tm.run(input_str)
    print(tm.tape.count("0"),len(tm.tape))