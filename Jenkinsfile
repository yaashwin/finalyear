pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Checkout the code from the GitHub repository
                git url: 'https://github.com/yaashwin/finalyear.git', credentialsId: 'your-credential-id'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install dependencies using npm
                sh 'npm install'
            }
        }
        stage('Build') {
            steps {
                // Run the build script
                sh 'npm run build'
            }
        }
        stage('Test') {
            steps {
                // Run tests
                sh 'npm test'
            }
        }
        stage('Deploy') {
            steps {
                // Deploy the application (this is just a placeholder, adjust as needed)
                sh 'npm run deploy'
            }
        }
    }
}
