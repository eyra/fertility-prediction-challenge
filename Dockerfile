FROM continuumio/miniconda3:23.3.1-0

COPY environment.yml /
RUN conda env create -f /environment.yml

COPY data /data
COPY script.py /

ENTRYPOINT [ "conda", "run", "-n", "eyra-rank", "python", "/script.py" ]
CMD ["/data/test_data_liss_2_subjects.csv"]