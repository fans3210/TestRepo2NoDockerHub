def repoNameLower = (scm.getUserRemoteConfigs()[0].getUrl().tokenize('/')[3].split("\\.")[0]).toLowerCase()

pipeline {
    options {
      timeout(time: 10, unit: 'MINUTES') 
    }
    environment {
        dhUser = 'fans3210'
        registryCredential = 'algodockerhub'
        dockerImageSha = ''
        dockerImageLatest = ''
    }
    agent any
    
    stages {
        stage('clone') {
            steps {
                checkout scm
            }
        }
        
        stage('build docker image') {
            steps {
                // sh 'docker build -t algoimg/testrepo .'
                echo 'github repoNameLower = ' + repoNameLower
                script {
                    dockerImageSha = docker.build "$dhUser/$repoNameLower" + ":$GIT_COMMIT"
                    dockerImageLatest = docker.build "$dhUser/$repoNameLower" + ":latest"
                }
            }
        }
        stage('upload to dh') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImageSha.push()
                        dockerImageLatest.push()
                    }
                }
            }
        }
    }
}
