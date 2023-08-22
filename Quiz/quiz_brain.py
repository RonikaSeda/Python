class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        while self.question_number <= 11:
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"\nQ.{self.question_number}: {current_question.text} True/False? ")
            self.chek_answer(user_answer, current_question.answer)

    def chek_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}\nYour current score is: {self.score}/{self.question_number}")
        


