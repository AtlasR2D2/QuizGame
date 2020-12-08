from data import question_data


class Question:
    def __init__(self, q_text, q_answer):
        self.question = q_text
        self.answer = q_answer

    def q_and_a_string(self):
        return f"{self.question} (True/False)?: "

# Load Question Data to list as instances of Question Class
# List comprehension used
question_bank=[]
for i in range(len(question_data)):
    q_x = question_data[i]["text"]
    a_x = question_data[i]["answer"]
    question_bank.append(Question(q_text=q_x, q_answer=a_x))

