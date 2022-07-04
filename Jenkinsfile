pipeline{
        agent any
        environment {
        DOCKER_HUB_CREDS_USR = credentials('dockerhub_id')
        DOCKER_HUB_CREDS_PSW = credentials('dockerhub_id')
        }

        stages{
            stage('Testing'){
                steps{
                    git branch: '/main', url: 'https://github.com/ThomasStoyles/BorderlandsWeaponGen'
                    sh '''sudo apt install python3 python3-pip python3-venv -y
                    pip3 install pytest pytest-cov
                    sudo chmod +x test.sh
                    ./test.sh '''

                }
            }
            stage('Deploy'){
                steps{

                    sh '''scp docker-compose.yaml Thomas@swarm-manager:/home/Thomas/
                    scp nginx.conf Thomas@swarm-manager:/home/Thomas/
                    ssh Thomas@swarm-manager docker stack deploy --compose-file docker compose.yaml deployment-stack
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