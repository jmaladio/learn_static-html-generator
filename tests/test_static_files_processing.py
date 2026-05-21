import unittest

from static_files_processing import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_ok(self):
        markdown_title = "# Title"
        new_title = extract_title(markdown_title)
        self.assertEqual(new_title, "Title")
    def test_extract_title_with_no_title(self):
        markdown_title = "Title"
        with self.assertRaises(ValueError):
            extract_title(markdown_title)
    def test_extract_title_with_line_break(self):
        markdown_title = "Not a title\n# Title"
        new_title = extract_title(markdown_title)
        self.assertEqual(new_title, "Title")
    def test_extract_title_with_subtitle_first(self):
        markdown_title = "## Subtitle\n# Title"
        new_title = extract_title(markdown_title)
        self.assertEqual(new_title, "Title")
    def test_extract_title_with_spaces(self):
        markdown_title = "#     Title    "
        new_title = extract_title(markdown_title)
        self.assertEqual(new_title, "Title")
