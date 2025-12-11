class WriterTool:
    name = "Writer Tool"

    def run(self, task):
        task_lower = task.lower()

        if "multi-agent system" in task_lower:
            return (
                "Multi-agent systems (MAS) consist of multiple intelligent agents "
                "working together to solve problems that are difficult or impossible "
                "for a single agent to solve. Benefits include:\n"
                "1. Parallelism: Multiple agents can work simultaneously, increasing efficiency.\n"
                "2. Scalability: New agents can be added to handle larger tasks.\n"
                "3. Flexibility: Agents can adapt to changes in the environment.\n"
                "4. Robustness: Failure of one agent does not crash the entire system.\n"
                "5. Distributed problem-solving: Agents can solve parts of a problem locally and combine results."
            )
        
        # Default fallback
        return f"Here is a well-written answer:\n{task}"
