How to Delete Docker Image?
Go to window command prompt:

docker login 
docker image ls
docker container prune

How to kill an existing port?

1. find the PID of the port
	netstat -ano | findstr :8080

let's say the result return this:
TCP    0.0.0.0:8080           0.0.0.0:0              LISTENING       16860

2. PID is 16860, so type in the following command:
kill 16860

 
How many folders in total?
1. ML_DEV_LANGDETECT
2. app
3. model

How many files in total?

ML_DEV_LANGDETECT Folder:
	1. .dockerignore
	2. .gitignore
	3. Dockerfile
	4. heroku.yml
	5. requirements.txt
	
	(optional)
	6. readme
	7. TestAPI.py

app Folder:
	8. main.py

model Folder:
	9.model.py 
	10.train_pipeline-0.2.0.pkl

STEP BY STEP INSTRUCTIONS:

step 1: Build the model on GoogleColab and save it as pkl file
step 2: Download the pickle file and put it in "model folder"
step 3: Create a "model.py" in "model folder", this model.py serves as a helper function
step 4: Create main.py to do get and post
step 5: Create a ".dockerignore" file to specific what files to ignore
step 6: Create a "Dockerfile" based on the instruction https://fastapi.tiangolo.com/deployment/docker/
step 7: Create "requirements.txt" to store all dependencies
step 8: VSCode Terminal Command: docker build -t appname
step 9: VSCode Terminal Command: docker run -p 80:80 appname (map the port from Docker container to our port)
step 10: [FastAPI] Visit the localhost:80.docs to test out the get/post
step 11: git init
step 12: add .gitignore
step 13: git add .
step 14: git commit -m "message" 
step 15: git push
step 16: heroku login -> open the heroku website
step 17: create "heroku.yml"
step 18: git add "heroku.yml"
step 19: git commit -m "add heroku.yml"
step 20: heroku create <appName>
step 21: heroku git:remote <appName> : set up a remote Git repository on Heroku, allowing us to deploy our code to the Heroku platform
step 22: heroku stack:set container :specify that we want to use a container-based stack on Heroku, allowing us to deploy containerized applications
step 23: git branch -M main
step 24: git push heroku main
Deployment is done!!!!
step 25: copy and paste the URL : https://language-detection-app-12.herokuapp.com/predict on Postman 
step 26: Test the api and see if it works
