# @title TI Class
import re
from defaults import DEFAULT_OUTDIR, DEFAULT_TAB


def is_comment(line):
    """
    Determine if a line is a comment
    """
    strip = line.strip()
    if len(strip) > 0 and strip[0] == '#':
        return True
    return False


def find_parentheses(s):
    """ Find and return the location of the matching parentheses pairs in s.

    Given a string, s, return a dictionary of start: end pairs giving the
    indexes of the matching parentheses in s. Suitable exceptions are
    raised if s contains unbalanced parentheses.

    """

    # The indexes of the open parentheses are stored in a stack, implemented
    # as a list

    stack = []
    parentheses_locs = {}
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            try:
                parentheses_locs[stack.pop()] = i
            except IndexError:
                raise IndexError('Too many close parentheses at index {}'
                                 .format(i))
    if stack:
        raise IndexError('No matching close parenthesis to open parenthesis '
                         'at index {}'.format(stack.pop()))
    return parentheses_locs


def is_blank(line):
    """
    Determine if a line is a comment
    """
    if line.strip() == '':
        return True
    return False


def is_hash(line):
    """
    Determine if a line is entirely hash. E.g. ###############
    Line must have at least one hash, but not no other characters
    :param line:
    :return:
    """
    import re
    if '#' in line:
        if re.sub('#', '', line).strip() == '':
            return True
    return False


def is_one_line_if_statement(line):
    """
        Some if statements happen on one line. E.g. IF(nCondition = 1, ProcessBreak, 0);
        This should be split into 3 lines to prevent indentation issues
        """
    if is_comment(line):
        return False
    else:
        # Assume line must start with IF, and entire IF() statement is in ONE line
        if line.lstrip().upper()[:2] == "IF":
            # Get only text inside IF parentheses
            paren_string = line[line.find("(") + 1:line.rfind(")")]
            # Remove inner parenthesis before counting commas
            while '(' in paren_string:
                paren_string = paren_string[:paren_string.find("(")] + paren_string[paren_string.rfind(")") + 1:]
            if paren_string.count(",") == 2:
                return True
    return False


def line_is_intro_or_conclusion(lst, line_idx):
    """
    Determine if a line comes before the prolog or after the epilog.
    """
    for i in range(len(lst)):
        start_idx = None
        end_idx = None
        if lst[i].startswith('572,'):
            start_idx = i
        elif lst[i].startswith('575,'):
            end_idx = i + int(lst[i][4:])
    if start_idx is None:
        return False
    elif line_idx < start_idx:
        return True
    elif end_idx is None:
        return False
    elif line_idx > end_idx:
        return True
    else:
        return False


def char_is_in_string(lst, line_idx, char_idx):
    """
    Determine if a given character (referenced by index) is part of a string. E
        E.g. logx = '\\s-grp-dbsvr6\sqlpackagedata$\TM1\Working\test.txt'; should return True for all \,
        but nResult = nNumerator \ nDenominator; should return False for \
    Since strings can go over multiple lines, look back to previous semicolon (if exists?) for start of strings
    """
    # Loop backward to find first semicolon
    idx = line_idx
    start_idx = 0
    while idx > 0:
        if ";" in lst[idx]:
            # Assume ";" is the last character of previous line
            start_idx = idx
            idx = 0
        elif idx == 1:
            start_idx = 0
        idx = idx - 1

    # Create single string from start_idx to line_idx, then append current line
    longstr = "".join(lst[start_idx:line_idx])
    longstr += (lst[line_idx][:char_idx + 1])

    # Count the number of occurrences of '
    count = longstr.count("'")
    if count % 2 == 0:
        return False
    return True


class TI(object):
    """
    A python class for tidying up TM1 TurboIntegrator Processes
    """
    text: object

    def __init__(self, text=None, infile="", tab=DEFAULT_TAB, outdir=DEFAULT_OUTDIR, outfile="out.ti"):
        """
        Initialize TI object in python
        """
        self.infile = infile
        self.text = text
        self.tab = tab
        self.outdir = outdir
        self.outfile = outfile
        self.isprofile = False

        if self.infile != "":
            with open(self.infile, 'r') as f:
                text_list = f.read().splitlines()
            self.text = text_list

        elif self.text != "":
            ### Note: In cases like nNumerator\nDenominator, a raw string must be passed here.
            # self.text = self.text.replace('\\', '\\ ')
            self.text = self.text.split('\n')

        if self.text is None:
            print("I think there's an error here. Make sure infile or text are populated...")

        if self.infile != "":
            self.outfile = self.infile.split('/')[-1]

    def set_tab(self, tab_str):
        self.tab = tab_str

    def set_outdir(self, outdir_str):
        self.outdir = outdir_str

    def set_outfile(self, outfile_str):
        self.outfile = outfile_str

    def capitalize_keywords(self):
        """
        Capitalize 7 control keywords if found at the start of a line
        """
        from defaults import KEYWORDS
        out = []
        for line in self.text:
            if is_comment(line) is True:
                out.append(line)
            else:
                for keyword in KEYWORDS:
                    idx = line.upper().find(keyword)
                    if idx != -1:
                        if line.strip().upper().find(keyword) == 0:
                            line = line[:idx] + keyword + line[idx + len(keyword):]
                out.append(line)
        self.text = out

    def capitalize_functions(self):
        """
        Capitalize ~150 reserved TI function names
        """
        from defaults import FUNCTION_NAMES
        out = []
        for line in self.text:
            if is_comment(line) is True:
                out.append(line)
            else:
                for keyword in FUNCTION_NAMES:
                    idx = line.upper().find(keyword.upper())
                    # Keyword must be preceded by a space or '(' if not at start of line:
                    if idx != -1 and (line[idx - 1] == ' ' or line[idx - 1] == '(' or idx == 0):
                        # Keyword must also be followed by a space or '(' or ';'
                        following_char = str(line + ' ')[idx + len(keyword)]
                        if following_char == ' ' or following_char == '(' or following_char == ';':
                            line = line[:idx] + keyword + line[idx + len(keyword):]
                            # print(line, keyword, idx)
                    # Else keyword must be followed closely by '('
                    elif idx == 0 and '(' in line[idx + len(keyword):idx + len(keyword) + 3]:
                        line = keyword + line[idx + len(keyword):]
                    elif idx != -1:
                        # uncomment for testing
                        # print(line, keyword, idx)
                        pass
                out.append(line)
        self.text = out

    #
    # def separate_one_line_ifs(self):
    #     """
    #     Some if statements happen on one line. E.g. IF(nCondition = 1, ProcessBreak, 0);
    #     This should be split into 3 lines to prevent indentation issues
    #     """
    #     out = []
    #     line_idx = -1
    #     for line in self.text:
    #         line_idx += 1
    #         if is_comment(line) or line_is_intro_or_conclusion(self.text, line_idx):
    #             out.append(line)
    #         else:
    #             # Assume line must start with IF, and entire IF() statement is in ONE line
    #             if line.lstrip().upper()[:2] == "IF":
    #                 paren_string = line[line.find("(")+1:line.rfind(")")]
    #                 # Remove inner parenthesis before counting commas
    #                 #print('Hello', paren_string)
    #                 while '(' in paren_string:
    #                     paren_string = paren_string[:paren_string.find("(")] + paren_string[paren_string.rfind(")")+1:]
    #                     #print('Hello', paren_string)
    #                 if paren_string.count(",") == 2:
    #                     print(line, paren_string.split(','))
    #                     splt = paren_string.split(',')
    #
    #                     # Append If statement
    #                     out.append("IF(" + splt[0] + ");")
    #
    #                     # Append condition if true
    #                     if str(splt[1]).split() == '0':
    #                         out.append(" ")
    #                     else:
    #                         out.append(splt[1] + ";")
    #
    #                     #Append Else and Endif
    #                     if str(splt[2]).strip() == '0':
    #                         out.append('ENDIF;')
    #                     else:
    #                         out.append('ELSE;')
    #                         out.append(splt[2] + ';')
    #                         out.append('ENDIF;')
    #                 else:
    #                     out.append(line)
    #             else:
    #                 out.append(line)
    #     self.text = out

    def indent(self):
        """
        Add indentation
        """
        level = 0
        out = []
        tab = self.tab
        for line in self.text:
            line = line.lstrip()
            if line.startswith('END') or line.startswith('ENDIF') or line.startswith('ELSE'):
                level -= 1
            out.append(tab * level + line)
            if line.startswith('WHILE') or line.startswith('IF') or line.startswith('ELSEIF') or line.startswith(
                    'ELSE'):
                level += 1
            # Rare exception for one line if statements
            if is_one_line_if_statement(line):
                level -= 1
        self.text = out

    def remove_trailing_whitespace(self):
        self.text = [x.rstrip() for x in self.text]

    def space_operators(self):
        """
        Add spacing around operators. E.g. n=n+1; --> n = n + 1;
        """
        from defaults import OPERATORS
        out = []
        previous_lines = []
        line_idx = -1
        for line in self.text:
            line_idx += 1
            previous_lines.append(line)
            if is_comment(line) or line_is_intro_or_conclusion(self.text, line_idx):
                out.append(line)
            else:
                for op in OPERATORS:
                    # Need to escape + and * when using regex
                    if op == '+' or op == '*':
                        reop = '\\' + op
                    else:
                        reop = op
                    indices = [m.start() for m in re.finditer(reop, line)][::-1]
                    for idx in indices:
                        # Make sure operator doesn't occur in a string
                        if char_is_in_string(previous_lines, len(previous_lines) - 1, idx) is False:
                            # If previous or next character is another operator or '@', then skip this operator for this position
                            if idx == 0 or line[idx - 1] not in OPERATORS + ['@']:
                                if idx + len(op) == len(line) or line[idx + len(op)] not in OPERATORS + ['@']:
                                    # Apply spacing before operator
                                    if idx == 0:
                                        line = ' ' + op + line[idx + len(op):]
                                    elif line[idx - 1] != ' ':
                                        line = line[:idx] + ' ' + op + line[idx + len(op):]
                                        idx += 1
                                    # Apply spacing after operator
                                    if idx + len(op) < len(line):
                                        if line[idx + len(op)] != ' ':
                                            line = line[:idx] + op + ' ' + line[idx + len(op):]
                                    else:
                                        line = line[:idx] + op + ' '
                out.append(line)
        self.text = out

    def enforce_max_blank_lines(self):
        from defaults import MAX_CONSECUTIVE_BLANK_LINES
        out = []
        consecutive_blanks = 0
        for line in self.text:
            if is_blank(line):
                consecutive_blanks += 1
                if consecutive_blanks <= MAX_CONSECUTIVE_BLANK_LINES:
                    out.append(line)
            else:
                consecutive_blanks = 0
                out.append(line)
        self.text = out

    def remove_hash_lines(self):
        # Only remove hash lines if there are more than one in a row.
        out = []
        for line in self.text:
            if is_hash(line) is True:
                consec += 1
                if consec < 2:
                    out.append(line)
            else:
                consec = 0
                out.append(line)
        self.text = out

    def space_back_slash(self):
        # Forward slashes cause issues in python, especially 12\n_months which creates a newline.
        out = []
        previous_lines = []
        line_idx = -1
        for line in self.text:
            line_idx += 1
            previous_lines.append(line)
            indices = [m.start() for m in re.finditer(r'\\', line)][::-1]
            for idx in indices:
                if line_is_intro_or_conclusion(previous_lines, len(previous_lines) - 1) is False:
                    if char_is_in_string(previous_lines, len(previous_lines) - 1, idx) is False:
                        if len(line) > idx:
                            line = line[:idx] + " \\ " + line[idx + 1:]
                        else:
                            line = line[:idx] + " \\ " + line[idx + 1:]
                        line = line.replace("  ", " ")
            out.append(line)
        self.text = out

    def remove_space_before_semicolon(self):
        out = []
        for line in self.text:
            while " ;" in line:
                line = line.replace(" ;", ";")
            out.append(line)
        self.text = out

    def update_pmde_lengths(self):
        """
        When working with a .pro file, the Prolog, metadata, data, and epilog tabs are preceded by <Code>,<Length of tab>.
        .pro files risk being invalid if this line is not updated.
        This process should not make any changes to TI code that is not in .pro format
        """
        pmde_lengths = {'intro': 0, 'prolog': 0, 'metadata': 0, 'data': 0, 'epilog': 0, 'outro': 0}
        stage = 'intro'
        for i in range(len(self.text)):
            if self.text[i][:4] == '572,':
                stage = 'prolog'
            elif self.text[i][:4] == '573,':
                stage = 'metadata'
            elif self.text[i][:4] == '574,':
                stage = 'data'
            elif self.text[i][:4] == '575,':
                stage = 'epilog'
            elif self.text[i][:4] == '576,':
                stage = 'outro'
            pmde_lengths[stage] += 1

        for i in range(len(self.text)):
            if self.text[i][:4] == '572,':
                self.text[i] = '572,' + str(pmde_lengths['prolog'] - 1)
            elif self.text[i][:4] == '573,':
                self.text[i] = '573,' + str(pmde_lengths['metadata'] - 1)
            elif self.text[i][:4] == '574,':
                self.text[i] = '574,' + str(pmde_lengths['data'] - 1)
            elif self.text[i][:4] == '575,':
                self.text[i] = '575,' + str(pmde_lengths['epilog'] - 1)
            pmde_lengths[stage] += 1

    def tidy(self):
        """
        Apply all TIdy processes
        """
        self.space_back_slash()
        self.capitalize_keywords()
        self.capitalize_functions()
        self.remove_trailing_whitespace()
        self.space_operators()
        self.indent()
        self.enforce_max_blank_lines()
        self.remove_space_before_semicolon()
        self.remove_hash_lines()
        self.update_pmde_lengths()

    def write_output(self):
        """
        Write text to outfile
        """
        with open(self.outdir + '/' + self.outfile, 'w') as f:
            for line in self.text:
                f.write("%s\n" % line)

    def print_output(self):
        """
        Print text
        """
        for line in self.text:
            print(line)
