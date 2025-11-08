# Example: DIY Cursor with OpenAI Agents
from agents import Agent, Runner

coder = Agent(name="Coder", instructions="You write and fix code using the repo context.")
tester = Agent(name="Tester", instructions="You run tests and report results.")

result = Runner.run_sync([coder, tester], "Implement quicksort and verify correctness.")
print(result.final_output)
with open("test_output.txt", "a", encoding="utf-8") as f:
    f.write(result.final_output)