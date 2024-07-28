FROM jupyter/datascience-notebook

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./julia-packages.sh /tmp/julia-packages.sh
RUN /bin/bash /tmp/julia-packages.sh

