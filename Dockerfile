FROM python:latest
RUN apt update && pip install dohq-artifactory
WORKDIR /opt/myscript
COPY ./3_pythonscript.sh .
ENTRYPOINT [ "python", "./pythonscript.py" ]
