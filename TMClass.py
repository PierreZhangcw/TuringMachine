#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   TMClass.py
@Time    :   2023/09/19 16:47:42
@Author  :   Cunwang ZHANG 
@Version :   1.0
@Contact :   zhangcwbuaa@qq.com
@Content :   图灵机模型的基类
'''

class TM:
    def __init__(self):
        self.name = "Turing Machine"
        # 状态
        self.states = []
        # 字母表
        self.alpha = []
        # 空白符
        self.black = "B"
        # 初始状态
        self.start = "q0"
        # 接受状态
        self.end = None
        # 指针位置
        self.point = 0
        # 带子上的内容
        self.tape = ["B"]
        # 当前状态
        self.state = "q0"
    def reset(self):
        self.tape = ["B"]
        self.point = 0
        self.state = self.start
    def transition(self):
        value_index = self.alpha_all.index(self.tape[self.point])
        state,value,action = self.trans_table[self.state][value_index] 
        return state,value,action
    def move(self,value,action):
        # 修改带子上的值
        self.tape[self.point] = value
        # self.tape = list("".join(self.tape).strip("B"))
        # 移动指针
        if action == "R":
            if self.tape[0] == "B":
                self.tape = self.tape[1:]
            else:
                self.point += 1
                if self.point >= len(self.tape):
                    self.tape.append("B")
        elif action == "L":
            self.point -= 1
            if self.point == -1:
                self.point = 0
                self.tape = ["B"] + self.tape
    def run(self,input_str):
        self.tape = list(input_str)
        self.point = 0
        step = 1
        while True:
            print(f"step-{step}:",end="")
            print("".join(self.tape[:self.point] + ["["+self.state+"]"] + self.tape[self.point:]))
            next_state,value,action = self.transition()
            if not action:
                # print(next_state)
                break
            self.move(value,action)
            if next_state in self.end:
                break
            self.state = next_state
            step += 1
        self.tape = list("".join(self.tape).strip("B"))
    def result(self):
        return "".join(self.tape)