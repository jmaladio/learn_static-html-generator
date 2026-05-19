import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def markdown_to_blocks(markdown):

    return list((filter(lambda item: len(item) != 0,map((lambda block: block.strip()), markdown.split('\n\n')))))

def block_to_block_type(markdown_block):
    lines = markdown_block.split('\n')
    if len(lines) == 1 and re.fullmatch(r"\#{1,6}\s.+", markdown_block):
        return BlockType.HEADING
    elif markdown_block.startswith("```\n") and markdown_block.endswith("\n```"):
        return BlockType.CODE
    elif all(line.startswith('>') for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST
    flag = False
    for i, line in enumerate(lines, start=1):
        if (line.startswith(f"{i}. ")):
            flag = True
        else:
            flag = False
            break
    if flag:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH