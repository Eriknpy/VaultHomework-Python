# Stage 1: Build Stage
# Use an official Python runtime as a parent image
FROM python:3.9-slim as builder

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY ./requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy the rest of your application's code
COPY ./ .

# Stage 2: Run Stage
# Use a smaller image
FROM python:3.9-slim

# Copy the built artifacts from the builder stage
WORKDIR /usr/src/app
COPY --from=builder /usr/src/app .
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are usable:
ENV PATH=/root/.local:$PATH

# Run your application
CMD ["python", "main.py"]