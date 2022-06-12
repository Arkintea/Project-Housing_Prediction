Software and Account Requirement

Github Account
Heroku Account
VS Code
GIT cli

To create the virtual environment in the same folder with the project
conda create -p venv python==3.7 -y

To activate the created virtual environment
............
conda activate venv/

or

conda activate venv

pip install -r requirements.txt

To add file to git
...............
git add .

or 

git add <filename>

Note: To ignore file or folder from git we can write the name of the file/folder in .gitignore folder
..............

To check status
............
git status

To check all versions maintained by git
...............................
git log

To create version/commit all changes by git
...........................
git commit -m "message"

To send version/changes to github
....................
git push origin main

To check remote url
.................
git remote -v


Deployment

To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = arkintea@gmail.com
HEROKU_API_KEY = cfb3682d-696b-452a-861e-274ef284ed4e
HEROKU_APP_NAME = implem

BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase

.....................
To list docker image
docker images
.......................
Run docker image
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
.......................
To check running container in docker
docker ps
......................
To stop docker conatiner
docker stop <container_id>
.....................