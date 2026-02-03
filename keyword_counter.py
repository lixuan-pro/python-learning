keyword="li"
count2=0
with open("test.txt","r",encoding="utf-8") as f:
    content=f.read()
    count1=content.count(keyword)
    print(f"单词{keyword}有{count1}个")
    for line in content.splitlines():
        line=line.strip()
        words=line.split()
        for word in words:
            if word==keyword:
                count2+=1

    print(f"单词{keyword}有{count2}个")
