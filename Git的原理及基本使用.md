# Git的原理及基本使用

## 一、Git的原理

#### 1、Git的概念

Git是一个开源的***分布式版本控制系统***，可以有效、高速地处理从很小到非常大的项目版本管理，也是[Linus Torvalds](https://baike.baidu.com/item/Linus Torvalds/9336769?fromModule=lemma_inlink)为了帮助管理Linux内核开发而开发的一个开放源码的版本控制软件，每个 Git 项目的根目录下有一个 .git 目录，它是 Git 默默进行版本控制时读写的“数据库”。有几个概念需要提一下：  

> (1)工作区：代码所在目录。

> (2)暂存区： .git/index 文件。

> (3)本地仓库： .git 目录。

#### 2、Git的分层结构

![](C:\Users\LENOVO\Desktop\GitHub第三次作业（不能删！）\图片1.png)

git的工作总共分四层，其中三层是在自己本地也就是前面说的git仓库，包括了工作目录，暂存区和本地仓库，工作目录就是我们执行命令git init时所在的地方，也就是我们执行一切文件操作的地方，暂存区和本地仓库都是在.git目录，因为它们只是用来存数据的。远程仓库在中心服务器，也就是我们做好工作之后推送到远程仓库，或者从远程仓库更新下来最新代码到我们的git仓库。git所存储的都是一系列的文件快照，然后git来跟踪这些文件快照，发现哪个文件快照有变化它就会提示你需要添加到暂存区或是提交到本地仓库来保证你的工作目录是干净的。  

#### 3、Git的对象

从根本上讲，git是一套内容寻址的文件系统，它存储的也是key-value键值对，是根据指针来寻址的，这些指针就存储在git的对象中。git一共有3种对象，**commit对象**，**tree对象**和**blob对象**。  

#### 4、git内部原理：[内部原理链接](http://www.open-open.com/lib/view/open1328070620202.html)


## 二、Git的基本使用

#### 1、Git的基本工作流程

###### （1）在工作目录中修改文件。

###### （2）暂存文件，将文件的快照放入暂存区域。

###### （3）提交更新，找到暂存区域的文件，将快照永久性存储到 Git 仓库目录。

#### 2、Git的基本使用

![](C:\Users\LENOVO\Desktop\GitHub第三次作业（不能删！）\v2-0072de93344d98ef70dbf0ba7505d073_720w.png)

***上面的四条命令在工作目录、暂存目录(也叫做索引)和仓库之间复制文件。***

> git add files：把当前文件放入暂存区域。

> git commit：给暂存区域生成快照并提交。

> git reset -- files：用来撤销最后一次git add files，你也可以用git reset 撤销所有暂存区域文件。

> git checkout -- files 把文件从暂存区域复制到工作目录，用来丢弃本地修改。

***你可以用 git reset -p, git checkout -p, or git add -p进入交互模式，也可以跳过暂存区域直接从仓库取出文件或者直接提交代码。***

![](C:\Users\LENOVO\Desktop\GitHub第三次作业（不能删！）\v2-5afb12c1af95c1e1ba243546fe78a9b8_720w.png))

> git commit -a 相当于运行 git add 把所有当前目录下的文件加入暂存区域再运行。git commit.

> git commit files 进行一次包含最后一次提交加上工作目录中文件快照的提交。并且文件被添加到暂存区域。

> git checkout HEAD -- files 回滚到复制最后一次提交。

#### 3、创建与合并分支

每次提交，Git都把它们串成一条时间线，这条时间线就是一个分支。截止到目前，只有一条时间线，在Git里，这个分支叫主分支，即master分支。HEAD严格来说不是指向提交，而是指向master，master才是指向提交的，所以，HEAD指向的就是当前分支。

> ***查看分支：git branch***

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210304155621185.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0MDk0Mjk2,size_16,color_FFFFFF,t_70)

> ***合并分支：git merge***

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210304160819821.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0MDk0Mjk2,size_16,color_FFFFFF,t_70)

**分支策略：** 首先master主分支应该是非常稳定的，也就是用来发布新版本，一般情况下不允许在上面干活，干活一般情况下在新建的dev分支上干活，干完后，比如上要发布，或者说dev分支代码稳定后可以合并到主分支master上来。

#### 4、小提示

######  (1)git config -global参数，有了这个参数，表示这台机器上所使用的git仓库都会使用这个配置。

######  (2)命令git checkout -- readme.txt中的--很重要，如果没有--的话，那么命令就变成了创建分支了。

