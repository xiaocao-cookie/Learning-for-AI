# Docker

***Docker 是什么 ？ :* **

**A platform for building running and shipping applications**

**Docker是一个软件，和Linux是无关的，不是Linux的一部分**

**Docker是一个软件，主要负责容器化。**

**容器化：一个非常迷你的linux作为基础系统，在其上安装我们所需要的软件。**



**解决了什么问题：	这个应用在我的电脑能运行，那么在别人的电脑也能运行 **

**为什么这个应用（APP）在只在我的电脑能运行? **

​		**1、可能存在应用所需文件丢失**

​		**2、软件版本不匹配（比如一个应用是MySQL的版本是8.4 ，一个应用MySQL的版本是5.6）**

​		**3、不同电脑的环境变量配置不一样**

如果应用需要特定版本的python和mysql，docker可以把应用需要的特定版本的python和mysql打包，然后就能在其他有docker电脑上跑这个应用了

More: 如果你想跑/改写一个正在开发的应用，你可能一开始要花大量时间下载应用的编程语言，依赖的各种包，调机器的环境变量等等；

<img src="E:\Google下载文件\docker改良后的应用程序配置.png" alt="docker改良后的应用程序配置" style="zoom: 50%;" />

## Ubuntu安装docker步骤 

**先把docker上架到本地虚拟机的应用商店上，之后再从本地安装**

1、Set up Docker's `apt` repository.

```bash
#Add Docker's official GPG key:
sudo apt-get update                                   #更新应用商店
sudo apt-get install ca-certificates curl			  #安装curl，之后可以使用curl
sudo install -m 0755 -d /etc/apt/keyrings			  #安装keyrings文件,应该是没有输出
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc  #使用curl，应该是没有输出
sudo chmod a+r /etc/apt/keyrings/docker.asc			  #修改docker.asc的权限，应该是没有输出
```

```bash
#Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null         #输出重定向到dev/null，应该是没有输出

sudo apt-get update								        #应用商店更新
```

[附]：执行

```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
```

​		出现这个错误：curl: (35) OpenSSL SSL_connect: 连接被对方重置 in connection to download.docker.com:443

​		使用下面这两行

```bash
#nslookup命令是一个用于查询域名系统（DNS）记录的命令行工具。它可以帮助用户获取关于特定域名或IP地址的详细信息，包括其对应的IP地址、邮件交换服务器等
nslookup download.docker.com

ping download.docker.com
```

2、Install the Docker packages.

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



3、Verify that the installation is successful by running the `hello-world` image:

```bash
#要验证docker是否安装成功，可以用下面两种方式
#第一种： 这个步骤需要外网环境，需vpn
sudo docker run hello-world					#run运行这个hello world,如果没有则下载，如果有直接运行

#第二种
sudo docker --version
```



## 一、镜像

### 1、获取镜像

```bash
#从dockerhub获取镜像
sudo docker pull 镜像名:版本号
sudo docker pull ubuntu							#默认下载latest版本的Ubuntu		
sudo docker pull ubuntu:24.04					#下载24.04版本的Ubuntu


#使用镜像生成容器
sudo docker run -it --rm 镜像名:版本号 bash
#-it 开启一个交互式的终端
#--rm 容器退出时删除该容器
#bash  可以不写，默认bash；如果写了则确定运行bash
```

### 2、查看镜像

```bash
#查看电脑上下载了那些镜像
sudo docker image ls
sudo docker images -a -q
#-a: 查看所有镜像（默认参数 -a）
#-q: 显示镜像的ID

sudo docker search 镜像名 						#用于在 Docker Hub上搜索相关镜像
sudo docker info							  #查看docker的详细信息（版本号，镜像数，容器数等信息）
sudo docker image inspect 镜像ID/镜像名		   #查看某个镜像的详细信息（版本号，创建时间等）
sudo docker inspect 镜像ID/镜像名			   #查看某个镜像的详细信息（版本号，创建时间等）

```

### 3、删除镜像

```bash
sudo docker rmi -f 镜像ID					#删除镜像，如果镜像里有正在运行的容器，则需删除容器再删除镜像
#-f 强制删除

docker images -aq						#查看所有镜像ID

#反引号是 命令替换（Command Substitution） 的语法，
#它的作用是：先执行反引号中的命令，然后把它的输出结果当作参数传给外层命令。
#$()与反引号作用等价
echo `docker images -aq`				#反引号可以将docker images -aq执行的结果输出成一行
echo $(docker images -aq)	


sudo docker rmi `docker images -aq`		#批量删除镜像
#使用这个命令的风险：
#1. 导致容器无法启动
#2. 重建/重新拉取镜像耗时 （dockerhub）
#3. 可能不可逆 

```



### 4、镜像管理

```bash
sudo docker commit

#导出镜像
#这里test.tar只是一个tar文件的示例
sudo docker image save 镜像名:版本号 > 目录/test.tar

#导入镜像
sudo docker image load -i 目录/test.tar
#-i(input的缩写)，从指定的文件导入

```



## 二、容器

镜像通过docker run命令可以产生容器。
容器可以被理解为是一个正在运行的linux系统。
容器就可以被理解为：用镜像装好的一个系统。
对容器如何进行破坏，都不会影响原始镜像。

### 1、运行一个容器

sudo docker run 参数1 参数2... 镜像名:版本 容器启动后要执行的命令

如果容器内，什么事也没做，容器也会挂掉  ->   容器内必须有一个进程在容器的前台运行

```bash
#错误写法
sudo docker run ubuntu:24.04				#运行一个会挂掉的容器
#这个写法会产生多个独立的容器记录，因为容器内没有程序再跑
#每次调用docker run都会在主机上分配新的计算资源（CPU、内存等），如果频繁地创建新容器，则可能导致系统资源耗尽


sudo docker run -it --rm 镜像名 要执行的程序命令
#[注意]：‼️ 当我们运行一个容器的时候(sudo docker run )，如果对应的镜像不存在，会先帮我们自动下载镜像。
#-it参数：我们和这个容器要以交互的方式进行沟通，后面的bash可以不写，默认进行命令行程序
#--rm参数：容器一关闭立刻被自动删除

sudo docker run -it --rm ubuntu:24.04 bash				#以交互式的方式进入Ubuntu24.04的命令行


sudo docker run -dit --name 别名 镜像名 要执行的程序命令
#-dit 等同于-d -it
#-dit : 非常适合那些既需要长期稳定运作又可能偶尔需要用到手工干预的服务类应用部署场景
#-d   （detach）分离模式：后台运行一个容器命令
#--name   起别名

sudo docker run -dit --name pingBaidu ubuntu:24.04 ping baidu.com		
#让Ubuntu24.04运行ping百度，并在后台进行，这个容器起名为pingBaidu

sudo docker start 容器ID							#启动一个停止的容器
```

### 2、查看/进入容器

```bash
sudo docker container ls				#查看当前运行的容器
sudo docker ps -a						#查看所有容器
sudo docker logs 容器ID/容器名			 #查看容器日志
sudo docker logs -f 容器ID/容器名		 #刷新容器日志

#进入正在运行的容器空间，进行交互性操作
sudo docker exec -it 容器id bash
sudo docker attach 容器id

#查看容器的详细信息，返回JSON数组，里面保存了容器的版本号，创建时间等日期
sudo docker container inspect 容器ID
sudo docker inspect 容器ID


```

### 3、删除docker容器

```bash
sudo docker stop 容器id			#停止正在运行的容器

sudo docker rm -f 容器id			#删除某个容器，删除前必须先停止该容器运行
#-f 强制删除

sudo docker ps -aq  			#输出所有容器ID


#反引号是 命令替换（Command Substitution） 的语法，
#它的作用是：先执行反引号中的命令，然后把它的输出结果当作参数传给外层命令。
#$()与反引号作用等价
sudo docker rm `sudo docker ps -aq`					#反引号可以把sudo docker ps -aq的结果变成一行
sudo docker rm $(sudo docker ps -aq)
```

### 4、容器的端口映射

```bash
sudo docker run -d --name 容器名 -p 主机端口:镜像内的端口 镜像名
#-d :后台运行
#--name :给容器起名
#-p: 端口映射

sudo docker run -d --name my_nginx -p 85:80 nginx
#后台运行nginx,把nginx的80端口映射到85端口，之后可以通过85端口访问nginx，访问方式为localhost:85 或者 公网IP:85

浏览器 --> localhost:85  --> Docker映射 --> 容器内端口 nginx:80


sudo docker run -d --name 容器名 -P 镜像名
#-P: 大写P， 随机映射端口

sudo docker run -d --name my_nginx -P nginx 	#随机端口映射

sudo docker port 容器ID						#查看某个具体容器的端口映射情况

netstat -tunlp								 #查看主机占用的端口
```

### 5、容器提交

```bash
sudo docker commit 容器ID 新的镜像名		#容器提交
#可以在容器里面安装一些东西，比如nginx，alpine等，提交到本地镜像，之后如果再用此镜像运行容器，容器里就会有相应的nginx，alpine等程序了


```

### 6、数据卷共享 -- 目录映射

```bash
#数据卷共享，本地的文件和容器内的文件映射，也就是更新容器内文件内容，主机内文件内容也随之更新；反之，主机内文件内容更新，容器内文件内容也会更新，即使容器关闭或者被删除，被共享的数据卷还是保存在了本地主机中
#容器内的数据不重要，本质是一个base image + 其他可运行的程序  -> 容器运行后的销毁很自然，只要数据保留在主机上，就可以接着通过数据卷共享去创建镜像
sudo docker run -it -v 本地文件夹路径:容器内的文件夹路径 镜像名 要执行的命令
#-it 交互式运行
#-v 数据卷共享，前提是本地文件夹路径是存在的，容器内的文件夹路径可以不存在，如果没有则自动创建

sudo docker run -it -v /usr/test:/data ubuntu bash
#-v 数据卷共享,前提是本机/usr/test有这个目录，共享本机/usr/test文件和镜像Ubuntu产生的容器里面的/data文件
# 交互式运行，并进入容器的命令行
```

![](G:\01资料\Pictures\目录映射.png)





总结：
镜像：  操作系统（和主机操作系统匹配）， 工程里的东西  环境变量
容器：  隔绝的环境，可以被停止，可以被重启；可以被看成运行的程序（进程）；  每一个容器都有自己的文件系统



## 三、Dockerfile: 构建属于自己的镜像

**Dockerfile 用于构建docker镜像，部署一个容器环境，这个环境可以自定义**

**Dockerfile相当于一个脚本，通过Dockerfile运行自己的指令，来构建软件依赖，文件依赖，存储等等**



**镜像是多层存储，每一层在前一层的基础上进行修改**

**容器也是多层存储，以镜像为基础层，在其基础上加一层作为容器运行时的存储层**

**Dockerfile：基于基础镜像，一次添加层，最终生成一个新的镜像**

![](G:\01资料\Pictures\镜像和容器.png)





### 1、Dockerfile指令

```dockerfile
FROM 基础镜像（Base Image）

MAINTAINER 维护者信息 （可以没有）

WORKDIR 路径						#设置容器内的工作目录，类似于cd；

#COPY和ADD的作用是一样的，都是拷贝主机的文件到容器内
#但是COPY仅复制，ADD不仅会复制文件还会自动解压该文件
ADD 宿主机本地文件 镜像/容器内的文件
COPY 宿主机本地文件 镜像/容器内的文件


VOLUME 容器目录					  #声明挂载点，即要和主机共享的目录

EXPOSE 端口号                   #指定对外端口，在容器内暴露一个端口

ENV 环境变量					
#环境变量就像给程序贴上标签或配置说明，告诉程序在“什么环境”下运行；容器运行期间，这个变量始终有效

RUN 指令名称					#在构建镜像时执行,例如RUN apt update
CMD ["指令名称"]				#容器启动后要干的事
ENTRYPOINT 
#CMD的结果可能会被docker run覆盖掉，所以我们在使用date命令时可能看不到结果，而ENTRYPOINT执行的结果一定不会被覆盖

```



#### ① **COPY/ADD**

```dockerfile
#两者统一格式
ADD/COPY 宿主机本地文件 镜像/容器内的文件

#COPY指令：从宿主机复制文件/目录到新的一层镜像内
#可以保留源文件的元数据，如权限，访问修改时间等
#也可以通过模式匹配的方式对文件进行复制
COPY /demo/demo.txt /home/demo

COPY /demo/de*.txt /home/tes?.txt		#这里的*可匹配任意长度字符串，?只可匹配一个字符


#ADD的特性和COPY的三条特性基本一致，不过增加了一些功能
#ADD的源文件可以是一个URL，他会自动下载这个链接里的东西到指定目录
ADD http://www.baidu.com /app

#源文件也可以是一个tar压缩文件，它会自动解压缩该文件到指定目录
ADD *.tar /app
```

**Dockerfile官方更推荐使用COPY；ADD要用到复杂的功能时使用**



#### ②WORKDIR

```dockerfile
WORKDIR 路径						#设置容器内的工作目录，类似于cd；

#等价于在容器内执行 mkdir app && cd /app,后续所有指令（如COPY、RUN、CMD）的相对路径都以/app为基础
#如果容器内不存在该目录，会自动创建目录
WORKDIR /app
```



#### ③VOLUME

```dockerfile
VOLUME 容器目录						#声明容器和宿主机之间的共享目录（不负责挂载， docker run 时再挂载）

VOLUME ["/data"]
#表明/data是一个持久化的数据目录

#挂载方式有两种，1、-v参数 2、自动挂载
#1、-v 参数 指定了宿主机路径
docker run -v ./local/data:/data my_image	#把my_image的/data目录和主机的/local/data目录共享，也就是挂载

#2、自动挂载
docker run -it my_image			
#在运行my_image时没有指定-v参数，则docker会随机挂载到主机的某个目录下，通常是/var/lib/docker/volumes 下


```



**最后可以通过docker inspect 容器ID查看挂载情况**
**docker inspect返回的是一个JSON数组，其中Mounts参数记录了挂载的详细信息**
**以下是截取的docker inspect的结果**

```json
//运行容器时使用 -v 参数指定了宿主机路径
sudo docker run -v ~/demo:/demo alpine ash

     "Mounts": [
            {
                "Type": "bind",
                "Source": "/root/demo",
                "Destination": "/demo",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],

----------------------------------------------------------------------------------------------

//运行容器时没有使用 -v 参数指定
Dockerfile里面加VOLUME ["/data"]

        "Mounts": [
            {
                "Type": "volume",
                "Name": "7c6248bf9dc266365c345cdd8e11399b448604b5d14a64d66299c06b5b5f8424",
                "Source": "/var/lib/docker/volumes/7c6248bf9dc266365c345cdd8e11399b448604b5d14a64d66299c06b5b5f8424/_data",
                "Destination": "/data",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],
```





#### ④CMD

```dockerfile
#CMD 在容器内运行某个指令，启动程序，也代表该镜像在运行容器实例的时候，执行的具体参数
#容器不是虚拟机，对于容器的宿主机而言，容器是一个进程，既然是进程，那么容器在启动的时候需要指定些运行参数，这就是CMD指令的作用
#有的镜像会默认启动bash，比如Ubuntu镜像默认的CMD就是/bin/bash，所以在跑Ubuntu镜像的时候，可以不指定容器执行的命令
#即：sudo docker run -it ubuntu bash里面最后的bash可以省略

CMD ["参数1", "参数2"]
CMD ["cat", "/etc/lsb-release"]   #相当于在容器内执行cat /etc/lsb-release 文件中存储的是本机操作系统的信息

CMD ["/bin/bash"]                  #与docker run -it ubuntu /bin/bash等价，前提是此Dockerfile里有FROM ubuntu


```



#### ⑤RUN、CMD和ENTRYPOINT区别

```dockerfile
RUN 指令名称					#在构建镜像时执行,例如RUN apt update

CMD ["指令名称"]				#容器启动后要干的事

ENTRYPOINT ["指令名称"]
#CMD的结果可能会被docker run覆盖掉，所以我们在使用date命令时可能看不到结果，而ENTRYPOINT执行的结果一定不会被覆盖
#不仅如此，CMD还会成为ENTRYPOINT的参数


下面来说明这个 CMD 会成为 ENTRYPOINT 参数的机制：
----------------------------------------------------------------------------------------
sudo docker run -it --rm my_image:1.0 bash -> 程序会执行 date bash -> 报错 date: invalid date 'bash'

#my_image:1.0的Dockerfile如下
FROM Ubuntu:24.04
ENTRYPOINT ["date"]
#docker run [options] 镜像名 [命令]中的最后一个[命令]相当于Dockerfile的CMD ["命令"]
#例如
sudo docker run -it --rm my_image:1.0 bash -> 程序会执行 date bash -> 报错 date: invalid date 'bash'
#里面的bash就相当于 Dockerfile 里面的 CMD ["bash"]
#也就是说 Dockerfile里相当于以下三行
FROM Ubuntu:24.04
CMD ["bash"]
ENTRYPOINT ["date"]
#上面两行等价于 CMD ["date", "bash"]，这是由于Dockerfile中CMD会成为ENTRYPOINT的参数
#这样程序就会执行 date bash ，之后报错：bash为无效的date参数

--------------------------------------------------------------------------------------------

```



### 2、镜像构建

```bash
sudo docker build -t 镜像名 路径		#构建一个镜像
#-t 为构建的镜像起个名
#路径: 表示在哪个路径搜寻Dockerfile

sudo docker build -t my_image /usr/test
```



### 3、自定义镜像push到dockerhub

```bash
#自定义的镜像要推送到dockerhub网站，要把镜像的名字改成 账户名/镜像名
#更改镜像名  ---> tag
sudo docker tag 镜像ID /账户名/新的镜像名
#更改镜像名之后镜像ID不变，又多了一个镜像

#先登录到dockerhub,需要外网，执行这条命令后按提示输入密码即可
sudo docker login -u 用户名

#push到dockerhub，需要访问外网
sudo docker push 账户名/新的镜像名
```





## 四、容器网络、多容器运行

**容器和主机之间、容器和容器之间默认不会进行网络互通，接下来看看怎么让它们进行网络互联？**

### 1、容器和主机进行网络互联

**我们通常不会让他们真的连接，而是利用一个端口打通两个计算机，即通过 【-p参数： 端口映射】进行互联**

```bash
-p 主机端口:容器端口								#端口映射，将主机端口和容器端口互联
#端口映射后可以访问主机的IP地址:主机端口 --> 就可以访问容器内的运行程序

sudo docker run -d -p 81:80 nginx			#指定端口映射(小写p)
#把主机的81端口和nginx的80端口连在一起，这样在本机的浏览器上访问localhost:85 就可以访问到容器内的nginx

sudo docker run -d --name 容器名 -P 镜像名					#随机端口映射(大写P)
```



### 2、容器和容器之间进行互联

#### ① docker中的网络情况

**查看本机中docker 的网络情况（可以将其假想成网卡）**

**电脑有三个网线插口**

**（1）桥接网络： 插完网线后能连上互联网**

**（2）主机网络： -p 主机端口：容器端口**

**（3） 不上网（有的时候需要隔绝容器和互联网）**

```bash
sudo docker network ls				#查看本机docker中的网络情况
结果如下：
NETWORK ID          NAME                DRIVER              SCOPE
17e324f45964        bridge              bridge               local   桥接网络，容器之间如果需要互联使用这种网络
6ed54d316334        host                host                 local   主机网络，容器和主机之间，类似于-p
7092879f2cc8        none                null                 local   容器不联网

```



**如果我们直接运行容器，这些容器默认都挂在bridge网络上。**

**挂在这个网络上容器的特点是：可以连通互联网 ping baidu.com，容器之间可以通过IP地址互相访问**

**但是不能通过ping 容器名字进行访问 --> ping 容器名字 -->  失败**

```bash
sudo docker network inspect bridge
#查看bridge这个网络上有几个容器，和他们的网络信息 --> 这个信息在返回的JSON文件中的Containers字段

#容器内查看IP地址
进入容器内 --> ip addr --> 会显示本容器的IP信息


sudo docker run -it --rm alpine ash								#运行并进入容器alpine，默认挂在bridge网络上
进入容器alpine内 --> ping baidu.com --> 可以ping通
#这个说明了挂在bridge网络上容器的特点是：可以连通互联网


#以下是实验过程
#alpine1 alpine2默认在docker的bridge网络上运行
sudo docker run -it --name alpine1 alpine ash			#alpine1的IP地址为172.10.0.3
sudo docker run -it --name alpine2 alpine ash			#alpine2的IP地址为172.10.0.4
进入容器alpine1内 -->
	 ping baidu.com --> 成功√
	 ping 172.10.0.4 --> 成功√
	 ping alpine2 --> 失败×
	 
进入容器alpine2内 -->
	 ping baidu.com --> 成功√
	 ping 172.10.0.3 --> 成功√
	 ping alpine1 --> 失败×
#这个实验说明了容器之间可以通过IP地址互相访问，但是不能通过--name名字进行访问
```



#### ②自定义桥接网络

*引言：上述运行起来的容器有一个局限，就是容器之间访问不能使用名字进行访问，这就导致了要记IP地址，而且IP地址会变，非常的不方便，相反，容器的名字一般是固定的，所以可以通过自定义的桥接网络，使得容器之间可以用名字进行访问*



**自己建立bridge网络的好处是：容器可以访问互联网，可以通过IP互联，也可以通过名字来进行访问**

```bash
sudo docker network create --driver bridge 网络名		#自定义桥接网络
sudo docker network inspect 网络名					    #查看自定义的网络下有几个运行的容器

#以下是实验过程
sudo docker network create --driver bridge alpine-net		#建立一个名叫alpine-net的网络
sudo docker network ls 										#查看当前网络，此时就是4个网络了（原先的3个+自定义的1个）

#通过自定义的桥接网络来运行两个容器
#--network 网络名： 将容器挂载到我们自己建立的网络上
sudo docker run -it --name alpine1 --network alpine-net alpine ash		#alpine1的IP地址为172.10.0.3
sudo docker run -it --name alpine2 --network alpine-net alpine ash		#alpine2的IP地址为172.10.0.4
进入容器alpine1内 -->
	ping baidu.com --> 成功√
	ping 172.10.0.4 --> 成功√
	ping alpine2 -->  成功 --- √√√

进入容器alpine2内 -->
	ping baidu.com --> 成功√
	ping 172.10.0.3 --> 成功√
	ping alpine1 --> 成功 --- √√√
#这个实验说明了：挂载到自己建立的网络上的容器之间，互相可以ping通
```



### 3、多容器运行



```bash
sudo docker compose up -d
#同时启动多个容器，并将它们互联（创建了一个bridge网络）, -d 后台运行
#所有启动的容器都是基于创建的桥接模式网络运行 --> 容器之间可以通过名字请求到对方

sudo docker compose down  		#停掉多个容器

```

**sudo docker compose up --> 在执行这个命令的目录下，有一个文件（格式为YAML），这个文件在描述多个容器怎么组织，每个容器的具体信息是什么样的，比如此容器基于的镜像，端口等等信息。**



**下面是多容器运行的实验：**

**a. 先拉两个有用的镜像**

```bash
#python环境（运行python的代码）
#在线的 代码编辑 + 运行的环境 专用于做数据分析，科学计算，机器学习/深度学习
sudo docker pull jupyter/scipy-notebook:latest

sudo docker pull python:3.9-slim			#迷你的python
```



**b.  准备一个目录结构**

***cd ~ && mkdir test && cd test && mkdir workspace***

**在~/test里面创建并编辑一个YAML文件：nano  docker-compose.yml ， 这个文件名必须叫docker-compose.yml**

```yaml
services: 						#容器/服务
  jupyter:
    image: jupyter/scipy-notebook:latest  # Jupyter Notebook
    container_name: jupyter_notebook			#容器名，可自己指定
    ports:
      - "8888:8888"								#端口映射 相当于-p 8888:8888 jupyter/scipy-notebook:latest
    volumes:
      - ./workspace:/home/jovyan/work  			#共享目录,卷挂载
    environment:
      - JUPYTER_ENABLE_LAB=yes
    command: start-notebook.sh --NotebookApp.token=''

  api:
    image: python:3.9-slim  					# 轻量级 Python
    container_name: fastapi_server				#容器名，可自己指定
    ports:
      - "8000:8000"								#端口映射 相当于-p 8000:8000 python:3.9-slim
    volumes:
      - ./workspace:/app  						# 共享目录，FastAPI 可以访问 Jupyter 代码
    working_dir: /app
    command: >
      sh -c "pip install -i https://pypi.tuna.tsinghua.edu.cn/simple fastapi uvicorn && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

```



**c. 在workspace下建立文件main.py**

**workspace：也就是两个容器的共享目录**

```python
# 在 workspace/main.py 里写入以下代码
from fastapi import FastAPI

app = FastAPI()

@app.get("/")						#请求路径 
def home():
    return {"message": "FastAPI is running!"}

@app.get("/predict/{x}")			#请求路径 
def predict(x: float):
    return {"input": x, "prediction": x * 2} 
    

```



**d. 在 ~/test 目录下运行sudo docker compose up  构建多个容器**

​        ***这里要说明一点的是，此前步骤中没有创建网络的语句，也就是sudo docker network create ,但在查看网络的时候会多出一个网络，也就是说在sudo docker compose up时，自动构建了一个bridge网络，从而使 ~/test 目录下的容器能互联***

**测试<u>http:// 公网IP:端口号</u> 或者 <u>http:// localhost: 端口号</u>**

以下假设本机公网IP为172.10.0.123

*浏览器输入 -->  http://localhost:8000 或  http://172.10.0.123:8000 --> 页面显示 {"message": "FastAPI is running!"}*

*浏览器输入 --> http://localhost:8000/predict/2 或 http://172.10.0.123:8000/predict/2 --> 页面显示 {"input": 2.0, "prediction": 4.0}*

*浏览器输入 --> http://localhost:8888 或 http://172.10.0.123:8888 --> 页面会显示jupyter notebook的主页* 



**e.  jupyter notebook 可以和 python的fast-api服务器做网络通信**

***（1）jupyter notebook  --> terminal --> ping api -->ping通  此处的api为步骤 b 中YAML文件中的api服务***



***（2）jupyter notebooke --> File --> 新建一个 jupyter notebook --> 在格子里输入如下python代码***

```python
import requests

# FastAPI 的服务地址（使用容器名 "api"）
base_url = "http://api:8000"

# 调用根路径
#相当于在浏览器里请求 http://api:8000/
r1 = requests.get(f"{base_url}/")
print("GET /:", r1.json())

# 调用 /predict 接口
#相当于在浏览器里请求 http://api:8000/predict/10
x = 10
r2 = requests.get(f"{base_url}/predict/{x}")
print(f"GET /predict/{x}:", r2.json())
```

***shift + enter 运行此代码  结果如下***

```css
GET /: {'message': 'FastAPI is running!'}
GET /predict/10: {'input': 10.0, 'prediction': 20.0}
```



**f . 回到 ~/test 目录下输入sudo docker compose down 结束容器并删除，此时基于compose构建的网络也被删除掉了**









