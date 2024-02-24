import os

class Convertr():
    # (Stephen) Clears the console in order to keep view less cluttered
    def clear(self):
        if os.name == "nt":  # (Stephen) Windows :(
            _ = os.system("cls")
        else:  # (Stephen) Linux, MacOS or other Unix OS
            _ = os.system("clear")

    # (Sam) Main Menu
    def main(self):
        print("What are you starting off with?")
        print("1. JSON")
        print("2. CSV")
        print()
        self.startingType = input("Enter: ")
        self.clear()

        print("What would you like to convert to?")
        print("1. JSON")
        print("2. CSV")
        print()
        self.endingType = input("Enter: ")
        self.clear()

        print(f"Make sure all the {self.startingType} files you want to convert are in the \"Input\" folder and press ENTER when ready.")
        self.fileLocation = input("")
        self.clear()

        print(f"Converting {self.startingType} to {self.endingType}")


# (Sam) Start the program and create the main class.
if __name__ == "__main__":
    convertr = Convertr()
    convertr.main()
