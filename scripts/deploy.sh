#!/bin/bash

# Set environment variables
export DEPLOY_ENV="production"

# Build the application
./gradlew build

# Deploy the application to the server
scp -r build/libs/alphapp.jar user@server:/path/to/deploy

# Run the application on the server
ssh user@server "nohup java -jar /path/to/deploy/alphapp.jar > /dev/null 2>&1 &"

