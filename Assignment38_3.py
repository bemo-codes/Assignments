import numpy as np
import pandas as pd

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

if __name__ == "__main__":
    main()