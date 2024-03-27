FROM r-base:4.3.3

RUN mkdir /app
WORKDIR /app

COPY *.R /app
COPY *.rds /app

RUN Rscript packages.R

ENTRYPOINT ["Rscript", "run.R"]