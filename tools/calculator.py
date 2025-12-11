class Calculator:
    def run(self, task):
        try:
            expr = task.lower().replace("calculate", "").strip()
            return str(eval(expr))
        except:
            return "Error: invalid expression"
