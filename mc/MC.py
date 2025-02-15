# old exams at https://www.cse.msu.edu/~cse231/Online/Exams/
# copy text of old exam into text file and put in folder with .py file (only tested exam2c19f and exam2c 18f)
# make sure there are no empty lines between answers of a question
# Ex.
# A) 2
# B) 5
# is good
#
# A) 2
#
# B) 5
# will cause issues, make sure the remove the empty line before running
#
# Percentage of correct answers given at the end is based on % of questions
# answered correctly on the first try
#
#
# q to quit answering early, next question is shown once correct answer is given

questions_hit = False
question_number = 1
next_question_string = "02."
answer_dict = dict()
answers_hit = False
second_form = False
key_line = True
zip_ready = False
correct = True
correct_counter = 0
reading_question = False
first_blank = True
need_answer = False
reading_answers = False
exit = False

while True:
    try:
        file_name = input("Enter test file name: ")
        fp = open(file_name,"r")
        break
    except FileNotFoundError:
        print("File does not exist")

for line in fp:
    if "Form" in line:
        if second_form:
            answers_hit = True
            continue
        second_form = True
        continue
    if answers_hit:
        if key_line and line.strip():
            key_line_list = line.split()
            key_line = False
        elif not key_line:
            answer_line_list = line.split()
            zip_ready = True
        if zip_ready:
            temp_dict = dict(zip(key_line_list,answer_line_list))
            answer_dict |= temp_dict
            zip_ready = False
            key_line = True


    if "01." in line:
        questions_hit = True
        answers_hit = False
        reading_question = True
        print("Enter answers or \"q\" to quit\nIf an answer is correct the next question will be shown")
    if questions_hit:
        print(line, end="")
    if next_question_string in line:
        reading_question = True
        question_number += 1
        if (question_number + 1) < 10:
            next_question_string = "0"+ str(question_number+1) +"."
        else:
            next_question_string = str(question_number + 1)+"."
    if reading_question and "A)" in line:
        reading_answers = True
    if reading_answers and line.strip() == "":
        need_answer = True

    if need_answer:
        answer = input("Input Answer: ")
        if answer.lower() == "q":
            exit = True
            break
        while answer.lower() not in answer_dict[str(question_number)].lower():
            correct = False
            print("Incorrect")
            answer = input("Input Answer: ")
        if correct:
            correct_counter += 1
        if len(answer_dict[str(question_number)]) > 1:
            print("Correct Answers: ",answer_dict[str(question_number)])
        correct = True
        reading_answers = False
        reading_question = False
        need_answer = False

if not exit:
    answer = input("\nInput Answer: ")
    while answer.lower() not in answer_dict[str(question_number)].lower():
        correct = False
        print("Incorrect")
        answer = input("Input Answer: ")
    if correct:
        correct_counter += 1
    if len(answer_dict[str(question_number)]) > 1:
        print("Correct Answers: ", answer_dict[str(question_number)])
    correct = True

if exit:
    percent_correct = (correct_counter / (question_number-1)) * 100
else:
    percent_correct = (correct_counter / question_number) * 100

print(f"Percent correct: {percent_correct:.2f}%")