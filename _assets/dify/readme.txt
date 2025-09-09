修改dify docker目录中的.env文件：
FORCE_VERIFYING_SIGNATURE=false
PIP_MIRROR_URL=https://pypi.tuna.tsinghua.edu.cn/simple
重启dify:
docker compose up -d