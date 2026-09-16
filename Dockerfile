FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache --no-install-project

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uv run python manage.py migrate --noinput && uv run python manage.py createsuperuser --noinput || true && uv run python manage.py runserver 0.0.0.0:8000"]
