# Use the official Python image from the Docker Hub
FROM python:3.11

# Set environment variables for Python and Django
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=todolist.todolist.settings

# Set the working directory in the container
WORKDIR /code

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project directory into the container
COPY todolist /code/todolist

# Expose the Django development server port
EXPOSE 8000

# Run Django's development server with manage.py
CMD ["python", "/code/todolist/manage.py", "runserver", "0.0.0.0:8000"]
