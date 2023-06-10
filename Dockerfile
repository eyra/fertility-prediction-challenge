FROM continuumio/miniconda3:23.3.1-0

COPY environment.yml /
RUN conda env create -f /environment.yml

RUN mkdir /src

COPY data /data
COPY src/script.py /src

ENTRYPOINT ["conda", "run", "-n", "eyra-rank", "python", "/src/script.py"]
CMD ["predict", "/data/test_data_liss_2_subjects.csv"]