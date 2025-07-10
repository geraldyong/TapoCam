FROM python:3.13-slim

# Create App User.
RUN addgroup --system apps --gid 1001 && adduser --system appuser --uid 1001 --gid 1001

# Set the working directory.
WORKDIR /app

# Install Python libraries.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -f requirements.txt && \
    mkdir video_chunks && \
    chown appuser:apps video_chunks

# Copy files.
COPY --chown=appuser:apps ./config ./config
COPY --chown=appuser:apps ./models ./models
COPY --chown=appuser:apps ./routes ./routes
COPY --chown=appuser:apps ./utils ./utils
COPY --chown=appuser:apps ./main.py .
COPY --chown=appuser:apps ./requirements.txt .

# Set the default user as the app user.
USER appuser

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]
