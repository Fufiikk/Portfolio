from __future__ import annotations

import argparse
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Fufiikk Portfolio")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.mount("/", StaticFiles(directory=BASE_DIR, html=True), name="site")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run portfolio site with FastAPI + Uvicorn")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind (default: 8000)")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload for development")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    uvicorn.run("main:app", host=args.host, port=args.port, reload=args.reload)


if __name__ == "__main__":
    main()
