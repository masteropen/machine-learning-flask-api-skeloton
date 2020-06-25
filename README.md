# Machine learning Flask API skeleton

Requirements
-
This project was generated using the following requirements :

- `docker version 19.03.8`

- `docker-compose version 1.25.5`

Build and run the application
-

1. Clone this repository
`git clone https://github.com/masteropen/machine-learning-flask-api-skeloton.git`.

2. You can customize `.env` file and eventually the variable `WORKDIR` in `Dockerfile` to match your own project
directory name under the container.

3. Build application dependencies by placing to the root project directory and run
`docker-compose up` . Compose builds an image for your code, and start service(s).

4. Go to http://0.0.0.0:5000 to see your application running.

Connect to the container
-
1. get container_id by running
`docker container ps`

2. get shell prompt from the container by running
`docker exec -it <container_id> sh`

Enjoy !
