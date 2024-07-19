pipeline {
    agent any
    stages{
        stage('Clone')  {
            steps   {
                git branch: 'main', credentialsId: 'GitHub', url: 'https://github.com/dang12394/LearnDevOps'
            }
        }
    }
}
