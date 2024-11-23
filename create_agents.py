from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor

from constants import  MAX_CONSECUTIVE_AUTO_REPLY, CODE_WRITER_SYSTEM_MESSAGE


def create_code_executor_agent(work_dir):
    """
    Creates and returns a code executor agent.
    """
    executor = LocalCommandLineCodeExecutor(work_dir=work_dir)
    return ConversableAgent(
        name="code_executor_agent",
        llm_config=False,
        code_execution_config={"executor": executor},
        human_input_mode="NEVER",
    )

def create_code_writer_agent(llm_config, max_auto_reply, system_message):
    """
    Creates and returns a code writer agent.
    """
    return ConversableAgent(
        "code_writer",
        system_message=system_message,
        llm_config={"config_list": llm_config['llm_config'], "seed": llm_config['seed']},
        code_execution_config=False,
        max_consecutive_auto_reply=max_auto_reply,
        human_input_mode="NEVER",
    )
