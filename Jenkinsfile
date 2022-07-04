pipeline{
        agent any
        environment {
        DOCKER_HUB_CREDS_USR = credentials('docker-hub-cred')
        DOCKER_HUB_CREDS_PSW = credentials('docker-hub-cred')
        }

        stages{
            stage('Testing'){
                steps{
                    git branch: 'main', url: 'https://github.com/ThomasStoyles/BorderlandsWeaponGen.git'
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
            stage('Deploy'){
                steps{

                    sh '''scp docker-compose.yaml Thomas@swarm-manager:/home/Thomas/
                    scp nginx.conf Thomas@swarm-manager:/home/Thomas/
                    ssh Thomas@swarm-manager docker stack deploy --compose-file docker-compose.yaml deployment-stack
                    sleep 25
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