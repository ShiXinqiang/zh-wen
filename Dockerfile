# 使用一个官方的、轻量级的 Python 3.9 版本作为基础
FROM python:3.9-slim

# 在容器（虚拟服务器）内部创建一个叫做 /app 的工作目录
WORKDIR /app

# 将你的依赖文件复制到工作目录中
COPY requirements.txt .

# 运行 pip 命令来安装这些依赖
RUN pip install --no-cache-dir -r requirements.txt

# 将你所有的代码（main.py等）都复制到工作目录中
COPY . .

# 设置一个环境变量，让Python的输出更直接，方便查看日志
ENV PYTHONUNBUFFERED=1

# 【重要】最后，设置当容器启动时要执行的命令
# 这会运行你的机器人脚本
CMD ["python", "main.py"]
