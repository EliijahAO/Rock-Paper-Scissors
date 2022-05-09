from tkinter import *
import random
class Game(Frame):
    def __init__(self, master=None):
        self.wins = IntVar()
        self.winsNum = 0
        self.losses = IntVar()
        self.lossesNum = 0

        Frame.__init__(self, master)
        self.grid(padx=20, pady=20)
        self.createWidgets()

    def createWidgets(self):
        print("ewe")
        self.rock = Button(self)
        self.rock["command"] = lambda: self.chooseWinner("rock")
        self.rockPhoto = PhotoImage(file="rock.png")
        self.rock.config(image=self.rockPhoto, width="263", height="263", justify='center')

        self.scissors = Button(self)
        self.scissors["command"] = lambda: self.chooseWinner("scissors")
        self.scissorsPhoto = PhotoImage(file="scissors.png")
        self.scissors.config(image=self.scissorsPhoto, width="263", height="263", justify='center')

        self.paper = Button(self)
        self.paper["command"] = lambda: self.chooseWinner("paper")
        self.paperPhoto = PhotoImage(file="paper.png")
        self.paper.config(image=self.paperPhoto, width="263", height="263", justify='center')

        self.rock.grid(row=2, column=0)
        self.paper.grid(row=2, column=1)
        self.scissors.grid(row=2, column=2)

        self.result = Label(self, justify="center")
        self.result["font"] = ("Comic Sans MS", 16)
        self.result["fg"] = "#ff220c"
        self.result.grid(row=5, sticky=W, columnspan=5)

        self.winsLabel = Label(self, text="You")
        self.winsLabel.grid(row=0, column=0, stick=W)
        self.winsCount = Label(self, textvariable=self.wins)
        self.winsCount["fg"] = "#70d6ff"
        self.winsCount["font"] = ("Comic Sans MS", 13)
        self.winsCount.grid(row=1, column=0, sticky=W)

        self.lossesLabel = Label(self, text="Robot")
        self.lossesLabel.grid(row=0, column=3, stick=E)
        self.lossesCount = Label(self, textvariable=self.losses)
        self.lossesCount["fg"] = "#70d6ff"
        self.lossesCount["font"] = ("Comic Sans MS", 13)
        self.lossesCount.grid(row=1, column=3, sticky=E)

    def chooseWinner(self, action):
        self.user_choice = action
        self.robot_choice = random.choice(["rock","paper","scissors"])

        if self.user_choice == self.robot_choice:
            self.result["text"] = "Tie!"

        elif self.user_choice == "rock":
            if self.robot_choice == "paper":
                self.lossesNum += 1
                self.losses.set(self.lossesNum)
                self.result["text"] = "You lose to robot... {} covers {}".format(self.robot_choice, self.user_choice)
            else:
                self.winsNum += 1
                self.wins.set(self.winsNum)
                self.result["text"] = "You win! {} smashes {}".format(self.user_choice, self.robot_choice)

        elif self.user_choice == "paper":
            if self.robot_choice == "scissors":
                self.lossesNum += 1
                self.losses.set(self.lossesNum)
                self.result["text"] = "You lose to robot... {} cut {}".format(self.robot_choice, self.user_choice)
            else:
                self.winsNum += 1
                self.wins.set(self.winsNum)
                self.result["text"] = "You win! {} covers {}".format(self.user_choice, self.robot_choice)

        elif self.user_choice == "scissors":
            if self.robot_choice == "rock":
                self.lossesNum += 1
                self.losses.set(self.lossesNum)
                self.result["text"] = "You lose to robot... {} smashes {}".format(self.robot_choice, self.user_choice)
            else:
                self.winsNum += 1
                self.wins.set(self.winsNum)
                self.result["text"] = "You win! {} cut {}".format(self.user_choice, self.robot_choice)



root = Tk()
root.wm_title("Rock Paper Scissors")
app = Game(master=root)
app.mainloop()
root.destroy()

   








