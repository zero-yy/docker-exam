列举镜像
docker images

新建一个镜像
docker build -t hello .

单独运行，映射到外网端口4001
docker run -p 4001:80 hello

swarm集群初始化
docker swarm init

通过compose启动集群
docker stack deploy -c docker-compose.yml hellolab

查看集群状态
docker stack ps hellolab


其他：
docker service ls
docker service rm hellolab_web