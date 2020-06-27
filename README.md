# Machine learning Flask API skeleton

Requirements
-

- `docker version 19.03.8`

- `docker-compose version 1.25.5`

Build and run the skeleton
-

1. Clone this repository
`git clone https://github.com/masteropen/machine-learning-flask-api-skeloton.git`

2. (Optional) Customize `.env` file and eventually the variable `WORKDIR` in `Dockerfile` to match your own project
directory name under the container.

3. Build and run container :
`docker-compose up --build`

4. (Optional) if you change `CONTAINER_FLASK_PORT` in `.env`, make sure to match the same port value in 
`./src/config.py`

5. Run `./src/app/api/main.py` script to dump model result into `./src/app/dumps` folder

6. Execute `curl --location --request POST 'http://0.0.0.0:5000/api/predict' --form 'years_experience=15'`

You should get a response like this :
```
{
  "code": 200, 
  "salary": 165604.06906824565
}

```

Work on your own machine learning models
-

It's time to work on your machine learning algorithms. You can use the existent `./src/app/api/main.py` file 
for example to explore your data, clean it, construct and test your machine learning models ... The only requirement is
to dump model result into dumps folder that will be used by `./src/app/api/controllers.py` entry-points.

Connect to the container
-

1. Get container_id by running `docker container ps`

2. Get shell prompt from the container by running `docker exec -it <container_id> sh`
