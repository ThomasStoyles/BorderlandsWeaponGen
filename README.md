# BorderlandsWeaponGen

### Table of contents

[Introduction](#Introduction)

[MVP](#MVP)

[Architecture](#Architecture)

[Planning](#Planning)

[Services](#Services)

[Docker-compose](#Docker-compose)

[Jenkins](#Jenkins)

[CI-CD Pipeline](#CI-CD_Pipeline)

[Known app issues](#Known_app_issues )

[Challenges](#Challenges)

[Future updates](#Future_updates)

[Conclusion](#Conclusion)

[Contributors](#Contributors)

[Acknowledgements](#Acknowledgements)

# Introduction 
This project which has been set out by QA is to create an application that genetayes objects. THese will be set upon predefined rules. In this project thes objects will create a random gun from the game Borderlands. This will give you a manufacturer, gun rarity and elemental damage. These objects will be randomized however will be defined in some way.  

This project will involve the following skills...

* Project Management - Trello
* Version Control - GIT
* CI Server - Jenkins
* Configuration Management - Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX


# MVP (Minimum Viable Product) 

This project comes with a set of requirements that will need to be met to ensure completion of the project, also known as the Minimum Viable Product. 
These requirements are as followed...

* A Kanban Board (Trello) - That will have full expansion on tasks that need to be completed and, tasks that have been completed. As well as records of any issues that might be encountered and a risk assessment.

* An Application fully integrated using the Feature-Branch model - Created in Python, this application will have 4 services which will be following the requirements set on my Trello Board.

* CI Server - The application will be built through a CI server, in this case jenkins, which will be deployed to a cloud-based virtual machine. This will also have webhooks integrated so that the application is automaticlly redeployed when changed.

* The project must follow the Service-oriented architecture - This will be displayed below.

* containerisation and orchestration tool - The projec must be deployed using a containerisation and orchestration tool. In this case this will be Docker and Docker swarm.

* Ansible Playbook - This will provision the environment that my application needs to run.

* The project must make use of a reverse proxy.

Once all these requirements have been met the project will be complete.

# Architecture
The architecture for this project will be a 5 service architecture as seen below.

Service 1 - This service will be the frontend of the application. This will be what the user sees and will be very basic.

Service 2 - This will be the first randomized value. For my project this will be types of manufacturers that can be drawn at random. 

Service 3 - This will be the second randomized value. For my project this will be a rarity picked from a list.

Service 4 - This service will be defining what numbers to give to each options. This will then add up to a overall damage number.

Service 5 - The last service will be an nginx proxy container. This will allow me to make it so the app only shows up on port 80.

## My Application
Next lets look at how my application will work following this architecture.
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/User%20diagram.jpg)

* The user will interact with the front-end html page 
* The service will then go to the nginx service/service 5, where it will activate the reverse proxy and listen on port 80
* The front-end/service1 will then got to service 2, service 3 and service 4 and retrive all the data using json
* Then front-end/service1 will then display the new randomized gun to the user by going ther the nginx service (service 5)

# Planning 

### Kanban Board
For the project we had to create a Kanban board, for this I used trello. I used this board to track my progress throughout the application and was able to track what still needs to happen and what has been completed. Below are images of the trello board to help you see this process.
Here I am half way through the project
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/Trello1.jpg)

Here I am close to finishing the project.
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/Trello2.jpg)

### Risk assessment
Below is a image of my risk assessment.

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/Risk.jpg)

# Services

The MVP of the project requires to have multiple services within the application which all work together. Here I will break down these services.

### Service 1
Service 1 is where everything is going to come together. Here we will call all the services and then put them together to be displayed on the html template that we have created.
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/service1.jpg)


### Service 2
Service 2 is going to be our first random service. Within this service we will be setting the gun manufacturers from the game Borderlands. This has been done in a list which can be seen in the screenshot below. 
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/service2.jpg)

Once the list has been created we used the random package to randomly pick one of these manufacturers and then store that until we need it later in service 4.


### Service 3
Service 3 is the second part of the randomly generated service. This service will be used to give the gun a rarity. This will be done the same way as service 2 by putting all the rarity options in a list and then using the random package. Picking one randomly and storing that until service 4 needs it. This can bee seen in the screenshot below.
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/service3.jpg)


### Service 4
Service 4 is where the two random services, 3 and 4, will be given values which will add up to give one overall value. In my code I have made diffrent manufacturers which will have diffrent values, these values will add up to the overall damage of the gun you are creating. The other feature will be the rarity of the gun which will also add to the overall damage of the gun. This has been achieved by using if statements to say if the manufacturer is this then add this amount. Please see the image below to show this.
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/service4.jpg)


# Testing

With the testing I used pytest to test all the lines of code was being used and are fully working. Below are some screenshots with breif comments on what the tests are doing and achieving.

## Service 1

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/service1_tests.jpg)

I then check if the client is able to get the three answers from my three mock services, which I have set up.

## Service 2

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/service2.jpg)

In service 2 we are just checking that the test is able to get a random value from the list manufacturer. Here we asked it to get the value Jakobs.

## Service 3

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/service3_tests.jpg)

Here is very similar to service 2, we take a random value from the rarity here we asked it for Uncommon.

## Service 4

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/service4_tests.jpg)

Service 4 tests multiple things. Firstly it tests if the values that are being added up are correct so for example, Atlas and Common have a overall damage of 15 so we test that this is given back to the service 4. We allow test if the client is able to get the random values from service2 and 3 by using the self.client.post along with the json={}.

# Docker-compose

When I started Docker I knew that I was going to have to incorporate ansible into my docker as well, as I was using ansible to install docker onto my swarm manager and worker. I created a docker-compose.yaml file ready for my swarm manager to deploy once ansible has completed all the set up.
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/docker_compose.jpg)

The docker compose will allow me to create my 5 services in images which will get sent to my docker hub. This allows me to pull the containers to my docker swarm manager and deploy them and the replicas to my swarm. So why do I need to deploy these to multiple other VM's. The reason is so that the VM doesn't get overloaded as one VM might not be able to load all the containers and their replicas without crashing.

I also created a nginx.conf this allowed me to add a reverse proxy to the project as seen in the image below
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/nginx.jpg)

# Docker swarm and Ansible 
Once the docker compose was created I created three VMs these being the docker swarm manager, worker and the ansible machine. This was because I was going to use the ansible playbook to deploy docker onto these two VMs. Firstly we made sure that the ssh key for the ansible VM is in both swarm machines, so that ansible could connect succesfully. Once completed we started working on the ansible playbook.

The playbook was created to deploy docker on the two VMs that I just created. In the image below you can see this playbook. 
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/docker_install_1.jpg)

Once this was done I tested that the ping worked so that the ansible VM could connect to the swarm manager and worker. See image below for proof
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/Pingtest.jpg)


When the ping was successful I tested the playbook installed docker onto both VMs. Firstly we ran the playbook to see if it works. See image below 
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/first_ansible_playbook.jpg)
As you can clearly see the playbook ran successfully and changes was made to the VMs.

We then went on to both VMs to see if docker had been installed.
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/swarm_manager_ansible_proof.jpg)
* Swarm Manager VM

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/swarm_worker_ansible_proof.jpg)
* Swarm worker VM

As you can see docker was installed on both VM's however, this wasn't enough for me therefore I changed the workbook so that it works with roles. The roles allowed the workbook to deploy the swarm and add the worker into the swarm. I organised these tasks into roles which was created using docker galaxy. Please see the images below.


* Here you can see the playbook which has been improved

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/improved_playbook.jpg)


* Here is the improved inventory 

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/improved_inv.jpg)


* Here you can see all the roles and files created by docker galaxy and one of the three files i had to change

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/roles.jpg)


Once this was working I moved onto Jenkins

# Jenkins
Jenkins is going to be used to automatically to deploy everything that we have created above. This is done by using a jenkins file which is on the development VM, I also added a webhook so that when you push something to github jenkins automatically runs the jenkins file. Within the jenkins file we have mulitple stages within the pipeline, as seen below.

* Testing - testing was using using pytest.
* Ansible Deployment - Automatically runs the ansible playbook and does everything within it
* Docker hub login, Container build - Here we will log into docker hub and build the new containers 
* Swarm deployment - Here we deploy the swarm 
* Curl - This isn't needed however I have it to see that the build has been fully successful.

Once all this has been complete the app will be deployed onto the swarm. This can then be accessed via the IP of either the swarm-manager or swarm-worker.

Here are some images of the jenkins pipeline terminal in which each stage has been complete, with comments.
* Here jenkins is running our pytests for the application
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/jenkins_testing.jpg)


* Jenkins the runs the ansible playbook
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/jenkins_playbook.jpg)
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/jenkins_playbook1.jpg)


* Here we have the docker compose being ran and pushed to docker hub

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/jenkins_docker_compose.jpg)




* Next we have the swarm being deployed with the new images plus a 25 second sleep so they have time to deploy
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/Sleep.jpg)


* Lastly we have the curl to show the application is running 
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/curl.jpg)


Here we have a screenshot of the finished pipeline
![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/jenkins_pipeline.jpg)


# CI-CD Pipeline
To help understand how the project works and the tools I used when creating it please see this CI-CD Pipeline I created.

![alt text](https://github.com/ThomasStoyles/BorderlandsWeaponGen/blob/main/Photos%20and%20Screenshots/CI-CD.jpg)

# Known app issues
There is only one issue within the application.

* HTML layout needs to be changed 
* Add a generate button as the one that was implemented doesn't work and was removed
* Table of content is not working 

# Challenges

When creating this project I ran into many challenges which I had to overcome the first challenge was json. When I was creating my python application I originally set myself a task which was above my abilities. Therefore once I had comepleted the application it was impossible to test the application because i had not implemented json correctly. I was not calling json at all the services therefore, I had to change my application to a more simple version and then correctly implemented json so that my service 1 was receiving the data correctly.

The last issue I came across was with the swarm set up. When trying to initialize the swarm I had already created a manager swarm which was on my development VM rather than the swarm manager VM. Therefore I was unable to add my swarm worker to the correct VM, as it was part of the development VM swarm. To change to this I had to remove the development swarm and then add it using the join token this allowed me to put these two vms together in a swarm. 


# Future updates
The application can be improved with future updates, some of my current ideas are as follows:

* Add an nginx balance loader to increase security
* Add an SQL database for store the values generated which will allow for more features
* More complex randomizers

# Conclusion
In conclusion I feel like this project has pushed me into areas that I am new to and, has allowed me to explore areas of DevOps that I wasn't comfortable with. This has made me more confident in my ability in Jenkins and Python while, learning new skills such as Ansible and Docker. This project is not perfect but with more experience I will be able to come back to this project and improve it.

# Contributors
Thomas Stoyles

# Acknowledgements 
I would like to thank Leon and Adam for all there support when delivering this project.
