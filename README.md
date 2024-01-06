# Twitter Content Generator

## Description
This project automates the creation of Twitter content focused on Python programming topics. It uses OpenAI's GPT models and LangChain to generate engaging and concise tweets.

## Features
- Generates tweets based on Python programming topics.
- Utilizes OpenAI's GPT models for natural language processing.
- Customizable tweet format with support for hashtags.

## Installation

### Prerequisites
- Python
- An OpenAI API key
- A .txt file with headers : No., Topic, Explaination seperated with '|' dividers.

Example:
| No. | Topic                             | Explanation                                                                 |
|-----|-----------------------------------|-----------------------------------------------------------------------------|
| 1   | List Comprehensions               | How to use list comprehensions for more concise and readable code.          |

## Usage
1. Set up your `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```
2. Launch Jupyter Notebook:
```
python -m notebook
```

3. Open the `finalPrompt.ipynb` file in Jupyter Notebook.

4. Run the cells in the Jupyter Notebook to generate tweets.

## Configuration
You can edit the parameters within the notebook to customize the topics and formats of the tweets.

## Acknowledgments
- OpenAI for providing the GPT models.
- LangChain for their language modeling tools.