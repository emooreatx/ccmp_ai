# filename: autogen_ftp_integration.py
import os
import subprocess

# Install the autogen-agi library from the source repository
subprocess.run(["pip", "install", "git+https://github.com/autogen-agi/autogen-agi.git"], check=True)

from autogen_agi import Agent, AgentCouncil, GroupChat
from ftp_access_bitsavers import BitsaversFTP

# Define the RetrieveFilesAgent, which uses FTP to retrieve files
class RetrieveFilesAgent(Agent):
    def __init__(self, name, ftp_client):
        super().__init__(name)
        self.ftp_client = ftp_client

    def perform_task(self, product_name):
        # Search for files related to the product
        files = self.ftp_client.list_files()
        relevant_files = [f for f in files if product_name in f]
        for filename in relevant_files:
            # Download the file and process it
            file_path = self.ftp_client.download_file(filename)
            self.communicate(f"File {filename} downloaded to {file_path}.")

class CCPMAIAgent(Agent):
    def __init__(self, name):
        super().__init__(name)

    def answer_query(self, query):
        # Process the query and provide an answer
        # This is a placeholder for the actual processing logic
        self.communicate(f"Answering the query: {query}")

# Initialize the FTP client
ftp_client = BitsaversFTP('/pdf/')

# Create agents
retrieve_files_agent = RetrieveFilesAgent("RetrieveFiles", ftp_client)
ccpm_ai_agent = CCPMAIAgent("CCPMAI")

# Initialize the Agent Council and Group Chat
agent_council = AgentCouncil([retrieve_files_agent, ccpm_ai_agent])
group_chat = GroupChat(agent_council)

# Example usage
product_name = "SEL 810A"
query = "How long did operations take on the SEL 810A?"

# Perform the task
retrieve_files_agent.perform_task(product_name)
ccpm_ai_agent.answer_query(query)