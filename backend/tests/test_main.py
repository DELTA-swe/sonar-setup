# tests/test_main.py
import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_read_root():
    """Test that the root endpoint returns a 200 status code and the expected response."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_add_endpoint():
    """Test that the add endpoint adds two numbers correctly."""
    # Test with positive numbers
    response = client.get("/add?a=1&b=1")
    assert response.status_code == 200
    assert response.json() == {'result': 2}

    # Test with negative numbers
    response = client.get("/add?a=-5&b=-3")
    assert response.status_code == 200
    assert response.json() == {'result': -8}

    # Test with mixed signs
    response = client.get("/add?a=1&b=-2")
    assert response.status_code == 200
    assert response.json() == {'result': -1}

def test_subtract_endpoint():
    """Test that the subtract endpoint subtracts two numbers correctly."""
    
    # Test with positive numbers
    response = client.get("/subtract?a=2&b=2")
    assert response.status_code == 200
    assert response.json() == {'result': 0}

    # Test with negative numbers
    response = client.get("/subtract?a=-5&b=3")
    assert response.status_code == 200
    assert response.json() == {'result': -8}

    # Test with positive numbers and negative 'a'
    response = client.get("/subtract?a=-2&b=-3")
    assert response.status_code == 200
    assert response.json() == {'result': 1}

    # Test with negative numbers and positive 'a'
    response = client.get("/subtract?a=2&b=-1")
    assert response.status_code == 200
    assert response.json() == {'result': 3}

    # Test with negative numbers and negative 'a'
    response = client.get("/subtract?a=-1&b=4")
    assert response.status_code == 200
    assert response.json() == {'result': -5}

def test_multiply_endpoint():
    """Test that the multiply endpoint multiplies two numbers correctly."""
    
    # Test with positive numbers
    response = client.get("/multiply?a=2&b=2")
    assert response.status_code == 200
    assert response.json() == {'result': 4}

    # Test with negative numbers
    response = client.get("/multiply?a=-5&b=3")
    assert response.status_code == 200
    assert response.json() == {'result': -15}

    # Test with positive numbers and negative 'a'
    response = client.get("/multiply?a=-2&b=-3")
    assert response.status_code == 200
    assert response.json() == {'result': 6}

    # Test with negative numbers and positive 'a'
    response = client.get("/multiply?a=2&b=-1")
    assert response.status_code == 200
    assert response.json() == {'result': -2}

    # Test with negative numbers and negative 'a'
    response = client.get("/multiply?a=-1&b=4")
    assert response.status_code == 200
    assert response.json() == {'result': -4}

def test_divide_endpoint():
    """Test that the divide endpoint divides two numbers correctly."""
    
    # Test with positive numbers
    response = client.get("/divide?a=2&b=2")
    assert response.status_code == 200
    assert response.json() == {'result': 1}

    # Test with negative numbers
    response = client.get("/divide?a=-5&b=3")
    assert response.status_code == 200
    assert response.json() == {'result': -1.6666666666666667}

    # Test with positive numbers and negative 'a'
    response = client.get("/divide?a=-2&b=-3")
    assert response.status_code == 200
    assert response.json() == {'result': 0.6666666666666666}

    # Test with negative numbers and positive 'a'
    response = client.get("/divide?a=2&b=-1")
    assert response.status_code == 200
    assert response.json() == {'result': -2}

    # Test with negative numbers and negative 'a'
    response = client.get("/divide?a=-1&b=4")
    assert response.status_code == 200
    assert response.json() == {'result': -0.25}


def test_square_endpoint():
    """Test that the square endpoint squares a number correctly."""
    
    # Test with positive number
    response = client.get("/square?a=2")
    assert response.status_code == 200
    assert response.json() == {'result': 4}

    # Test with negative number
    response = client.get("/square?a=-2")
    assert response.status_code == 200
    assert response.json() == {'result': 4}

    # Test with zero
    response = client.get("/square?a=0")
    assert response.status_code == 200
    assert response.json() == {'result': 0}

    # Test with large number
    response = client.get("/square?a=1000000")
    assert response.status_code == 200
    assert response.json() == {'result': 1000000000000}

    # Test with large negative number
    response = client.get("/square?a=-1000000")
    assert response.status_code == 200
    assert response.json() == {'result': 1000000000000}

    
    