FROM python:3.10-slim

WORKDIR /win_bot

# Create virtual environment
RUN python3 -m venv .venv

# Activate virtual environment
ENV PATH="/win_bot/.venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot/ bot/
COPY app/ app/
COPY run-app.sh /
RUN chmod +x /run-app.sh


