import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get('https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]


# question_data = [
#     {
#         "type": "boolean", "difficulty": "easy", "category": "Science: Computers",
#         "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "In most programming languages, the operator ++ is equivalent to the statement += 1.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "The logo for Snapchat is a Bell.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"]
#      },
#     {
#         "type": "boolean",
#          "difficulty": "easy",
#          "category": "Science: Computers",
#          "question": "The Windows 7 operating system has six main editions.",
#          "correct_answer": "True",
#         "incorrect_answers": ["False"]
#      },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"]},
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "Linux was first created as an alternative to Windows XP.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "The programming language &quot;Python&quot; is based off a modified version of JavaScript;.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"]},
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True",
#         "incorrect_answers": ["False"]},
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"]},
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "Time on Computers is measured via the EPOX System.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"]}
# ]
