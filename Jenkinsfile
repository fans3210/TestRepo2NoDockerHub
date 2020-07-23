node {
    agent { dockerfile true }
    def app
    stage('clone repo') {
        checkout scm
    }

    stage('build image') {
        app = docker.build('algo/testrepo')
    }
}