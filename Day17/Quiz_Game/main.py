from data import question_data
from question_model import question
from quiz_brain import quiz_brain
question_bank=[]
for element in question_data:
    Q_text=element["text"]
    Q_ans=element["answer"]
    Que=question(Q_text,Q_ans)
    question_bank.append(Que)
quiz=quiz_brain(question_bank)
while quiz.still_has_ques():
    quiz.next_ques()
