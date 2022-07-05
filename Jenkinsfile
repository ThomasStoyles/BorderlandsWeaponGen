pipeline{
        agent any
        environment {
        DOCKER_HUB_CREDS_USR = credentials('docker-hub-usr')
        DOCKER_HUB_CREDS_PSW = credentials('docker-hub-psw')
        }

        stages{
            stage('Testing'){
                steps{
                    git branch: 'main', credentialsId: 'd0400d76-2d66-40c4-a808-7ea099c737fc', url: 'git@github.com:ThomasStoyles/BorderlandsWeaponGen.git'
                    sh '''sudo apt install python3 python3-pip python3-venv -y
                    pip3 install pytest pytest-cov
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=application service1
                    python3 -m pytest --cov=application service2
                    python3 -m pytest --cov=application service3
                    python3 -m pytest --cov=application service4
                    '''
                }
            }

            stage('Ansible Deployment'){
                steps{
                    git branch: 'main', credentialsId: 'd0400d76-2d66-40c4-a808-7ea099c737fc', url: 'git@github.com:ThomasStoyles/BorderlandsWeaponGen.git'
                    sh 'ssh Thomas@ansible /usr/bin/ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml'
                }
            }
            
            stage('Docker login and biuld conatiners'){
                steps{
                    sh '''docker-compose build 
                        docker login --username $DOCKER_HUB_CREDS_USR --password $DOCKER_HUB_CREDS_PSW
                        docker-compose push'''
                }
            }

            stage('Deploy to swarm'){
                steps{

                    sh '''scp docker-compose.yaml Thomas@swarm-manager:/home/Thomas/
                    scp nginx.conf Thomas@swarm-manager:/home/Thomas/
                    ssh Thomas@swarm-manager docker stack deploy --compose-file docker-compose.yaml deployment-stack
                    '''
                }
            }
            
            stage('Curl'){
                steps{
                    sh ''' curl swarm-manager
                    curl swarm-worker
                    '''
                }
            }

        }
}