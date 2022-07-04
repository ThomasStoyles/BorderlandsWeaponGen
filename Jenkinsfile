pipeline{
        agent any
        environment {
        DOCKER_HUB_CREDS_USR = credentials('dockerhub_id')
        DOCKER_HUB_CREDS_PSW = credentials('dockerhub_id')
        }

        stages{
            stage('Testing'){
                steps{
                    git branch: '/main', url: 'https://gitlab.com/qacdevops/chaperootodo_client'
                    sh '''sudo apt install python3 python3-pip python3-venv -y
                    pip3 install pytest pytest-cov
                    sudo chmod +x test.sh
                    ./test.sh '''

                }
                
            stage('Test'){
                steps{
                    sh "sudo apt-get update"
                    sh "sudo apt install curl -y"
                    sh "curl https://get.docker.com | sudo bash"
                    sh "sudo usermod -aG docker $(whoami)"
                }
            }
            
            stage('Deploy'){
                steps{
                    sh "sudo apt-get update"
                    sh "sudo apt install curl -y"
                    sh "version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')"
                    sh "sudo curl -L https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose"
                    sh "sudo chmod +x /usr/local/bin/docker-compose"
                    sh "docker-compose --version"
                }
            }
            
            stage('Curl'){
                steps{
                    sh "sudo docker-compose pull && sudo -E DB_PASSWORD=${DB_PASSWORD} docker-compose up -d"
                }
            }
        }
}