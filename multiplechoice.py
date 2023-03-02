from question import Question

question_prompts = [
    "What planet do we live on?\n(a) Mars\n(b) Earth\n(c) Jupiter\n",
    "What is the color of the sky?\n(a) Yellow\n(b) Purple\n(c) Blue\n",
    "Which of these is a vegetable?\n(a) Carrot\n(b) Papaya\n(c) Tomato\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def run_game(questions_list):
    score = 0
    for question in questions_list:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions_list)))


run_game(questions)

