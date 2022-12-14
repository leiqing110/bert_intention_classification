#FROM ubuntu:latest
FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel
ENV LANG=C.UTF-8
#RUN sed -i "s#archive.ubuntu.com#mirrors.aliyun.com#g" /etc/apt/sources.list \
#   && sed -i "s#security.ubuntu.com#mirrors.aliyun.com#g" /etc/apt/sources.list
RUN sed -i "s#archive.ubuntu.com#mirrors.tuna.tsinghua.edu.cn#g" /etc/apt/sources.list \
   && sed -i "s#security.ubuntu.com#mirrors.tuna.tsinghua.edu.cn#g" /etc/apt/sources.list

RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-key del 7fa2af80
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub

RUN apt-get autoclean
RUN apt-get update
#RUN apt-get dist-upgrade

RUN apt-get install vim -y \
&& apt-get install lrzsz -y 

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
&& pip install tensorboard==2.2.0 \
&& pip install scikit-learn==1.0
#&& pip install torch==1.6.0 


# RUN mkdir /opt/log \
#    && ln -s /workspace/logs/ /opt/log


# COPY  ./ /workspace/
# WORKDIR /workspace/

# EXPOSE 8999 
#ENTRYPOINT ["/bin/bash"]

