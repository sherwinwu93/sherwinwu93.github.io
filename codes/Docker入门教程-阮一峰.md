# Docker入门教程
# 一`环境配置的难题
# 二`虚拟机
虚拟机的缺点:
1. 资源占用多
2. 冗余步骤多
3. 启动慢
# 三`Linux容器
Linux容器不模拟完整的操作系统,对进程进行隔离.
优点:
1. 启动快
2. 资源占用少
3. 体积小
# 四`Docker是什么?
Docker属于Linux容器的封装,提供简单易用的容器使用接口
# 五`Docker的用途
1. 一次性环境
2. 弹性的云服务
3. 组件微服务架构
# 六`Docker的安装
# 六`image文件
Docker把应用及其依赖,打包在image文件里面.
image是类,docker生成实例.同一个image,多个实例.

命令:
# 列出images
docker image ls
# 删除image
docker image rm [imageName]
# 七`实例:hello world
# 设置镜像
修改 /etc/default/docker
DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
# docker image pull library/hello-world
docker image pull hello-world 
docker image ls
# 运行
docker container run hello-world
# docker run ubuntu
docker container run -it ubuntu bash
# 杀程序
docker container kill [containID]
# 八`容器文件
iamge的容器实例,也是文件.
# 列出容器
docker container ls

# 列出本机所有容器
docker container ls --all

# 删除容器文件
docker container rm [containerID]
# 九`Dockerfile文件
# apk加速
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
# 十`实例:制作自己的Docker容器
待续...
# 十一`其他有用的命令
# 重复使用容器
docker containter start [containerID]

# 终止容器运行
docker container kill/ stop

# 容器输出日志
docker container logs

# 进入容器
docker container exec -it [containerID] /bin/bash

# 拷贝容器
docker container cp [containID]:[/path/to/file] .




