from fastapi import FastAPI, HTTPException

app = FastAPI()
@app.get("/")
async def read_root():
    """
    The root endpoint of the API.

    Returns a simple message.

    Args:
        None

    Returns:
        A dict with a single key, "message", with the value "Hello, World!".
    """
    return {"message": "Hello, World!"}

@app.get("/add")
async def add(a: int, b: int):
    """
    Add two numbers.

    Args:
        a (int): The augend.
        b (int): The addend.

    Returns:
        A dict with a single key, "result", with the value being the sum of a and b.
    """
    return {'result' : a + b }

@app.get("/subtract")
async def subtract(a: int, b: int):
    """
    Subtract two numbers.

    Args:
        a (int): The minuend.
        b (int): The subtrahend.

    Returns:
        A dict with a single key, "result", with the value being the difference of a and b.
    """
    return {'result' : a - b }

@app.get("/multiply")
async def multiply(a: int, b: int):
    """
    Multiply two numbers.

    Args:
        a (int): The multiplicand.
        b (int): The multiplier.

    Returns:
        A dict with a single key, "result", with the value being the product of a and b.
    """
    
    return {'result' : a * b }

@app.get("/divide")
async def divide(a: int, b: int):
    """
    Divide two numbers.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        The result of the division.

    Raises:
        HTTPException: If b is zero.
    """
    if b == 0:
        raise HTTPException(status_code=400, detail="Divide by zero")
    return {'result' : a / b }

@app.get("/square")
async def square(a: int):
    """
    Calculate the square of a number.

    Args:
        a (int): The number to square.

    Returns:
        A dict with a single key, "result", with the value being the square of a.
    """
    return {'result' : a * a }