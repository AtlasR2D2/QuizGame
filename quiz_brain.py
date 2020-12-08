class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.question_total = len(q_list)
        self.player_score = 0
        self.quiz_over = False

    def next_question(self):
        """method will fetch next question if not at end of list and will return True, otherwise will return False"""
        if not self.quiz_over:
            next_question = self.questions_list[self.question_number]
            guess = input(f"Q.{self.question_number+1}: {next_question.q_and_a_string()}").title()
            if guess == next_question.answer:
                self.player_score += 1
            # Increment Question Number
            self.question_number += 1
            # Check if Quiz is Over
            if self.question_number > self.question_total - 1:
                self.quiz_over = True
        else:
            pass
        return self.quiz_over

    def print_score(self):
        print(f"The quiz is over. Your score was {self.player_score} out of {len(self.questions_list)}.")