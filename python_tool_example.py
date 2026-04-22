"""
Each script must define a `main` function, which serves as the entry point for the Tool.

If your script requires any Python libraries, be sure to:
1. Include the necessary `import xxx` statements in your code.
2. Select these libraries in Step 1[Basic Settings] > Dependency Library.

Parameters:
- `input`: A dictionary containing the input parameters defined in Step 2[Parameter Configuration].

Return:
- A dictionary that matches the output parameters defined in Step 2[Parameter Configuration].

⚠️ Make sure to configure both input and output parameters in Step 2[Parameter Configuration], so that the LLM can correctly understand and use your tool.
"""

def add(a, b):
  if a is None or b is None:
    raise ValueError('Parameter a and b must be provided')
  return a+b

def main(input): 
  return {"result": add(input['a'], input['b'])}
