# filename: ccmp_ai.py
import os
from ftplib import FTP
from autogen_mods.modified_group_chat import ModifiedGroupChat, ModifiedGroupChatManager
from agents import (
    user_proxy,
    code_reviewer,
    agent_awareness_expert,
    python_expert,
    function_calling_agent,
    creative_solution_agent,
    first_principles_thinker_agent,
    project_manager_agent,
    task_history_review_agent,
    task_comprehension_agent,
    bitsavers_agent,
)

# Define AGENT_TEAM with the necessary agents
AGENT_TEAM = [
    user_proxy,
#    agent_awareness_expert,
    function_calling_agent,
#    creative_solution_agent,
#    first_principles_thinker_agent,
    project_manager_agent,
    task_history_review_agent,
    task_comprehension_agent,
    bitsavers_agent,
]


# Assuming dotenv has been loaded elsewhere and OPENAI_API_KEY is available in environment variables


config_list3 = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": os.environ["OPENAI_API_KEY"],
    }
]

config_list4 = [
    {
        "model": "gpt-4-1106-preview",
        "api_key": os.environ["OPENAI_API_KEY"],
    }
]

llm_config = {
    "seed": 42,
    "config_list": config_list4,
    "temperature": 0.1,
}




# Instantiate the ModifiedGroupChat
group_chat = ModifiedGroupChat(
    agents=AGENT_TEAM,
    messages=[],
    max_round=100,
    use_agent_council=True,
    inject_agent_council=True,
    continue_chat=False,
)

# Instantiate the ModifiedGroupChatManager with the group_chat instance
group_chat_manager = ModifiedGroupChatManager(groupchat=group_chat, llm_config=llm_config)

# Example query
prompt = """You are a network of agents who answer questions regarding antique computers by referencing files from bitsavers. 
The function calling agent can list the contents of directories and download files from the archives. 
The consult archive agent can reference the files to answer questions.
Do not attempt to read the file directly, instead please use consult_archive_bot
When looking for files, start by listing the contents of pdf. Remember file names without suffixes are likely directories.
consult archive bot first, in case we already have domain knowledge for that make and model of device.
QUERY: What type of grease was used on the IBM 029 Keypunch?
"""

# Start the chat with the bitsavers archive agent added
user_proxy.initiate_chat(
    group_chat_manager,
    clear_history=False,
    message=prompt,
)
