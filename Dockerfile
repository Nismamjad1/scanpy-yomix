FROM python:3.11-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install yomix from source
RUN git clone https://github.com/perrin-isir/yomix.git /tmp/yomix && \
    pip install --no-cache-dir -e /tmp/yomix

# Copy your scanpy fork/project
COPY . .

# Install your package with yomix extra
RUN pip install --no-cache-dir -e .[yomix]

EXPOSE 8050

CMD ["python"]

