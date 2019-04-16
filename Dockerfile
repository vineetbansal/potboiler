FROM continuumio/miniconda3

EXPOSE 5000

RUN mkdir /app/ && mkdir /app/src && mkdir /app/tests

COPY environment.yml /app
COPY setup.py /app
COPY src /app/src/
COPY tests /app/tests/

WORKDIR /app

RUN ["conda", "env", "create", "-f", "environment.yml"]
RUN ["/bin/bash", "-c", "source activate potboiler && python setup.py install"]

RUN echo "source activate potboiler" > ~/.bashrc
ENV PATH /opt/conda/envs/potboiler/bin:$PATH

ENV FLASK_APP=potboiler.flask:create_app
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["source activate potboiler && exec python -m flask run --host=0.0.0.0"]
