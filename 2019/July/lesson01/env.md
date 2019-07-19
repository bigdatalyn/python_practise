SET VAGRANT_HTTP_PROXY=
SET VAGRANT_HTTPS_PROXY=

### 环境+git环境


### Git

echo "# python_practise" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/bigdatalyn/python_practise.git
git push -u origin master

push an existing repository from the command line

git remote add origin https://github.com/bigdatalyn/python_practise.git
git push -u origin master


# 第一次使用

git clone https://github.com/bigdatalyn/python_practise.git
cd 2019/lesson01/
mkdir July                            # 添加自已名称目录， 用拼音表示
echo "print("hello world")" >> July/day01.py
git add July/day01.py
git status     # 查看当前github作业提交状态
git commit -m "add July/day01.py"     # 提交代码到本地仓库
git pull			        # 防止冲突,每次push之前先pull
git push -u origin master               # 提交代码到远程仓库

# 后面写好作业后，只需要下面三行即可
git add .
git commit -m "modify July/day01.py"	# 引号内为本次提交的描述,请自行更改
git pull			        # 防止冲突,每次push之前先pull
git push 

# 错误

    因虚拟机yum源默认版本为git-1.7.1, 所以会导致报错**

    第一步:

    sudo yum -y remove git

    第二步:

    新建一个yum的repo文件并将一下内容复制进去

    vim /etc/yum.repo.d/wandisco-git.repo

    [WANdisco-git]
    name=WANdisco Distribution of git
    baseurl=http://opensource.wandisco.com/rhel/$releasever/git/$basearch
    enabled=1
    gpgcheck=1
    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-WANdisco

    第三步:

    sudo rpm --import http://opensource.wandisco.com/RPM-GPG-KEY-WANdisco

    第四步:

    yum -y install http://opensource.wandisco.com/centos/6/git/x86_64/git-2.2.1-1.WANdisco.232.x86_64.rpm

    第五步:

    yum update -y nss curl libcurl

    然后就可以使用git了

    注意: 如果你开了翻墙软件并且不是日本节点,请先关闭翻墙软件在进行安装.

# git 

·  git add -A  提交所有变化

·  git add -u  提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)

·  git add .  提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件

+++++++++++++++++++++++++++++++++++++++++++++++
git 设置和取消代理 
git config --global https.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
git config --global --unset http.proxy
git config --global --unset https.proxy
npm config delete proxy
+++++++++++++++++++++++++++++++++++++++++++++++
