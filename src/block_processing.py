def markdown_to_blocks(markdown):

    return list((filter(lambda item: len(item) != 0,map((lambda block: block.strip()), markdown.split('\n\n')))))
