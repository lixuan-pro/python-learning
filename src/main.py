import pandas as pd
from input_source import InputSource
from report_writer import save_report
from analyzer import calculate_statistics, print_statistics


def main():
    choice=input("请选择一种输入方式：1.cil 2.file 3.csv")
    if choice=="1":
        source=InputSource("cli")
    elif choice=="2":
        source=InputSource("file","../data/scores.txt")
    elif choice=="3":
        source=InputSource("csv", "../data/scores.csv")
    else:
        print("输入无效。。。")
        return
    student_scores=source.get_scores()
    min_score,max_score,average_score=calculate_statistics(student_scores)
    print_statistics(min_score,max_score,average_score)

    use_ai = input("是否使用 AI 分析？(y/n)：")

    if use_ai.lower() == "y":
        from ai_analyzer import analyze_scores_with_ai

        ai_result = analyze_scores_with_ai(student_scores)
        print("\nAI 分析结果：")
        print(ai_result)

        save=input("是否保存为分析报告？y/n")
        if save.lower() == "y":
            path=save_report(ai_result)
            print(f"文件已经保存到：{path}")


if __name__ == "__main__":
    main()



