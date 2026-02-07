import pandas as pd
from input_source import InputSource

def calculate_statistics(student_scores):
    min_score=min(student_scores.values())
    max_score=max(student_scores.values())
    average_score=sum(student_scores.values())/len(student_scores)
    return min_score, max_score,average_score

def print_statistics(min_score, max_score, average_score):
    print(f"学生的最高分为{max_score},最低分为{min_score}")
    print(f"学生的平均分为{average_score}")


def main():
    choice=input("请选择一种输入方式：1.cil 2.file 3.csv")
    if choice=="1":
        source=InputSource("cli")
    elif choice=="2":
        source=InputSource("file","scores.txt")
    elif choice=="3":
        source=InputSource("csv","scores.csv")
    else:
        print("输入无效。。。")
        return
    student_scores=source.get_scores()
    min_score,max_score,average_score=calculate_statistics(student_scores)
    print_statistics(min_score,max_score,average_score)


if __name__ == "__main__":
    main()

