FROM continuumio/anaconda3:2024.02-1

COPY environment.yml /
RUN conda env create -f /environment.yml

RUN mkdir /app

COPY data /data
COPY *.py /
COPY *.joblib /

ENTRYPOINT ["conda", "run", "-n", "eyra-rank", "python", "/run.py"]
CMD ["predict", "/data/fake_data.csv"]