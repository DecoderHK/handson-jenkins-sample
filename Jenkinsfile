pipeline {
    agent any
    tools {
        git 'Default'  // Reference the named Git installation
    }
    environment {
        VENV_DIR = 'venv'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/IvanMok510/Form-handon.git', branch: 'main'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                bat '''
                if not exist %VENV_DIR% (
                    python -m venv %VENV_DIR%
                )
                '''
            }
        }
        stage('Start Web Server') {
            steps {
                bat "start /B python -m http.server 8000"
                sleep 5
            }
        }
        stage('Install Dependencies') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Selenium Tests') {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                python py.py
                '''
            }
        }
    }
    post {
        always {
            script {
                bat(script: 'taskkill /F /IM python.exe', returnStatus: true)
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
