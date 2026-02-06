
def get_scores_from_file(filename):
    student_scores={}
    with open(filename,"r",encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            try:
                line=line.split(",")
                student_scores[line[0]]=float(line[1])
            except ValueError:
                print(f"接受格式错误！跳过该行{line}")
    return student_scores



def get_scores():

    """
    输入学生成绩
    :return: 返回学生成绩字典
    """
    student_scores={}
    while True:
        name=input("请输入姓名：")
        if name=="q":
            break
        try:
            score=float(input("请输入分数："))

        except Exception as e:
            print("分数格式输入错误！！！")
            continue
        student_scores[name]=score

    print("输入结束。。。")
    return student_scores

def calculate_statistics(student_scores):
    min_score=min(student_scores.values())
    max_score=max(student_scores.values())
    average_score=sum(student_scores.values())/len(student_scores)
    return min_score, max_score,average_score

def print_statistics(min_score, max_score, average_score):
    print(f"学生的最高分为{max_score},最低分为{min_score}")
    print(f"学生的平均分为{average_score}")


def main():
    choice=input("请输入输入源：1.文件 2.命令行")
    if choice=="1":
        student_scores=get_scores_from_file("scores.txt")
    elif choice=="2":
        student_scores=get_scores()
    else:
        print("无效输入")
        return


    min_score,max_score,average_score=calculate_statistics(student_scores)
    print_statistics(min_score,max_score,average_score)

#解释一下下面这一段的作用
if __name__ == "__main__":
    main()















