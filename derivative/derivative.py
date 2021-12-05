# This file was generated from derivative.peg
# See http://canopy.jcoglan.com/ for documentation.

from collections import defaultdict
import re


class TreeNode(object):
    def __init__(self, text, offset, elements):
        self.text = text
        self.offset = offset
        self.elements = elements

    def __iter__(self):
        for el in self.elements:
            yield el


class TreeNode1(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode1, self).__init__(text, offset, elements)
        self.M = elements[0]
        self.S = elements[2]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self.K1 = elements[0]
        self.K = elements[2]
        self.K2 = elements[2]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    REGEX_1 = re.compile('^[0-9]')

    def _read_S(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['S'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_M()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 == '+':
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"+"')
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_S()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode1(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'SNode1', (cls0, self._types.SNode1), {})
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_M()
            if address0 is not FAILURE:
                cls1 = type(address0)
                address0.__class__ = type(cls1.__name__ + 'SNode2', (cls1, self._types.SNode2), {})
            if address0 is FAILURE:
                self._offset = index1
        self._cache['S'][index0] = (address0, self._offset)
        return address0

    def _read_M(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['M'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_K()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk0, max0 = None, self._offset + 2
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 == 'x^':
                address2 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
                self._offset = self._offset + 2
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"x^"')
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_K()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode2(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'MonomNode', (cls0, self._types.MonomNode), {})
        self._cache['M'][index0] = (address0, self._offset)
        return address0

    def _read_K(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['K'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 is not None and Grammar.REGEX_1.search(chunk0):
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[0-9]')
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'KNode', (cls0, self._types.KNode), {})
        self._cache['K'][index0] = (address0, self._offset)
        return address0


class Parser(Grammar):
    def __init__(self, input, actions, types):
        self._input = input
        self._input_size = len(input)
        self._actions = actions
        self._types = types
        self._offset = 0
        self._cache = defaultdict(dict)
        self._failure = 0
        self._expected = []

    def parse(self):
        tree = self._read_S()
        if tree is not FAILURE and self._offset == self._input_size:
            return tree
        if not self._expected:
            self._failure = self._offset
            self._expected.append('<EOF>')
        raise ParseError(format_error(self._input, self._failure, self._expected))


def format_error(input, offset, expected):
    lines, line_no, position = input.split('\n'), 0, 0
    while position <= offset:
        position += len(lines[line_no]) + 1
        line_no += 1
    message, line = 'Line ' + str(line_no) + ': expected ' + ', '.join(expected) + '\n', lines[line_no - 1]
    message += line + '\n'
    position -= len(line) + 1
    message += ' ' * (offset - position)
    return message + '^'

def parse(input, actions=None, types=None):
    parser = Parser(input, actions, types)
    return parser.parse()
