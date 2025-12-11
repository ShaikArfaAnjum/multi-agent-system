from .calculator import Calculator
from .search_tool import SearchTool
from .summarizer_tool import SummarizerTool
from .writer_tool import WriterTool

def select_tool(task):
    task_lower = task.lower()

    if "summarize" in task_lower:
        return SummarizerTool()
    elif "search" in task_lower:
        return SearchTool()
    elif "calculate" in task_lower:
        return Calculator()
    # Only pure math expressions (digits, spaces, + - * / .)
    elif all(c.isdigit() or c.isspace() or c in "+-*/.()" for c in task):
        return Calculator()
    else:
        return WriterTool()
