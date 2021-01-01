# This code is based on the answer by Duncan Harris for the
# following stackoverflow question:
# https://stackoverflow.com/questions/6949395/is-there-a-way-to-get-a-line-number-from-an-elementtree-element


import sys

sys.modules['_elementtree'] = None
import xml.etree.ElementTree as ElementTree

class LineNumberingParser(ElementTree.XMLParser):
    def _start(self, *args, **kwargs):
        element = super(self.__class__, self)._start(*args, **kwargs)
        element.start_line_number = self.parser.CurrentLineNumber
        element.start_column_number = self.parser.CurrentColumnNumber
        element.start_byte_index = self.parser.CurrentByteIndex
        return element

    def _end(self, *args, **kwargs):
        element = super(self.__class__, self)._end(*args, **kwargs)
        element.end_line_number = self.parser.CurrentLineNumber
        element.end_column_number = self.parser.CurrentColumnNumber
        element.end_byte_index = self.parser.CurrentByteIndex
        return element


def create_element_tree(xml: str):
    return ElementTree.fromstring(xml,parser=LineNumberingParser())
