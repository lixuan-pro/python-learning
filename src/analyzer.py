def calculate_statistics(student_scores):
    min_score=min(student_scores.values())
    max_score=max(student_scores.values())
    average_score=sum(student_scores.values())/len(student_scores)
    return min_score, max_score,average_score

def print_statistics(min_score, max_score, average_score):
    print(f"学生的最高分为{max_score},最低分为{min_score}")
    print(f"学生的平均分为{average_score}")

