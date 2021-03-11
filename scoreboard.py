from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Courier", 18, "bold"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Courier", 18, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()
    # def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER!", align="center", font=("Courier", 18, "bold"))
