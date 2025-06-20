FROM python:3.11-slim


# Copy pyproject files
COPY pyproject.toml poetry.lock ./

# Install system dependencies
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --without dev --no-root --no-interaction --no-ansi

# Copy project files
COPY ./src/ /src/

WORKDIR /src/

# Start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
