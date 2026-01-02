from fastapi import FastAPI, HTTPException, Request
from logger import logger
from middleware import request_id_middleware
from exceptions import unhandled_exception_handler

app = FastAPI(title="Orders Service")

app.middleware("http")(request_id_middleware)
app.add_exception_handler(Exception, unhandled_exception_handler)

@app.on_event("startup")
def startup():
    logger.info("orders service started")

@app.get("/orders/{order_id}")
def get_order(order_id: int, request: Request):
    logger.info(
        "order request received",
        {
            "request_id": request.state.request_id,
            "order_id": order_id,
            "path": request.url.path
        }
    )

    if order_id <= 0:
        logger.warning(
            "invalid order id",
            {
                "request_id": request.state.request_id,
                "order_id": order_id
            }
        )
        raise HTTPException(status_code=400, detail="invalid order id")

    logger.info(
        "order processed successfully",
        {
            "request_id": request.state.request_id,
            "order_id": order_id
        }
    )

    return {"status": "ok"}
