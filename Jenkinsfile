pipeline {
    agent any

    stages {

        stage('Create Virtual Environment') {
            steps {
                bat '''
                python -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                venv\\Scripts\\python -m pip install --upgrade pip
                venv\\Scripts\\python -m pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                venv\\Scripts\\python -m pytest
                '''
            }
        }
    }
}
