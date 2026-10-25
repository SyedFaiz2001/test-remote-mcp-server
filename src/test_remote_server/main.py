from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool
def random_number(min: int, max:int) -> int:
    """Generate a random number between min and max."""
    return random.randint(min, max)

@mcp.resource("info://server")
def server_info():
    """Return server information."""
    info = {
        'name':'Simple Calculator Server',
        'version':'1.0',
        'description':'A simple calculator server that can add numbers and generate random numbers.',
        'tools': ['add', 'random_number'],
        'authors': 'FAIZ',
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)