def markdown_to_blocks(markdown):
    blocks = []
    stripped_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        clean_block = block.strip()
        if clean_block != "":
            stripped_blocks.append(clean_block)
    return stripped_blocks