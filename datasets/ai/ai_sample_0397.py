FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Copy project files
WORKDIR /usr/src/app
RUN mkdir static
RUN mkdir templates
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD uvicorn app:app --host=0.0.0.0 --port=8000