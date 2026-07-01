# Building the Docker Image
FROM ubuntu:18.04
 
# Setting up the environment
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
 
RUN pip3 install -U scikit-learn
 
# Copying the application code
COPY application.py /
 
# Running the application
CMD ["python3", "application.py"]

# Building the Docker Image
docker build -t prediction-model .

# Pushing the Docker Image to Amazon ECR
$(aws ecr get-login --no-include-email)
docker tag prediction-model:latest <your-aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/prediction-model:latest
docker push <your-aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/prediction-model:latest

# Setting up AWS ECS
# 1. Create a new ECS cluster
# 2. Create a new task definition
# 3. Create a new service
# 4. Configure the services to use the task definition with our Docker image
# 5. Deploy the task and service