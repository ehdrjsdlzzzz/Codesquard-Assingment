import random

class BaseballGame:

    def __init__(self):
        self.randNum = BaseballGame.generateRandom()

    @staticmethod
    def generateRandom():
        numList = [1,2,3,4,5,6,7,8]
        randNum = []
        while len(randNum) != 3:
            randNum = list(set(random.sample(numList, 3)))
        return randNum

    def compareLists(self, userInput, randNum):
        userInputSet = set(userInput)
        randNumSet = set(randNum)
        return len(userInputSet - (userInputSet - randNumSet))

    def getStrikeCount(self,userInput, randNum):
        count = 0
        for a, b in zip(userInput, randNum):
            if a == b:
               count += 1
        return count

    def getBallCount(self, userInput, randNum):
        return self.compareLists(userInput, randNum) - self.getStrikeCount(userInput, randNum)

    def displayResult(self, strike, ball):
        if strike == 3: print("{} 스트라이크".format(strike))
        elif strike + ball == 0 : print("낫싱")
        elif strike == 0: print("{} 볼".format(ball))
        elif ball == 0: print("{} 스트라이크".format(strike))
        else: print("{} 스트라이크 {} 볼".format(strike, ball))

    def isStrike(self, strike, ball):
        return strike == 3

    def round(self, randNum):
        userInput = list(map(int, list(input("숫자를 입력해주세요 ex)123 : "))))
        strike = self.getStrikeCount(userInput, randNum)
        ball = self.getBallCount(userInput, randNum)
        self.displayResult(strike, ball)
        if self.isStrike(strike, ball):
            print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
            return True
        return False

    def play(self):
        print("컴퓨터의 숫자 : {}".format(self.randNum))
        while self.round(self.randNum) == False:
            continue
