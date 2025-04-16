from tkinter import  *


THEME_COLOR ="#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz Game")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        # Labels
        score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="SOME QUESTION",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=0)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=1)


        # Buttons



        self.window.mainloop()