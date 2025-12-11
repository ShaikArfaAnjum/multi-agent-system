from tools.tool_selector import select_tool

class AgentOrchestrator:
    def __init__(self, llm):
        self.llm = llm

    def run(self, task):
        tool = select_tool(task)
        tool_output = tool.run(task)
        final_output = self.llm(tool_output)
        return final_output
