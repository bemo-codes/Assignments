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
    
    plt.scatter(
        df[df["FinalResult"] == 1]["SleepHours"],
        df[df["FinalResult"] == 1]["FinalResult"],
        color = "green",
        marker = "o",
        label = "Passed"
    )

    plt.scatter(
        df[df["FinalResult"] == 0]["SleepHours"],
        df[df["FinalResult"] == 0]["FinalResult"],
        color = "red",
        marker = 'x',
        label = "Failed"
    )

    plt.title("Sleep Hours vs Result")
    plt.xlabel("Sleep Hours")
    plt.ylabel("Result")
    plt.yticks([0,1],['Failed', 'Passed'])
    plt.legend()
    plt.show()

    #Here we get to observe that the students who have completed more than 5 assignments have passed in exam and others have failed
if __name__ == "__main__":
    main()