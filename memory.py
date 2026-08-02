from db import get_memory

def build_memory():

    memories = get_memory()

    text = ""

    for memory in memories:

        text += f"""

Category:
{memory["category"]}

Information:
{memory["content"]}

"""

    return text