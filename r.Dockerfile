FROM rocker/r2u:22.04


RUN mkdir /app
WORKDIR /app

COPY *.R /app
COPY *.rds /app
COPY *.csv /app

RUN Rscript packages.R

ENTRYPOINT ["Rscript", "run.R"]
