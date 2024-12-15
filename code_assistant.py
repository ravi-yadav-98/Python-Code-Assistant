from pathlib import Path
import os
import pprint

from helper import load_config, load_prompt_from_file, save_chat_history
from constants import  MAX_CONSECUTIVE_AUTO_REPLY, CODE_WRITER_SYSTEM_MESSAGE
from create_agents import create_code_executor_agent, create_code_writer_agent

work_dir = Path("output")
work_dir.mkdir(exist_ok=True)

PROMPT_FILE = "user_prompt.txt"


#first Agent: Code Executor
code_executor_agent = create_code_executor_agent(work_dir=work_dir)

#seond Agent : Code writer

llm_config = load_config()
code_writer_agent = create_code_writer_agent(llm_config, MAX_CONSECUTIVE_AUTO_REPLY, CODE_WRITER_SYSTEM_MESSAGE)

prompt = load_prompt_from_file(PROMPT_FILE)

chat_result = code_executor_agent.initiate_chat(
    code_writer_agent, message=prompt
)

save_chat_history(chat_result, "log.txt")
pprint.pprint(chat_result)