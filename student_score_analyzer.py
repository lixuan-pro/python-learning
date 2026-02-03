
flag=True
student_score={}
while flag:
    name=input("请输入姓名：")
    if name.lower()=="q":
        print("已退出记录。。。")
        break

    try:
        score=int(input("请输入成绩："))

    except Exception as e:
        print("成绩不能为非数字！")
        continue

    student_score[name]=score

print("开始统计情况排名分数：")
count=0
average=0
max=0
min=101
for name,score in student_score.items():
    count=count+1
    average=average+score
    if score>max:
        max=score
        max_name=name

    if score<min:
        min=score
        min_name=name
print(f"学生人数为{count}")
print(f"平均分为：{average/count}")
print(f"最高分为：{max},最低分为：{min}")



