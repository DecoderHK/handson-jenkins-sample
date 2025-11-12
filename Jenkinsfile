pipeline {
    agent any
    tools {
        git 'Default'  // Reference the named Git installation
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/IvanMok510/Form-handon.git', branch: 'main'
            }
        }
        stage('Start Web Server') {
            steps {
                bat 'start /B python -m http.server 8000'
                sleep 5
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Selenium Tests') {
            steps {
                bat 'python py.py'
            }
        }
    }
    post {
        always {
            script {  // Use script block to handle exit codes gracefully
                bat(script: 'taskkill /F /IM python.exe', returnStatus: true)  // Ignore failure
                echo 'Pipeline complete.'
            }
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed. Check console output.'
        }
    }
}
