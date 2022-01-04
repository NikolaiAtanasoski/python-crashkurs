from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "Which pokemon do you think is the best?"
pokemon_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
pokemon_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Pokemon: ")
    if response == "q":
        break
    pokemon_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
pokemon_survey.show_results()
