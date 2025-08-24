# LLM Agent Proof-of-Concept (POC): Browser-Based Multi-Tool Reasoning

![Nexus AI](https://img.shields.io/badge/Nexus-AI-blue?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=for-the-badge&logo=javascript)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green?style=for-the-badge&logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple?style=for-the-badge&logo=bootstrap)

Modern LLM-powered agents aren't limited to text—they can combine LLM output with external tools like web search, pipelined APIs, and even live code execution! This proof-of-concept demonstrates building a browser-based agent that can use multiple tools, looping as needed to accomplish complex goals.

## 🎯 Project Overview

### Goal
Build a minimal JavaScript-based LLM agent that can:
- Take user input in the browser
- Query an LLM for intelligent responses
- Dynamically trigger tool calls (search, API workflows, code execution) based on LLM decisions
- Loop until tasks are complete, integrating results at each step
- Provide a premium user experience with modern UI/UX

### Core Features
- **Multi-Tool Integration**: Web search, HTTP proxy, JavaScript execution
- **OpenAI-Style Function Calling**: Industry-standard tool invocation interface
- **Real-time Processing**: Live feedback with "thinking" indicators
- **Premium UI/UX**: Glassmorphism design with responsive layout
- **Error Handling**: Graceful error management with user-friendly alerts
- **Theme Support**: Light/dark mode switching

## 🛠️ How It Works

### Core Agent Logic
The agent implements an intelligent reasoning loop based on this core logic:

```python
def loop(llm):
    msg = [user_input()]  # App begins by taking user input
    while True:
        output, tool_calls = llm(msg, tools)  # Send conversation + tools to LLM
        print("Agent: ", output)  # Always stream LLM output
        if tool_calls:  # Continue executing tool calls until LLM decides it needs no more
            msg += [handle_tool_call(tc) for tc in tool_calls]  # Handle multiple tool calls
        else:
            msg.append(user_input())  # Add user input and continue
```

### Workflow
1. **User Input**: User types a question or request
2. **LLM Processing**: Query LLM with conversation history and available tools
3. **Tool Selection**: LLM decides which tools (if any) to use
4. **Tool Execution**: Execute selected tools and collect results
5. **Integration**: Add tool results to conversation context
6. **Response Generation**: LLM provides final response or continues reasoning
7. **Loop**: Repeat until task completion

## 🔧 Technologies Used

### Frontend
- **HTML5**: Semantic markup with modern standards
- **CSS3**: Advanced styling with custom properties and animations
- **JavaScript ES6+**: Modern JavaScript with async/await, modules
- **Bootstrap 5.3.3**: Responsive UI framework with utilities
- **Bootstrap Icons**: Comprehensive icon library
- **Inter Font**: Premium typography for modern appearance

### Backend
- **Python 3.11+**: Modern Python with type hints
- **Flask 2.3.3**: Lightweight web framework with debug mode
- **Werkzeug**: WSGI utilities for development server

### APIs & Services
- **OpenAI API**: LLM processing with function calling
- **Google Custom Search API**: Web search capabilities
- **AI Pipe Proxy**: CORS bypass and API management
- **Web Workers**: Sandboxed JavaScript execution

### Architecture
- **Single Page Application (SPA)**: Client-side rendering
- **RESTful API**: Clean separation of concerns
- **Event-Driven**: Asynchronous processing with promises
- **Modular Design**: Separation of UI, logic, and API layers

## 🚀 Supported Tool Calls

### 1. Web Search (`search_snippets`)
- **Purpose**: Get real-time web search results
- **API**: Google Custom Search JSON API
- **Features**: Snippet extraction, relevance ranking
- **Usage**: Research, fact-checking, current events

### 2. HTTP Proxy (`ai_pipe_proxy`)
- **Purpose**: Make HTTP requests through CORS proxy
- **API**: AI Pipe proxy service
- **Features**: GET/POST requests, JSON processing
- **Usage**: API integration, data fetching

### 3. JavaScript Execution (`exec_js`)
- **Purpose**: Execute JavaScript code safely
- **Environment**: Web Workers sandbox
- **Features**: Console capture, error handling
- **Usage**: Calculations, data processing, demonstrations

## 💻 Local Setup Instructions

### Prerequisites
- **Python 3.11+** installed
- **Git** for version control
- **Modern web browser** (Chrome, Firefox, Safari, Edge)
- **Text editor** (VS Code recommended)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd "llm proj"
   ```

2. **Install Python Dependencies**
   ```bash
   pip install flask==2.3.3 werkzeug
   ```
   
   Or using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**
   - Get AI Pipe token from [AI Pipe](https://aipipe.ai)
   - (Optional) Get Google API key and Custom Search Engine ID
   - Configure in the application setup panel

4. **Start the Server**
   ```bash
   python app.py
   ```

5. **Open in Browser**
   - Navigate to `http://localhost:5000`
   - The application will open automatically

### Configuration
1. **AI Pipe Token**: Required for LLM functionality
2. **Google API** (Optional): For web search capabilities
3. **Provider Selection**: Choose OpenAI or OpenRouter
4. **Model Selection**: Select your preferred LLM model

## 📁 File Structure

```
llm proj/
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
├── requirements.txt          # Python dependencies
├── app.py                   # Flask server application
├── index.html               # Main application (SPA)
└── test.html               # Button testing page
```

### File Descriptions

#### `app.py`
- **Purpose**: Flask web server with development mode
- **Features**: Static file serving, health check endpoint
- **Routes**: 
  - `/` - Main application
  - `/test` - Testing page

#### `index.html`
- **Purpose**: Complete single-page application
- **Components**:
  - Premium UI with glassmorphism design
  - LLM integration with function calling
  - Three tool implementations
  - Real-time chat interface
  - Configuration management
  - Error handling and alerts

#### `test.html`
- **Purpose**: Simple testing page for debugging
- **Usage**: Button click testing, functionality verification

#### `requirements.txt`
- **Purpose**: Python package dependencies
- **Contents**: Flask, Werkzeug versions

## 🎨 UI/UX Features

### Design Elements
- **Glassmorphism**: Modern glass-like effects with backdrop blur
- **Gradient Backgrounds**: Dynamic color schemes
- **Smooth Animations**: CSS transitions and keyframe animations
- **Responsive Design**: Mobile-first approach with breakpoints
- **Accessibility**: ARIA labels, keyboard navigation

### Interactive Components
- **Feature Badges**: Clickable tool demonstrations
- **Setup Panel**: Collapsible configuration interface
- **Chat Interface**: Real-time messaging with timestamps
- **Status Indicators**: Visual feedback for operations
- **Theme Switcher**: Light/dark mode toggle

### User Experience
- **Thinking Indicator**: Shows AI processing status
- **Example Prompts**: Quick-start demonstrations
- **Error Alerts**: User-friendly error messages
- **Auto-scroll**: Automatic chat scrolling
- **Form Validation**: Input validation with feedback

## 📋 Example Agent Conversations

### Web Search Example
```
User: What are the latest developments in artificial intelligence?

AI: I'll search for the latest AI developments for you.
[🔍 SEARCH_SNIPPETS] Searching for "latest developments artificial intelligence 2025"

AI: Based on my search, here are the latest developments in AI:
- GPT-4 and large language models continue advancing
- AI integration in healthcare and autonomous vehicles
- New regulations and ethical frameworks being developed...
```

### Code Execution Example
```
User: Calculate the factorial of 10 using JavaScript

AI: I'll create a JavaScript function to calculate the factorial of 10.
[⚡ EXEC_JS] Executing JavaScript code...

AI: ✅ JavaScript executed successfully!
The factorial of 10 is 3,628,800. Here's how it works:
- Factorial is the product of all positive integers up to n
- 10! = 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1
```

### HTTP Proxy Example
```
User: Get information about a GitHub user using their API

AI: I'll fetch user information from the GitHub API.
[🌐 AI_PIPE_PROXY] Making HTTP request to api.github.com...

AI: Successfully retrieved user data! Here's the information:
- Username: octocat
- Public repositories: 8
- Followers: 4000+
- Bio: "How people build software"
```

## 🔒 Security Considerations

### JavaScript Execution
- **Web Workers**: Isolated execution environment
- **No DOM Access**: Sandboxed from main thread
- **Timeout Protection**: Prevents infinite loops
- **Error Containment**: Graceful error handling

### API Security
- **Token-based Authentication**: Secure API access
- **CORS Proxy**: Managed through AI Pipe service
- **Input Validation**: Client and server-side validation
- **Error Sanitization**: Safe error message display

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Commit changes**: `git commit -m "Description"`
4. **Push to branch**: `git push origin feature-name`
5. **Submit pull request**

### Development Guidelines
- Keep code simple and hackable
- Follow existing code style
- Add comments for complex logic
- Test new features thoroughly
- Update documentation as needed

## 🐛 Troubleshooting

### Common Issues

#### Server Won't Start
- Check Python version (3.11+ required)
- Install Flask: `pip install flask==2.3.3`
- Check port 5000 availability

#### AI Not Responding
- Verify AI Pipe token configuration
- Check browser console for errors
- Ensure internet connectivity
- Try different LLM model/provider

#### Tools Not Working
- Web Search: Configure Google API credentials
- HTTP Proxy: Check AI Pipe service status
- JavaScript: Verify Web Workers support

### Debug Mode
The Flask server runs in debug mode with:
- **Auto-reload**: Automatic server restart on file changes
- **Debug console**: Detailed error information
- **Development tools**: Enhanced debugging capabilities

## 📊 Performance Optimization

### Frontend
- **Minimal Dependencies**: Lightweight external libraries
- **Efficient DOM Manipulation**: Optimized element creation
- **CSS Animations**: Hardware-accelerated transitions
- **Lazy Loading**: On-demand resource loading

### Backend
- **Flask Development Server**: Fast development iteration
- **Static File Serving**: Efficient asset delivery
- **Minimal Processing**: Lightweight request handling

## 🔮 Future Enhancements

### Planned Features
- **Plugin System**: Extensible tool architecture
- **Chat History**: Persistent conversation storage
- **Export Options**: Save conversations and results
- **Advanced Tools**: Database integration, file processing
- **Collaboration**: Multi-user support

### Technical Improvements
- **TypeScript**: Enhanced type safety
- **Testing Suite**: Automated testing framework
- **Docker Support**: Containerized deployment
- **Production Build**: Optimized production setup

## 📄 MIT License


