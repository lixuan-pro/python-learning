import os
from datetime import datetime

def save_report(content,out_dir="../reports"):
    os.makedirs(out_dir, exist_ok=True)
    timestamp=datetime.now().strftime("%Y%m%d-%H%M%S")
    filename=f"score_analysis_{timestamp}.txt"
    filepath=os.path.join(out_dir,filename)
    with open(filepath,"w",encoding="utf-8") as f:
        f.write(content)
    return filepath