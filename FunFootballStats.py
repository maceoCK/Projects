f = open("football_stats.txt", "a")
class FootballPlayer:
    def __init__ (self, firstName: str, lastName: str, weight: float, uniform: int, inches: int):
        self.firstname = firstName
        self.lastname = lastName
        self.weight = float(weight)
        self.uniform = uniform
        self.height = str(self.Dimension(inches))

    class Dimension:
        def __init__(self, inches):
            self.inches = inches
            self.feet = (self.inches // 12)
            self.inches = (self.inches%12)
            
        
        def __str__(self):
            return str(f"{self.feet}' {self.inches}''")

def datacollect(Type):
    if (Type == "1"):
        QuarterbackWeight = int(input(f"Please enter your Quarterback's weight in pounds:"))
        QuarterbackUni = int(input(f"Please enter your Quarterback's uniform number: "))
        QuarterbackInches = int(input(f"Please enter your Quarterback's height in inches: "))
        PA = int(input("Please enter your quarterback's passes attempted: "))
        PC = int(input("Please enter your quarterback's passes completed: "))
        while (PC > PA):
            print(f"Passes completed cannot be greater than passes attempted.")
            PC = int(input("Please enter your quarterback's passes completed: "))

        GY = float(input("Please enter yoxur quarterback's gross yards passing: "))
        while ((-20*PC)>GY>(99*PC)):
            print("this is above the maximum possible score")
            GY = float(input("Please enter your quarterback's gross yards passing: "))
        TD = int(input("Please enter your quarterback's number of touchdowns: "))
        while (TD > PC):
            print(f"Touchdowns cannot be greater than passes completed.")
            TD = int(input("Please enter your quarterback's number of touchdowns: "))
        INT = int(input("Please enter your quarterback's number of interceptions: "))
        while (INT>PA):
            print("Interceptions cannot be greater than passes attempted.")
            INT = int(input("Please enter your quarterback's number of interceptions: "))
        while ((INT+PC)>PA):
            print("Interceptions and completed passes are greater than attempted passes.")
            INT = int(input("Please enter your quarterback's number of interceptions: "))
        
        QBarray = [QuarterbackWeight, QuarterbackUni, QuarterbackInches, PA,TD, GY, PC, INT]
        return QBarray
    if (Type == "3"):
        RunningbackWeight = float(input(f"Please enter your Runningback's weight in pounds:"))
        RunningbackUni = int(input(f"Please enter your Runningback's uniform number: "))
        RunningbackInches = int(input(f"Please enter your Runningback's height in inches: "))
        RunningbackAtt = int(input(f"Please enter your Runningback's attempts: "))
        RunningbackTD = int(input(f"Please enter your runningback's touchdowns: "))
        RunningbackYD = float(input(f"Please enter your runningback's yards: "))
        RBarray = [RunningbackWeight, RunningbackUni, RunningbackInches, RunningbackAtt, RunningbackTD, RunningbackYD]
        return RBarray

class Runningback(FootballPlayer):
    def __init__(self, firstName: str, lastName: str, weight: float, uniform: int, inches: int, attempts: int, yards: float, touchdowns: int):
        super().__init__(firstName, lastName, weight, uniform, inches)
        if (isinstance((attempts,touchdowns), int) != 1 | isinstance(yards, (int,float)) != 1):
            e = "value error with attempts, touchdowns, or yards"
            raise ValueError(e)
        self.attempts = attempts
        self.yards = yards
        self.touchdowns = touchdowns
        

        


class Quarterback(FootballPlayer):
    def __init__(self, firstName: str, lastName: str, weight: float, uniform: int, inches: int, attempts: int, yards: float, touchdowns: int, completed: int, interceptions: int):
        super().__init__(firstName, lastName, weight, uniform, inches)
        if (isinstance((attempts,touchdowns,completed, interceptions), int) != 0 | isinstance(yards, (int,float)) != 1):
            e = "Value error with quarterback inputs"
            raise ValueError(e)
        self.attempts = attempts
        self.yards = yards
        self.touchdowns = touchdowns
        self.completed = completed
        self.interceptions = interceptions
    def QBscore(self):
        return ((100*(((((self.completed/self.attempts)*100 )- 30)/20) + ((self.yards/self.attempts - 3)/4) +((self.touchdowns/self.attempts*100)/5) +((1/4)*(9.5-((self.interceptions/self.attempts)*100))))) / 6)    

def main(desired):
    if (desired != "4"):
        if (desired == "1"):
            QuarterbackFirst = input(f"Please enter your Quarterback's first name: ")
            QuarterbackLast  = input(f"Please enter your Quarterback's last name: ")
            
            Quarterbackelse = datacollect(desired)
            QB = Quarterback(str(QuarterbackFirst),str(QuarterbackLast),Quarterbackelse[0],Quarterbackelse[1],Quarterbackelse[2],Quarterbackelse[3], Quarterbackelse[4],Quarterbackelse[5],Quarterbackelse[6],Quarterbackelse[7])
            print (f"\nQuarterback {QB.firstname} {QB.lastname}: \nWeight: {QB.weight} LBS \nUniform: {QB.uniform}\nHeight: {QB.height} \nAttempts: {QB.attempts} \nCompleted: {QB.completed}\nYards: {QB.yards}\nTouchdowns: {QB.touchdowns} \nInterceptions: {QB.interceptions} \nOverall Quarterback score: {QB.QBscore()}")
            f.write(f"\nQuarterback {QB.firstname} {QB.lastname}: \nWeight: {QB.weight} LBS \nUniform: {QB.uniform}\nHeight: {QB.height} \nAttempts: {QB.attempts} \nCompleted: {QB.completed}\nYards: {QB.yards}\nTouchdowns: {QB.touchdowns} \nInterceptions: {QB.interceptions} \nOverall Quarterback score: {QB.QBscore()}")
            restart()
        elif (desired == "2"):
            LinemanFirst = input(f"Please enter your Lineman's first name: ")
            LinemanLast  = input(f"Please enter your Lineman's last name: ")
            LinemanWeight = float(input(f"Please enter your Lineman's weight in pounds:"))
            LinemanUni = int(input(f"Please enter your Lineman's uniform number: "))
            LinemanInches = int(input(f"Please enter your Lineman's height in inches: "))
            
            Lineman = FootballPlayer(str(LinemanFirst), str(LinemanLast), LinemanWeight, LinemanUni, LinemanInches)
            print (f"\nLineman: \nFirst Name: {Lineman.firstname} \nLast Name: {Lineman.lastname} \nWeight: {Lineman.weight} LBS \nUniform: {Lineman.uniform}\nHeight: {Lineman.height}")
            f.write (f"\nLineman: \nFirst Name: {Lineman.firstname} \nLast Name: {Lineman.lastname} \nWeight: {Lineman.weight} LBS \nUniform: {Lineman.uniform}\nHeight: {Lineman.height}")
            restart()
        elif (desired == "3"):
            RunningbackFirst = input(f"Please enter your Runningback's first name: ")
            RunningbackLast  = input(f"Please enter your Runningback's last name: ")

            Runnerelse = datacollect(desired)
            runner = Runningback(str(RunningbackFirst),str(RunningbackLast),Runnerelse[0],Runnerelse[1],Runnerelse[2],Runnerelse[3], Runnerelse[4],Runnerelse[5])
            print (f"\nRunningback: \nFirst Name: {runner.firstname} \nLast Name: {runner.lastname} \nWeight: {runner.weight} LBS \nUniform: {runner.uniform}\nHeight: {runner.height} \nAttempts: {runner.attempts} \nYards: {runner.yards}\nTouchdowns: {runner.touchdowns}\n")
            f.write(f"\nRunningback: \nFirst Name: {runner.firstname} \nLast Name: {runner.lastname} \nWeight: {runner.weight} LBS \nUniform: {runner.uniform}\nHeight: {runner.height} \nAttempts: {runner.attempts} \nYards: {runner.yards}\nTouchdowns: {runner.touchdowns}\n")
            restart()
        else:
            print("Please enter a value listed.")
            restart()
        f.close()
def restart():
    print(f"\n\n")
    f.write(f"\n\n")
    hold = input(f"What type of player do you want to input data for?\nType (1) if you want to input data for a Quarterback\nType (2) if you want to input data for a Lineman\nType (3) if other type of player\nType (4) to exit\nInput: ")
    main(hold)
restart()