import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")

    print(df.head())
    print(df.tail())
    print(df.shape)
    print(df.columns)
    print(df.columns.dtype)

    total_students = len(df)
    passed_students = (df["FinalResult"] == 1).sum()
    failed_student = (df["FinalResult"] == 0).sum()

    print("Total number of students: ", total_students)
    print("Passed students: ", passed_students)
    print("Failed students: ", failed_student)

    print("Average study hours: ", (df["StudyHours"]).mean())
    print("Average attendance: ", (df["Attendance"]).mean())
    print("Maximum Previous Score", (df["PreviousScore"].max()))
    print("Maximum Sleep Hours: ", (df["SleepHours"].max()))

    print(df["FinalResult"].value_counts(normalize=True)*100)

    #Higher Study Hours increase the chances of passing as you observe the student who've studied above 4 hr mark have all passed so putting in more study hours is more beneficial over attendance.
    
    print(df["StudyHours"].dtype)
    print(df["Attendance"].dtype)

    df.boxplot(
        column= "Attendance",
        color = 'black'
        )

    plt.title("Attendance box plot")
    plt.ylabel("Attendance")
    plt.show()

if __name__ == "__main__":
    main()