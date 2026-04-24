from fastapi import FastAPI


app = FastAPI(title="CI/CD Example")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
