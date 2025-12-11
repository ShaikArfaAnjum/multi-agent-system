🚀 Multi-Agent System Using Python
This project is a lightweight multi-agent system built using Python. It demonstrates how different specialized agents can collaborate to process a wide range of tasks. Each agent is designed to handle one specific capability, and the system automatically selects the right tool based on the user’s input.
The goal of the project is to show how modular agents can work together in a simple orchestration setup, similar to real-world AI agent systems.

✨ Features
1. Calculator Agent
Performs mathematical operations like addition, subtraction, multiplication, and division.
Example:
calculate 5 + 7
2. Search Agent
Returns a mock search result for a given query. This simulates how a real search agent would respond.
3. Summarizer Agent
Creates a short summary of long text by extracting the first key portion.
4. Writer Agent
Generates a clear and structured written response to general questions.

🧠 How It Works
The user enters a task (e.g., "calculate 12 / 3", "summarize this text", or "write about AI").
The Orchestrator analyzes the input and chooses the appropriate agent.
The selected agent processes the task.
The final result is refined and displayed to the user.
This architecture represents the foundational concept of multi-agent collaboration, where each tool performs a focused job.

🎯 Purpose of the Project
The project is designed for learning and experimentation, especially for understanding:
Tool selection and routing
Basic orchestration logic
Modular design in agent-based systems
Real-world applications of multi-agent workflows

It serves as a starting point for more advanced agentic systems and can be expanded with new tools or integrated with LLMs.
🔧 Technologies Used
Python 3
Simple tool-based agent architecture
Modular folder structure for easy extension

📌 Future Improvements
Add memory for agents
Connect to real APIs
Enable conversation history
Improve summarization with NLP techniques

📥 Conclusion
This project illustrates how multiple small agents can work together to solve different tasks efficiently. It is simple, easy to extend, and acts as a foundation for building more advanced AI agent systems.

