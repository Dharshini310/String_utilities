pipeline{
    agent any

    stages {
        stage ("Install pytest")
        {
            steps{
                bat "python -m pip install pytest"
            }
        }

        stage ("Run tasks")
        {
            steps{
                bat "python -m pytest"
            }
        }
    }
}