from .files import create_file, read_text_file

from langchain_core.tools import tool

create_file_tool = tool(create_file)
read_text_file_tool = tool(read_text_file)