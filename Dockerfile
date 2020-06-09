# 使用官方的Python运行时环境作为父镜像
FROM python:3

# 将工作目录设置为“/app”
WORKDIR /app

# 将当前目录内容复制到“/app”的容器中
ADD . /app

# 安装requirements.txt中指定的所有需要的软件包
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# 将端口80映射到外部世界
EXPOSE 80

# 定义环境变量
ENV NAME World

# 容器启动时运行app.py
CMD ["python", "app.py"]