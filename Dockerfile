# set python image
FROM python:3.6-stretch

# install build utilities
RUN apt-get update && \
	apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# check python environment
RUN python3 --version
RUN pip3 --version

# set working directory in the container
WORKDIR /salary_predictor

# Copy all files to working directory
COPY . .

# install dependencies in the container
RUN pip install -r requirements.txt

# run app
CMD ["python3", "run.py"]
