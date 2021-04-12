FROM continuumio/miniconda:latest

WORKDIR /home/docker_conda_ifcproj

COPY environment.yml ./
COPY server.py ./
COPY driver.py ./
COPY ifcJsonData.json ./
COPY ifcJsonData2.json ./
COPY simplified_out.json ./
COPY simplified_out2.json ./
COPY mods mods /
COPY static static/
COPY templates templates/

COPY boot.sh ./

RUN chmod +x boot.sh

RUN conda env create -f environment.yml

# RUN echo "source activate testenv" < ~/.bashrc
ENV PATH /opt/conda/envs/testenv2/bin:$PATH

EXPOSE 3200

ENTRYPOINT ["./boot.sh"]
