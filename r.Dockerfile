FROM r-base:4.3.3


COPY data /data
COPY *.R /
COPY *.rds /

RUN Rscript packages.R

ENTRYPOINT ["Rscript", "run.R"]
CMD ["predict", "/data/fake_data.csv"]