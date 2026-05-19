import unittest

from block_processing import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("## Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("""```
python\ncode\n
```"""
        ), BlockType.CODE)
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- Unordered list item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. Ordered list item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    def test_block_to_block_type_tricky(self):
        # heading with 7 # should not be a heading
        self.assertEqual(block_to_block_type("####### Heading"), BlockType.PARAGRAPH)
        # quote with one non-quote line should fail quote detection
        self.assertEqual(block_to_block_type("> Quote\n> Quote 2\nnot a quote"), BlockType.PARAGRAPH)
        # unordered list where one line misses the space should fail
        self.assertEqual(block_to_block_type("- list\n-list 2"), BlockType.PARAGRAPH)
        # ordered list with 1., 3. should fail
        self.assertEqual(block_to_block_type("1. list\n3. list 2"), BlockType.PARAGRAPH)
        # code block with missing closing fence should fail
        self.assertEqual(block_to_block_type("```\ncode\n"), BlockType.PARAGRAPH)