# AI-Powered Enterprise Database Agent

A secure, backend bridge that allows AI applications to query a private company SQL database using natural language. Built with Python and the Model Context Protocol (MCP).

## Architecture
* **Database:** SQLite (Relational structure for enterprise data)
* **Backend:** Python
* **API Protocol:** Model Context Protocol (MCP) Server

## Features
* Protected SQL queries to prevent unauthorized data access.
* Translated raw database rows into readable context for LLMs.
* Securely exposed standard Python functions as MCP Tools.