# BorderlandsWeaponGen

### Table of contents

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
The architecture for this project will be as followed...

Service 1 - This service will be the frontend of the application. This will be what the user sees and will be very basic.

Service 2 - This will be the first randomized value. For my project this will be types of manufacturers that can be drawn at random. 

Service 3 - This will be the second randomized value. For my project this will be a number between 0-105 which will then correlate to the rarity of the weapon which will be defined in service 4.

Service 4 - This service will be where everything comes together and will be sent back to service 1. In here we will have the numbers from service 3 be defined into groups so this number represents this rarity. In here we will also have a list of damage types which can be put on each weapon. 

Service 5 - The last service will be an nginx proxy container. This will allow me to make it so the app only shows up on port 80.

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
![alt text]()


### Service 2
Service 2 is going to be our first random service. Within this service we will be setting the gun manufacturers from the game Borderlands. This has been done in a list which can be seen in the screenshot below. 

![alt text]()
Once the list has been created we used the random package to randomly pick one of these manufacturers and then store that until we need it later in service 4.


### Service 3
Service 3 is the second part of the randomly generated service. This service will be used to give the gun a rarity. This will be done the same way as service 2 by putting all the rarity options in a list and then using the random package. Picking one randomly and storing that until service 4 needs it. This can bee seen in the screenshot below.
![alt text]()


### Service 4
Service 4 is where the two random services, 3 and 4, will be given values which will add up to give one overall value. In my code I have made diffrent manufacturers which will have diffrent values, these values will add up to the overall damage of the gun you are creating. The other feature will be the rarity of the gun which will also add to the overall damage of the gun. This has been achieved by using if statements to say if the manufacturer is this then add this amount. Please see the image below to show this.
![alt text]()


# Testing

With the testing I used pytest to test all the lines of code was being used and are fully working. Below are some screenshots with breif comments on what the tests are doing and achieving.

Service 1
![alt text]()
Here you can see see the tests for service one. Within this test you can see that we are trying to create a gun so we set the services to our own answers so here we have Jakobs, Uncommon and 65, as 65 is the total for the combination of the two other values. We then check if the client is able to get them three answers from the three mock services, which we have set up.

Service 2
![alt text]()
In service 2 we are just checking that the test is able to get a random value from the list manufacturer. Here we asked it to get the value Jakobs.

Service 3
![alt text]()


Service 4
![alt text]()



# Docker Swarm

# Ansible

# Known app issues

# Challenges

# Future updates

# Conclusion

# Contributors
Thomas Stoyles

# Acknowledgements 
I would like to thank Leon and Adam for all there support when delivering this project.
