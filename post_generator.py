from llm_helper import llm


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag):
    length_str = get_length_str(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.
    
    1) Topic :{tag}
    2) length: {length}
    3) language: {language}
    If language is Hinglish then it means it is a mix of Hindi and English.
    The script for the generated post should be always be English.
    '''
    response = llm.invoke(prompt)
    return response.content
