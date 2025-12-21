class SummarizerTool:
    def run(self, text):
        words = text.split()
        return " ".join(words[:20]) + ("..." if len(words) > 20 else "")
