def yamlData = null
def repoName = null
def userName = null
def parsedCmdStr = """["python3","-u","longrun.py"]"""

pipeline {
    options {
        timeout(time: 10, unit: 'MINUTES') 
    }

    agent { node { label 'kubepod' } }
    // agent any
    stages {
        stage('test read yaml from str') {
            steps {
                script {
                    yamlData = readYaml text: """
                    apiVersion: batch/v1
                    kind: Job
                    metadata:
                        name: ${repoName}-job
                        namespace: algo
                    """
                    assert yamlData.something == 'my datas'
                    assert yamlData.size == 3
                    assert yamlData.isEmpty == false
                }
            }
        }
        stage('test print the yaml obj') {
            steps {
                echo 'yamlData = ' + yamlData
            }
        }
        // stage('prepare') {
        //     steps {
        //         echo 'pwd = ' + pwd()
        //         sh "which curl"
        //         sh "docker ps"
        //     }
        // }
        
        // stage('run kubctl ') {
        //     steps {
        //         sh 'kubectl get pods'
        //     }
        // }
        

    }
}