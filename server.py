import sqlite3
from mcp.server import MCPServer

# CHANGE 1: We create the MCP Bridge and give it a professional name
mcp = MCPServer("HR_Database_Agent")

# CHANGE 2: The Decorator. 
# This '@mcp.tool()' acts like a glowing neon sign. 
# It tells any connecting AI: "You are allowed to use this specific function!"
@mcp.tool()
def get_employee_by_name(name: str) -> str:
    """Fetch an employee's details by their name from the company database."""
    
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM employees WHERE name = ?", (name,))
    result = cursor.fetchone() 
    conn.close()
    
    if result:
        emp_name = result[1]
        department = result[2]
        salary = result[3]
        return f"{emp_name} works in {department} and earns {salary}."
    else:
        return f"No employee found with the name {name}."

# CHANGE 3: We remove the human testing area (the print statements).
# Instead, we tell the engine to turn on and listen silently for an AI.
if __name__ == "__main__":
    mcp.run()