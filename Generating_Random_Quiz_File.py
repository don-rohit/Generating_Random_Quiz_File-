import random
import os

# Quiz on US State Capitals for 35 students in a class
# Randomize the order of Questions so that each quiz is Unique

# 50 Questions
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier',
'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# We have to Create 35 different Quiz paper
# Containing all mutiple Questions in random order
# Provide Correct answer and 3 random wrong answer for each question in random order

os.makedirs(".\QuestionPaper")
os.makedirs(".\Solution")

#Genearte 35 quiz files
for quizNum in range(1,36):
    paper = open("QuestionPaper\Student"+str(quizNum)+".txt" , 'w') # question paper
    solution = open("Solution\SolutionStudent"+str(quizNum)+".txt" , 'w') # Solution

    # Header
    paper.write("Name:\n\nDate:\n\nRoll No:\n\n\n")
    paper.write((" "*20)+'State Capital Quiz\n\n')

    # Shuffle the order of states
    states = list(capitals.keys())
    random.shuffle(states)

    for quesNo in range(50):
        # Get right and wrong answer
        correctAnswer = capitals[states[quesNo]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer,3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)

        # Question
        paper.write(str(quesNo+1) + ". What is the capital of " +states[quesNo]+ "?\n")

        # Answer
        for k in range(len(answerOptions)):
            paper.write("\t"+chr(65+k)+". "+answerOptions[k]+"\n")
        paper.write("\n")

        # Solution in answer file
        solution.write(str(quesNo+1)+". "+ 'ABCD'[answerOptions.index(correctAnswer)] +"\n")
    paper.close()
    solution.close()