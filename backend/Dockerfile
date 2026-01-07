FROM python:3.9-alpine

RUN adduser -D appuser

WORKDIR /app

COPY app.py .

RUN chown appuser:appuser app.py

USER appuser

EXPOSE 8080

CMD ["python", "app.py"]

