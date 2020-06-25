# set python image
FROM python:3.6-stretch

# install build utilities
RUN apt-get update && \
	apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# check python environment
RUN python3 --version
RUN pip3 --version

# set working directory in the container
WORKDIR /ml_app

# Copy all files to working directory
COPY . .

# install dependencies in the container
RUN pip install --no-cache-dir -r requirements.txt

# set useful env variables
ENV FLASK_APP "app.py"
ENV FLASK_DEBUG True
ENV FLASK_RUN_HOST 0.0.0.0

# run app
CMD ["flask", "run"]
