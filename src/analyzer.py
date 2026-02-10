def calculate_statistics(student_scores):
    min_score=min(student_scores.values())
    max_score=max(student_scores.values())
    average_score=sum(student_scores.values())/len(student_scores)

    items=student_scores.items()
    sorted_items=sorted(items,key=lambda x:x[1],reverse=True)
    scores=[]
    for name,score in sorted_items:
        scores.append({
            'name':name,
            'score':score
        })

    stats = {
        "scores": scores,
        "max": max_score,
        "min": min_score,
        "average": average_score
    }

    return stats

def print_statistics(stats):
    print(f"学生的最高分为{stats['max']}, 最低分为{stats['min']}")
    print(f"学生的平均分为{stats['average']}")


