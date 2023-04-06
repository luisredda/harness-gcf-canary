FROM google/cloud-sdk:latest

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install google-cloud-functions

# Copy function code to container
COPY *.py /app

# Set working directory
WORKDIR /app

# Expose port 8080 for function
EXPOSE 8080

# Define command to start the function
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:handler"]
