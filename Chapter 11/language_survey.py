from Survey import AnonymousSurvey

""" Define a question, and make a survey"""
question = "What lang was your first language?"
my_survey = AnonymousSurvey(question)


""" Show the questions, and store responses to the question."""
my_survey.show_question()
print("Enter q to exit")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)


""" Show the survey results """
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
