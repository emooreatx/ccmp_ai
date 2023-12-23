ccmp_ai uses the [Autogen-AGI Framework](https://github.com/microsoft/autogen-agi) on top of the [AutoGen framework](https://github.com/microsoft/autogen) for multi-agent conversational systems, towards the goal of discovering and utilizing information in repositories like bitsavers and VTDA to identify, recover, restore, repair, and demonstrate antique computers.


## Features
- **Enhanced Group Chat** 💬: Modified AutoGen classes for advanced group chat functionalities.
- **Agent Council** 🧙: Utilizes a council of agents for decision-making and speaker/actor selection. Based on a prompting technique explored in [this blog post](https://www.prompthub.us/blog/exploring-multi-persona-prompting-for-better-outputs).
- **Agent Team Awareness** 👥: Each agent is aware of its role and the roles of its peers, enhancing team-based problem-solving.
- **Advanced RAG** 📚: Built in Retrieval Augmented Generation (RAG) leveraging [RAG-fusion](https://towardsdatascience.com/forget-rag-the-future-is-rag-fusion-1147298d8ad1) and [llm re-ranking](https://blog.llamaindex.ai/using-llms-for-retrieval-and-reranking-23cf2d3a14b6) implemented via [llama_index](https://www.llamaindex.ai/).
- **Domain Discovery** 🔍: Built in domain discovery for knowledge outside of llm training data, currently bitsavers files.
- **Custom Agents** 🌟: A growing list of customized agents.

## WARNING ⚠️
This project leverages agents that have access to execute code locally. In addition it is based on the extended context window of gpt-4-turbo, which can be costly. Proceed at your own risk.

## Installation 🛠️
- clone the project:
```bash
git clone this repo
cd ccmp_ai
```
- (optional) create a conda environment:
```bash
conda create --name ccmp_ai python=3.11
conda activate ccmp_ai
```
- install dependencies
```bash
pip install -r requirements.txt
```
- add environment variables
  - copy `.env.example` to `.env` and fill in your values
    ```bash
    cp .env.example .env
    ```
  - copy `OAI_CONFIG_LIST.json.example` to `OAI_CONFIG_LIST.json` and fill in your OPENAI_API_KEY (this will most likely be needed for the example task)
    ```bash
    cp OAI_CONFIG_LIST.json.example OAI_CONFIG_LIST.json
    ```

All set!! 🎉✨
 
*NOTE*: 
- 🔴 visit [GitHub docs](https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to get your GitHub personal access token (required)
- ✅ visit https://serpapi.com/ to get your own API key (optional)
- ✅ visit https://programmablesearchengine.google.com/controlpanel/create to get your own API key (optional)
  
## Getting Started 🚀

```bash
python ccmp_ai.py
```
Wait until it finishes and it will be ready for you to ask a question.

- If you would first like to see an example of the research/domain discovery functionality:
```bash
python example_research.py
```
- If you want to see an example of the RAG functionality:
```bash
python example_rag.py
```

## TODO 📝

- [ ] Expand research and discovery to support more resources (such as vtda and archive.org)
- [ ] Support chat history overflow. This would reflect a MemGPT like system where the overflow history would stay summarized in the context with relevant overflow data pulled in (via RAG) as needed.


This license is inherited from autogen-agi, along with most of this readme

## License

MIT License

Copyright (c) 2023 MetaMind Solutions

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

