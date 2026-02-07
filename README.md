# Python Learning Project

这是一个用于练习 Python 工程能力的学习项目，  
通过一个「学生成绩分析工具」逐步演进，练习：

- Python 基础工程结构
- 多种输入方式（CLI / 文件 / CSV）
- 函数拆分与职责划分
- 使用类封装变化点
- 使用 Git 进行阶段化管理

## 功能说明

当前工具支持以下输入方式：

1. 命令行交互输入学生成绩
2. 从文本文件读取成绩（name,score）
3. 从 CSV 文件读取成绩（使用 Pandas）

程序会输出：

- 学生人数
- 平均分
- 最高分 / 最低分

## 项目结构

```text
python-learning/
├─ src/
│  ├─ input_source.py
│  ├─ analyzer.py
│  └─ main.py
├─ data/
│  ├─ scores.txt
│  └─ scores.csv
