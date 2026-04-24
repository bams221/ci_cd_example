from fastapi import FastAPI


app = FastAPI(title="Demo app")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "NOT OK"}
