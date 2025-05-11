* Docker Compose
# compose 简介
使用yml来管理所有服务
# Compose 安装
curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname-s)-$(uname -m)" -o /usr/local/bin/docker-compose

docker-compose --version
# 使用
## 1. 准备
## 2. 创建dockerfile文件
## 3. 创建docker-compose.yml
## 4. 使用Compose命令构建和运行应用
# 运行命令
docker-compose up
# 后台运行命令
docker-compose up -d

在docker-compose.yml下,直接执行
docker-compose up xx服务
up: 运行
down: 卸载所有
stop: 停止
rm: 删除停止的
-d: 后台运行
exec xx服务 bash:进入容器内部

docker-compose stop xx && docker-compose rm -f && docker-compose up xx

# jenkins docker脚本
cd /root/git-code/spmia/spmia-chapter5
cd eurekasvr
mvn clean package docker:build
cd ../docker/common
docker-compose stop eurekaserver && docker-compose rm -f
docker-compose up -d eurekaserver

# jenkins docker all脚本
cd /root/git-code/spmia/spmia-chapter6
mvn clean package docker:build
cd docker/common
docker-compose down
docker-compose up -d
