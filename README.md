# Java Code Standards MCP Server

An MCP server that exposes Java coding standards as queryable rules — for use in AI-assisted code generation and review.

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
.venv/Scripts/python.exe -m src.app
```

Server starts at `http://localhost:80`. SSE endpoint: `http://localhost:80/sse`.

## Connect to Claude Code

**1. Start the server** (see Run section above).

**2. Register the MCP server** in Claude Code:

```bash
claude mcp add --transport sse java-code-standards http://localhost:80/sse
```

**3. Verify it's connected:**

```bash
claude mcp list
```

> By default the server is registered for the current project only.
> To make it available across all your projects, add `--scope user` to the command in step 2.

**4. Copy `CLAUDE.md` to the root of your project:**

```bash
cp CLAUDE.md /path/to/your/project/CLAUDE.md
```

Claude Code automatically picks up `CLAUDE.md` from the project root and loads it into context. This file contains the instructions that tell Claude to use the MCP server when writing or reviewing Java code.

## License

MIT License

Copyright (c) 2025 Yurii Shmorgun

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
