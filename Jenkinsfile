pipeline {
    agent any
    stages {
        stage('clone') {
            steps {
                // git credentialsId: 'gh_fans3210', url: 'https://github.com/fans3210/TestRepo1.git'
                checkout scm
            }
        }
        
        stage('build docker image') {
            steps {
                // sh 'docker build -t algoimg/testrepo .'
                echo 'githubconfig = ' + scm.getUserRemoteConfigs()
                echo 'githubconfig geturl = ' + scm.getUserRemoteConfigs()[0].getUrl()
                echo 'github repo name = ' + scm.getUserRemoteConfigs()[0].getUrl().tokenize('/')[3].split("\\.")[0]
                echo 'build number = ' + "$BUILD_NUMBER"
                script {
                    dockerImage = docker.build 'algoimg/testrepo' + ":$BUILD_NUMBER"
                }
            }
        }
    }
}
