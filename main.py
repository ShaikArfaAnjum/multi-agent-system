from agents.agent_orchestrator import AgentOrchestrator

# A simple LLM function that just returns the tool output
def llm(prompt: str) -> str:
    return prompt

def main():
    print("=== Multi-Agent System Started ===")
    
    # Ask user for input
    task = input("Enter your task (e.g., 'calculate 5 + 7'): ").strip()
    
    # Initialize the orchestrator
    orchestrator = AgentOrchestrator(llm)
    
    # Run the task through the multi-agent system
    output = orchestrator.run(task)
    
    print("\n=== Final Output ===")
    print(output)

if __name__ == "__main__":
    main()
