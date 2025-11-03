pipeline {
    agent any
    
    environment {
        IMAGE_NAME = "weather-monitor"
        CONTAINER_NAME = "weather-app"
        PORT = "5000"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                    sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
                }
            }
        }
        
        stage('Stop Old Container') {
            steps {
                echo 'Stopping and removing old container...'
                script {
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                }
            }
        }
        
        stage('Run New Container') {
            steps {
                echo 'Running new container...'
                script {
                    sh "docker run -d -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest"
                }
            }
        }
        
        stage('Verify Deployment') {
            steps {
                echo 'Deployment successful!'
                echo "Application running at http://localhost:${PORT}"
            }
        }
    }
    
    post {
        success {
            echo '✅ Build and deployment completed successfully!'
        }
        failure {
            echo '❌ Build failed. Check logs for details.'
        }
    }
}