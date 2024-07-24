# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install Strawberry GraphQL and other dependencies
RUN pip install --no-cache-dir strawberry-graphql[debug-server]

# Define environment variable for the port
ENV PORT 8000

# Expose the port the app runs on
EXPOSE 8000

# Run the server
CMD ["strawberry", "server", "schema"]