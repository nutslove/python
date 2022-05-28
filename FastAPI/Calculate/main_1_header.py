from fastapi import FastAPI, Response, Header
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from typing import Optional
from io import BytesIO
from PIL import Image
import httpx
import time

app = FastAPI()

@app.get("/api/v1/calculate")
def plus(
    operator:str = "",
    num_1: int = 10,
    num_2: int = 90,
    x_request_id: Optional[str] = Header(None),
    x_b3_traceid: Optional[str] = Header(None),
    x_b3_spanid: Optional[str] = Header(None),
    x_b3_parentspanid: Optional[str] = Header(None),
    x_b3_sampled: Optional[str] = Header(None),
    x_b3_flags: Optional[str] = Header(None),
    x_ot_span_context: Optional[str] = Header(None)
    ): ## parameterとして定義したもの(ex. operator)は初期値を定義しておく必要がある。(でないとエラーになる)

    print('--------------------------------Trace--------------------------------')
    print('Request ID      : ', x_request_id)
    print('Trace ID        : ', x_b3_traceid)
    print('Span ID         : ', x_b3_spanid)
    print('Parent Span ID  : ', x_b3_parentspanid)
    print('Sampled         : ', x_b3_sampled)
    print('B3 Flags        : ', x_b3_flags)
    print('ot span context : ', x_ot_span_context)
    print('--------------------------------Trace--------------------------------')

    if operator == "addition":
        result = num_1 + num_2
    elif operator == "multiplication":
        result = num_1 * num_2
    else:
        result = 77

    title = "猫と足し算の部屋"
    calculation = "足し算"

    db_url = "http://db.default.svc.cluster.local/cat/Ruka"
    with httpx.Client() as client:
        if x_b3_flags is None and x_ot_span_context is None:
            headers = {
                'x-request-id': x_request_id,
                'x-b3-traceid': x_b3_traceid,
                'x-b3-spanid': x_b3_spanid,
                'x-b3-parentspanid': x_b3_parentspanid,
                'x-b3-sampled': x_b3_sampled,
                }
        else:
            headers = {
                'x-request-id': x_request_id,
                'x-b3-traceid': x_b3_traceid,
                'x-b3-spanid': x_b3_spanid,
                'x-b3-parentspanid': x_b3_parentspanid,
                'x-b3-sampled': x_b3_sampled,
                'x-b3-flags': x_b3_flags,
                'x-ot-span-context': x_ot_span_context
                }

        db = client.get(db_url, headers=headers)
    return result, {"title": title, "calculation": calculation}, "cat", db.text

@app.get("/api/v1/image/{animal}")
def image_get(
    animal: str,
    x_request_id: Optional[str] = Header(None),
    x_b3_traceid: Optional[str] = Header(None),
    x_b3_spanid: Optional[str] = Header(None),
    x_b3_parentspanid: Optional[str] = Header(None),
    x_b3_sampled: Optional[str] = Header(None),
    x_b3_flags: Optional[str] = Header(None),
    x_ot_span_context: Optional[str] = Header(None)
    ):

    print('--------------------------------Trace--------------------------------')
    print('Request ID      : ', x_request_id)
    print('Trace ID        : ', x_b3_traceid)
    print('Span ID         : ', x_b3_spanid)
    print('Parent Span ID  : ', x_b3_parentspanid)
    print('Sampled         : ', x_b3_sampled)
    print('B3 Flags        : ', x_b3_flags)
    print('ot span context : ', x_ot_span_context)
    print('--------------------------------Trace--------------------------------')

    # image_url = "http://172.31.43.217:8080/api/v1/cat"
    image_url = "http://image.default.svc.cluster.local/api/v1/" + animal
    with httpx.Client() as client:
        if x_b3_flags is None and x_ot_span_context is None:
            headers = {
                'x-request-id': x_request_id,
                'x-b3-traceid': x_b3_traceid,
                'x-b3-spanid': x_b3_spanid,
                'x-b3-parentspanid': x_b3_parentspanid,
                'x-b3-sampled': x_b3_sampled,
                }
        else:
            headers = {
                'x-request-id': x_request_id,
                'x-b3-traceid': x_b3_traceid,
                'x-b3-spanid': x_b3_spanid,
                'x-b3-parentspanid': x_b3_parentspanid,
                'x-b3-sampled': x_b3_sampled,
                'x-b3-flags': x_b3_flags,
                'x-ot-span-context': x_ot_span_context
                }

        image = client.get(image_url, headers=headers)
    image = Image.open(BytesIO(image.content))
    image.save(f"static/{animal}.jpg")
    image_file = f"static/{animal}.jpg"
    return FileResponse(image_file)