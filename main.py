from question_model import Question, question_bank
from data import question_data
from quiz_brain import QuizBrain

# Initialise new QuizBrain object
quiz = QuizBrain(question_bank)
quiz_over = False


while not quiz_over:
    quiz_over = quiz.next_question()
    if not quiz_over:
        pass
    else:
        quiz.print_score()


