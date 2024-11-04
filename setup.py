from setuptools import setup, find_packages

LONG_DESC = """
Do you find yourself experiencing mixed feelings towards matplotlib? You’re not alone. 
To address this, I developed a mini-project designed to facilitate data visualization through natural language commands. 
This project relies on dependencies such as OpenAI and matplotlib, and it is remarkably user-friendly. 
By leveraging OpenAI’s GPT API, prompt engineering, and few-shot learning, matplotlib_ai can generate graphs without the need for any matplotlib coding. 
For more details, please visit the GitHub repository:
https://github.com/codingwithshawnyt/matplotlib-visualizer
"""

setup(name='matplotlib_visualizer',
      version='1.0',
      description='Introducing a GPT-powered solution designed to revolutionize data visualization without the need for coding!',
      long_description=LONG_DESC,
      author='Shawn Ray',
      author_email='shawnray5699@gmail.com',
      url='https://github.com/codingwithshawnyt/matplotlib-visualizer',
      packages=find_packages(),
      keywords=['python', 'openai', 'matplotlib', 'data-visualization', 'LLM'],
      license='MIT'
      )