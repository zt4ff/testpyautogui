# How to run pyautogui headless in docker

## Steps

- Build an image

  - `docker build -t <IMAGE_NAME> .`

- Run an interactive container from this image

  - `docker run -it --name <CONTAINER_NAME> <IMAGE_NAME>`

- start a virtual display (with given arbitary display number)

  - `source ./start_vd.sh 8`

- Run the virtual environment

  - `source /opt/venv/bin/activate`

- Stop the virtual display (started with the number chosen above)

  - `./stop_vd.sh 8`

- Exit the shell by `Ctrl + C`


## Copy files from docker container to local dir

- `docker cp <CONTAINER_NAME>:/home/screenshots .`