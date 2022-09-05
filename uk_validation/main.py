import re
from fastapi import FastAPI
from constants import VALIDATION_REGEX

app = FastAPI()


@app.get("/validate/{postcode}")
async def validate_postcode(postcode: str):
    postcode = postcode.upper()
    if re.match(VALIDATION_REGEX, postcode):
        return {"message": "Postcode OK"}
    else:
        return {"message": "Postcode invalid"}
