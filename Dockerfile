FROM centos:centos7

# build a container with lmod for singularity-hpc
# docker build -t singularity-hpc .

LABEL MAINTAINER @vsoch
ENV LMOD_VER 8.4.3

RUN yum -y install git tar which bzip2 xz \
            epel-release make automake gcc gcc-c++ patch \
            python-keyring zlib-devel openssl-devel unzip iproute \
            python3 python3-dev wget tcl-devel
RUN rpm -ivh https://kojipkgs.fedoraproject.org//packages/http-parser/2.7.1/3.el7/x86_64/http-parser-2.7.1-3.el7.x86_64.rpm
RUN mkdir -p /build
WORKDIR /build
RUN curl -LO http://github.com/TACC/Lmod/archive/${LMOD_VER}.tar.gz
RUN mv /build/${LMOD_VER}.tar.gz /build/Lmod-${LMOD_VER}.tar.gz
RUN tar xvf Lmod-${LMOD_VER}.tar.gz

WORKDIR /build/Lmod-${LMOD_VER}

RUN yum -y install lua lua-devel lua-posix lua-filesystem tcl iproute

RUN ./configure --prefix=/usr/local
RUN make install
RUN ln -s /usr/local/lmod/lmod/init/profile /etc/profile.d/modules.sh
RUN ln -s /usr/local/lmod/lmod/init/cshrc /etc/profile.d/modules.csh

ENV PATH /opt/conda/bin:${PATH}
ENV LANG C.UTF-8
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-latest-Linux-x86_64.sh

# install singularity
RUN yum update -y && \
    yum install -y epel-release && \
    yum update -y && \
    yum install -y singularity

RUN pip install ipython
WORKDIR /code
COPY . /code
RUN pip install -e .[all]

# If we don't run shpc through bash entrypoint, module commands not found
ENTRYPOINT ["/code/entrypoint.sh"]
