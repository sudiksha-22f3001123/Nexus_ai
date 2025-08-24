# LLM Agent Proof-of-Concept (POC): Browser-Based Multi-Tool Reasoning

Modern LLM-powered agents can combine text generation with external tools like web search, APIs, and live code execution. This proof-of-concept demonstrates a browser-based agent that integrates multiple tools and loops until tasks are complete.

## 🎯 Project Overview

### Goal
Build a minimal JavaScript-based LLM agent that can:
- Take user input in the browser
- Query an LLM for responses
- Dynamically trigger tool calls (search, API proxy, code execution)
- Loop until tasks are complete
- Provide a simple, responsive UI

### Core Features
- **Multi-Tool Integration**: Web search, HTTP proxy, JavaScript execution
- **OpenAI-Style Function Calling**: Tool invocation via function calls
- **Real-time Processing**: Live feedback with thinking indicators
- **Error Handling**: Graceful error management

## 🛠️ How It Works

### Core Agent Logic
```python
def loop(llm):
    msg = [user_input()]
    while True:
        output, tool_calls = llm(msg, tools)
        print("Agent: ", output)
        if tool_calls:
            msg += [handle_tool_call(tc) for tc in tool_calls]
        else:
            msg.append(user_input())
```

### Workflow
1. **User Input** → user types a query
2. **LLM Processing** → query sent with tools
3. **Tool Selection** → LLM decides tools
4. **Tool Execution** → tools run and return results
5. **Integration** → results added to context
6. **Response Generation** → LLM replies or continues

## 🚀 Supported Tool Calls

### 1. Web Search (`search_snippets`)
- **Purpose**: Get real-time web results
- **API**: Google Custom Search JSON API
- **Usage**: Research, fact-checking

### 2. HTTP Proxy (`ai_pipe_proxy`)
- **Purpose**: Make HTTP requests via proxy
- **API**: AI Pipe proxy service
- **Usage**: Fetch APIs, bypass CORS

### 3. JavaScript Execution (`exec_js`)
- **Purpose**: Run JavaScript safely
- **Environment**: Web Workers sandbox
- **Usage**: Calculations, demos

## 💻 Setup Instructions

### Prerequisites
- Python 3.11+
- Git
- Modern browser

### Installation
```bash
git clone <repository-url>
cd "llm proj"
pip install -r requirements.txt
```

### Run Server
```bash
python app.py
```
Open [http://localhost:5000](http://localhost:5000).

### Configuration
- **AI Pipe Token**: Required for LLM
- **Google API Key & CSE ID**: For web search
- **Model Selection**: Choose OpenAI or OpenRouter model

## 📁 File Structure
```
llm proj/
├── README.md
├── requirements.txt
├── app.py
├── index.html
└── test.html
```

## 📋 Example Agent Conversations

**Web Search Example**
```
User: Latest AI news
AI: [SEARCH_SNIPPETS] → returns snippets
```

**Code Execution Example**
```
User: Factorial of 10
AI: [EXEC_JS] → returns 3628800
```

**HTTP Proxy Example**
```
User: Fetch GitHub user data
AI: [AI_PIPE_PROXY] → returns profile
```

## 🔒 Security
- **Web Workers**: Sandboxed JS execution
- **Token-based Auth**: Secure LLM access
- **Input Validation**: For API calls

## 🔮 Future Enhancements
- Plugin system for new tools
- Persistent chat history
- Export conversations

## 📄 License
MIT
