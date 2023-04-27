import re

user_agent_pattern = re.compile(r"\'User-Agent\',\s(\w*)", re.IGNORECASE)


def find_user_agent(filename_content_tuple):
    request_str = filename_content_tuple[1]

    user_agent_match = user_agent_pattern.search(request_str)

    if not user_agent_match:
        return ""

    user_agent = user_agent_match.group(1)
    return user_agent
