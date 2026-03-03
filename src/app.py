import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.server import mcp

app = FastAPI()


@app.get("/alive")
async def alive() -> JSONResponse:
    return JSONResponse({"status": "alive"})


mcp_asgi = mcp.http_app(transport="sse")
app.mount("/", mcp_asgi)


if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=80)
