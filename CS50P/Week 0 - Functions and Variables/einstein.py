def convertMassToJoules(mass):
     mass = int(mass)
     c = 300000000
     joules = mass * c * c
     return joules

def main():
    mass = input("Enter a mass: ")
    joules = convertMassToJoules(mass)
    print(joules)

if __name__ == "__main__":
    main()
