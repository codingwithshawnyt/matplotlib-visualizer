## `matplotlib-visualizer`

Are you looking to streamline your data visualization process with [matplotlib](https://matplotlib.org)? Enter `matplotlib_ai` - a cutting-edge tool designed to simplify graph generation through natural language commands. By leveraging OpenAI's GPT API, innovative prompt engineering techniques, and employing few-shot learning capabilities, `matplotlib-visualizer` eliminates the need for manual `matplotlib` coding.

Imagine we have a dataset `data` featuring four distinct curves labeled `'a'`, `'b'`, `'c'`, and `'d'`:
```python
import numpy as np

data = {'a': [...],  # Specify the data for curve 'a'
        'b': [...],  # Specify the data for curve 'b'
        'c': [...],  # Specify the data for curve 'c'
        'd': [...]}  # Specify the data for curve 'd'
```

In a typical scenario where each curve needs to be plotted with specific styling and a customized title, conventional `matplotlib` code might look like this:
```python
import matplotlib.pyplot as plt

plt.plot(data['a'], linestyle='dashed', label='a')
plt.plot(data['b'], label='b')
plt.plot(data['c'], label='c')
plt.plot(data['d'], label='d')

plt.title('Custom Graph Title')
plt.legend()
plt.show()
```

On the other hand, leveraging the intuitive functionality of `matplotlib-visualizer`, accomplishing the same task is simplified:
```python
from matplotlib-visualizer.matplotlib-visualizer import matplotlib-visualizer

mpl_ai = matplotlib-visualizer("YOUR-OPENAI-API-KEY")
prompt = "Generate a graph for each curve in the dataset and title it 'Custom Graph Title'. Set curve 'a' as a dashed line."
generated_code = mpl_ai(prompt)
```

Inspect the code output through:
```python
print(generated_code)  # Display the GPT-generated code
```

Continually evolving, this project aims to enhance and expand its capabilities over time. Thank you for considering `matplotlib-visualizer` for your data visualization endeavors.
