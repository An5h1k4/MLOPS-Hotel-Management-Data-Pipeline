pipeline{
    agent any
    environment{
        VENV_DIR = 'venv'
        GCP_PROJECT = "triple-acre-472518-h7"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }
    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/An5h1k4/MLOPS-Hotel-Management-Data-Pipeline.git']])
                }
            }
        }
        stage('Setting up our virtual environment'){
            steps{
                script{
                    echo 'Setting up our Virtual Environment and Installing dependencies........'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
        
        stage('Building and Pushing Docker Image to GCR'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GCP_KEY_FILE')]) {
                    script {
                        echo 'Building and Pushing Docker Image to GCR.............'
                        
                        // Use triple single quotes to let shell expand variables at runtime
                        sh '''
                        # Add gcloud to PATH
                        export PATH=$PATH:/var/jenkins_home/google-cloud-sdk/bin

                        # Debug: ensure the GCP key file exists
                        echo "GCP key file path: $GCP_KEY_FILE"
                        ls -l "$GCP_KEY_FILE"

                        # Authenticate with GCP
                        gcloud auth activate-service-account --key-file="$GCP_KEY_FILE"

                        # Set the GCP project
                        gcloud config set project $GCP_PROJECT

                        # Configure Docker to use gcloud credentials
                        gcloud auth configure-docker --quiet

                        # Build Docker image
                        docker build -t gcr.io/$GCP_PROJECT/ml-project:latest .

                        # Push Docker image to GCR
                        docker push gcr.io/$GCP_PROJECT/ml-project:latest
                        '''
                    }
                }
            }
        }

    }
}