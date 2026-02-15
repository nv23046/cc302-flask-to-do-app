FROM python:3.11-slim

# Build arguments for version info
ARG VERSION=1.0.0
ARG BUILD_DATE
ARG VCS_REF

# Labels for Docker image metadata
LABEL org.opencontainers.image.version=$VERSION
LABEL org.opencontainers.image.created=$BUILD_DATE
LABEL org.opencontainers.image.revision=$VCS_REF
LABEL org.opencontainers.image.title="Flask To-Do Application"
LABEL org.opencontainers.image.description="A simple To-Do list application built with Flask and SQLite"
LABEL org.opencontainers.image.source="https://github.com/nv23046/cc312-flask-to-do-app"
LABEL maintainer="nv23046"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/api/version')" || exit 1

CMD ["python", "app.py"]
