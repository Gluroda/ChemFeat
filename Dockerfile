# Use an official Python runtime as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /workdir

# Create a directory for configuration files
RUN mkdir -p /config

# Copy the requirements.txt file to the config directory
COPY requirements.txt /config/

# Copy the current directory contents into the container at /app
COPY /src /workdir

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r /config/requirements.txt

# Copy the entry point script into the container
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Make the entry point script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set the entry point of the container
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
