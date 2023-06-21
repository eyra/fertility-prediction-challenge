FROM continuumio/anaconda3:2023.03-1

COPY environment.yml /
RUN conda env create -f /environment.yml

RUN mkdir /src

COPY data /data
COPY src/script.py /src
COPY models /models

ENTRYPOINT ["conda", "run", "-n", "eyra-rank", "python", "/src/script.py"]
CMD ["predict", "/data/fake_data.csv"]