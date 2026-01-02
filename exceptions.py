from fastapi import Request
from fastapi.responses import JSONResponse
from logger import logger

async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.error(
        "unhandled exception",
        {
            "request_id": getattr(request.state, "request_id", None),
            "path": request.url.path,
            "method": request.method,
            "error": str(exc)
        }
    )

    return JSONResponse(
        status_code=500,
        content={"error": "internal server error"}
    )
