FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    libpq-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /opt/mlmmjadmin

# Copy requirements and install Python dependencies
COPY mlmmjadmin/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY mlmmjadmin/ .

# Create necessary directories for mlmmj
RUN mkdir -p /var/log/mlmmjadmin \
    /var/spool/mlmmj \
    /var/spool/mlmmj-archive \
    /usr/share/mlmmj/text.skel

# Expose API port
EXPOSE 7790

# Run the application
CMD ["python3", "mlmmjadmin.py"]
