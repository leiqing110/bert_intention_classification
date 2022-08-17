#FROM ubuntu:latest
FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel
ENV LANG=C.UTF-8
#RUN sed -i "s#archive.ubuntu.com#mirrors.aliyun.com#g" /etc/apt/sources.list \
#   && sed -i "s#security.ubuntu.com#mirrors.aliyun.com#g" /etc/apt/sources.list
RUN sed -i "s#archive.ubuntu.com#mirrors.tuna.tsinghua.edu.cn#g" /etc/apt/sources.list \
   && sed -i "s#security.ubuntu.com#mirrors.tuna.tsinghua.edu.cn#g" /etc/apt/sources.list

# RUN apt-get update --fix-missing

#RUN apt-get install curl -y \
#   && apt-get install python -y \
#   && apt-get install libglib2.0-0 -y \
#   && apt-get install libsm6 -y \
#   && apt-get install libxrender-dev -y \
#   && apt-get install libxext-dev -y\
#   && apt install libgl1-mesa-glx -y \
#   && apt-get install vim -y \
#   && apt-get install unzip -y \
#   && apt-get install lrzsz -y \
#   && apt-get install language-pack-zh-hans -y \
#   && apt-get install python-matplotlib -y \
#   && apt-get install python-pip python-dev build-essential -y

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
&& pip install tokenizers==0.10.2 \
&& pip install transformers==4.5.1 \
&& pip install pytorch-lightning==0.9.0 \
&& pip install torch==1.6.0 \
&& pip install tensorboard==2.2.0


# RUN mkdir /opt/log \
#    && ln -s /workspace/logs/ /opt/log


# COPY  ./ /workspace/
# WORKDIR /workspace/

# EXPOSE 8999 
ENTRYPOINT ["/bin/bash"]

