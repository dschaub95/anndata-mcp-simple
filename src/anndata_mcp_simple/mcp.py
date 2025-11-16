from fastmcp import FastMCP

mcp: FastMCP = FastMCP(
    name="anndata-mcp-simple",
    instructions="A very interesting piece of code",
    on_duplicate_tools="error",
)
