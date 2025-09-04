## catia-plugin

**Author:** tecwin
**Version:** 0.0.1
**Type:** tool

### Description
修改dify docker目录中的.env文件：
FORCE_VERIFYING_SIGNATURE=false
PIP_MIRROR_URL=https://pypi.tuna.tsinghua.edu.cn/simple
重启dify:
docker compose up -d

### 可选
需要更改docker的pip镜像源
linux:
vi /etc/docker/daemon.json
{
    "registry-mirrors": [
        "https://docker.1ms.run",
        "https://docker.xuanyuan.me",
        "https://docker.rainbond.cc",
        "https://do.nark.eu.org",
        "https://dc.j8.work",
        "https://9cpn8tt6.mirror.aliyuncs.com",
        "https://registry.docker-cn.com",
        "https://mirror.ccs.tencentyun.com",
        "https://docker.1panel.live",
        "https://2a6bf1988cb6428c877f723ec7530dbc.mirror.swr.myhuaweicloud.com",
        "https://docker.m.daocloud.io",
        "https://hub-mirror.c.163.com",
        "https://mirror.baidubce.com",
        "https://your_preferred_mirror",
        "https://dockerhub.icu",
        "https://docker.registry.cyou",
        "https://docker-cf.registry.cyou",
        "https://dockercf.jsdelivr.fyi",
        "https://docker.jsdelivr.fyi",
        "https://dockertest.jsdelivr.fyi",
        "https://mirror.aliyuncs.com",
        "https://dockerproxy.com",
        "https://mirror.baidubce.com",
        "https://docker.m.daocloud.io",
        "https://docker.nju.edu.cn",
        "https://docker.mirrors.sjtug.sjtu.edu.cn",
        "https://docker.mirrors.ustc.edu.cn",
        "https://mirror.iscas.ac.cn",
        "https://docker.rainbond.cc"
    ]
}
sudo systemctl restart docker

