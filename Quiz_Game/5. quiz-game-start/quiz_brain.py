class quiz_brain:
    def __init__(self,list):
        self.ques_no=0
        self.ques_list=list
        self.score=0
    def still_has_ques(self):
        if self.ques_no<len(self.ques_list):
            return True
        else:
            return False
    def check_ans(self,user_answer):
        if self.ques_list[self.ques_no].ans==user_answer:
            print("Correct")
            self.score+=5
        else:
             print("Wrong")
             self.score-=2
        print(self.score)
    def next_ques(self):
            user_answer=input(f"Q{(self.ques_no)+1} {self.ques_list[self.ques_no].text} True/False ")
            self.check_ans(user_answer)
            self.ques_no+=1