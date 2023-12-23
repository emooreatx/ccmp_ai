# filename: autogen_agi_program.py

from ftplib import FTP
import os
import autogen_agi

# Assuming the following classes are available from the example files:
# - ModifiedGroupChat from example_modified_group_chat.py
# - ResearchAgent from example_research.py
# - RagAgent from example_rag.py
# These will be used to create the autonomous agents.

class BitsaversFTP:
    def __init__(self, directory):
        self.host = "bitsavers.informatik.uni-stuttgart.de"
        self.directory = directory
        self.user = "anonymous"
        self.passwd = "anonymous@"
        self.ftp = FTP(self.host)
        self.ftp.login(self.user, self.passwd)
        self.ftp.cwd(self.directory)

    def list_files(self):
        return self.ftp.nlst()

    def download_file(self, filename, local_path='.'):
        local_filename = os.path.join(local_path, filename)
        with open(local_filename, 'wb') as local_file:
            self.ftp.retrbinary('RETR ' + filename, local_file.write)
        return local_filename

# Initialize the FTP client for the specific directory related to SEL 810A
ftp_client = BitsaversFTP('/pdf/sel/810A/')

# List files and filter for relevant documents
files_list = ftp_client.list_files()
relevant_files = [file for file in files_list if 'SEL_810A' in file]

# Download the relevant files
for file in relevant_files:
    ftp_client.download_file(file)

# Initialize the autogen-agi agents
group_chat = autogen_agi.ModifiedGroupChat()
research_agent = autogen_agi.ResearchAgent()
rag_agent = autogen_agi.RagAgent()

# Function to handle the query using the autogen-agi agents
def handle_query(query):
    # Use the ResearchAgent to find relevant information
    research_results = research_agent.search(query)
    
    # Use the RagAgent to generate an answer based on the research
    answer = rag_agent.generate_answer(research_results)
    
    return answer

# Test the query
test_query = "How long does an operation take on the SEL 810A?"
answer = handle_query(test_query)
print(answer)