FROM continuumio/anaconda3:2024.02-1

COPY environment.yml /
RUN conda env create -f /environment.yml

RUN mkdir /app
WORKDIR /app

COPY *.csv /app
COPY *.py /app
COPY *.joblib /app

ENTRYPOINT ["conda", "run", "-n", "eyra-rank", "python", "/app/run.py"]
CMD []