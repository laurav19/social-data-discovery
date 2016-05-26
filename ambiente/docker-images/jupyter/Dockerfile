# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM jupyter/pyspark-notebook

MAINTAINER SDD Project <radianstk@gmail.com>

USER root

# RSpark config
ENV R_LIBS_USER $SPARK_HOME/R/lib

# pre-requisites
RUN apt-get update && \
    apt-get install -y build-essential git curl libpq-dev gfortran libatlas-base-dev python-pip python-dev \
    fonts-dejavu \
    gcc && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD sdd-ingesta.sh /home/jovyan/work/sdd-ingesta.sh
RUN chmod 777 /home/jovyan/work/sdd-ingesta.sh


USER jovyan
ADD sdd-ingesta.py /home/jovyan/work/sdd-ingesta.py
ADD sdd-visualizacion.ipynb /home/jovyan/work/sdd-visualizacion.ipynb

#Ejecutamos comando para instion de datos
#CMD ["./sdd-ingesta.sh"]
