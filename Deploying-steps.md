

# Steps to deploy a simple app in Kubernetes:
1. Create your app to deploy. I created a Python app called simple-sorter.py

2. Write down the steps required to set up an environment for your app. E.g:
    1. Base OS should be Linux
    2. Install Python
    3. Install dependencies 
    4. Copy source code to new environment
    5. Provide command for app. What do you want to do with the app in the new environment. E.g.: run bash to execute or just execute upon starting container.

3. Create Dockerfile.
    1. In a fresh new directory add your app file and any dependencies, along with a new file called Dockerfile (no extensions).
    2. Open Dockerfile in any text editor and write instructions to set up environment in the following format: <instruction> <argument>. See the DOokerfile I created in this repo.
    3. Save and exit.

4. Build Docker file in your local shell providing the directory it is in and the name you want to give it. E.g.:
    * `docker build . -t my-image`

5. Run the Dockerfile and see if the image is being pulled and the container running correctly.
    * `docker run my-image`

6. Push your directory containing this Dockerfile and app files to a Github repo.

7. Share your image to container registry like Docker Hub.

8. Create YAML files for your deployment. These would most likely include a pod definition file, a replicaset definition file and finally a deployment definiton file.
    - See .yml files in repo
    - These files will be the ones pulling your Docker image containg the app.

9. Set up your Kubernetes cluster, (I used an online [Kubernetes playground](https://www.katacoda.com/courses/kubernetes/playground) with the kubectl tool installed)

10. `git clone` your repo containing all YAML files.

11. `cd` into it

12. Run the `kubectl create -f <deployment-file>.yml` command to create the deployment.

13. Run the `kubectl get all` command to see the status and description of all your pods, replicasets and deployment.


![](https://media.giphy.com/media/h8ZUMDy8LWxGW4h73I/giphy.gif)
