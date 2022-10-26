import pandas as pd

# =============================================================================
# Q1
# =============================================================================

df = pd.read_csv("attacks.csv", encoding = "ISO-8859-1")


def question1():
    print("\nQ1")
    print("Location \t\t\t Attacks")
    print(df["Location"].value_counts().head(1))


def question2():
    print("\nQ2")
    print("Country \t Attacks")
    print(df["Country"].value_counts().head(6))


def question3():
    print("\nQ3")
    print("Country \t Fatal Attacks")

    fatal = df["Country"][df["Fatal"]=="Y"]
    print(fatal.value_counts().head(6))


def question4():
    print("\nQ4")

    surfing = df["Activity"][df["Activity"]=="Surfing"]
    scubaDiving = df["Activity"][df["Activity"]=="Scuba"]

    print("Number of attacks when surfing: ", surfing)
#    print("Number of attacks when scuba diving: ", scubaDiving)



def main():
    question1()
    question2()
    question3()
    question4()


main()




