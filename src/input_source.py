import pandas as pd
class InputSource:
    def __init__(self,source_type,filename=None):
        self.source_type = source_type
        self.filename = filename

    def get_scores(self):
        if self.source_type == 'cli':
            return self._get_from_cli()
        elif self.source_type == 'file':
            return self._get_from_file()
        elif self.source_type == 'csv':
            return self._get_from_csv()
        else:
            print("输入错误")

    def _get_from_cli(self):

        student_scores={}
        while True:

            name=input("请输入姓名：")
            if name=='q':
                print("已退出。。。")
                break
            try:
                score=float(input("请输入学生分数："))
                student_scores[name]=score
            except ValueError:
                print(f"分数格式输入错误！")
                continue
        return student_scores

    def _get_from_file(self):
        student_scores={}
        with open(self.filename,'r') as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                try:
                    line=line.split(",")
                    student_scores[line[0]]=float(line[1])
                except ValueError:
                    print(f"格式错误，跳过该行")

        return student_scores

    def _get_from_csv(self):
        student_scores={}
        df=pd.read_csv(self.filename)
        for _,row in df.iterrows():
            student_scores[row["name"]]=row["score"]

        return student_scores





