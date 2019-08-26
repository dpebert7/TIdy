#@title TI Class
from defaults import DEFAULT_OUTDIR, DEFAULT_TAB


def is_comment(line):
    """
    Determine if a line is a comment
    """
    strip = line.strip()
    if len(strip) > 0 and strip[0] == '#':
            return True
    return False


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
            self.text = self.text.replace('\\', '\\ ')
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
                    if idx != -1 and (line[idx-1] == ' ' or line[idx-1] == '('):
                        # Keyword must also be followed by a space or '('
                        following_char = line[idx + len(keyword)]
                        if following_char == ' ' or following_char == '(':
                            line = line[:idx] + keyword + line[idx + len(keyword):]
                            #print(line, keyword, idx)
                    # Else keyword must be followed closely by '('
                    elif idx == 0 and '(' in line[idx+len(keyword):idx+len(keyword)+3]:
                        line = keyword + line[idx + len(keyword):]
                    elif idx != -1:
                        pass
                        # uncomment for testing
                        #print(line, keyword, idx)
                out.append(line)
        self.text = out

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
            if line.startswith('WHILE') or line.startswith('IF') or line.startswith('ELSEIF') or line.startswith('ELSE'):
                level += 1
        self.text = out

    def remove_trailing_whitespace(self):
        self.text = [x.rstrip() for x in self.text]

    def space_operators(self):
        """
        Add spacing around operators. E.g. n=n+1; --> n = n + 1;
        """
        from defaults import OPERATORS
        out = []
        for line in self.text:
            if is_comment(line) is True:
                out.append(line)
            else:
                idx_list = [line.find(operator) for operator in OPERATORS]
                if sum(idx_list) != len(OPERATORS)*-1:
                    # Determine the correct operator
                    operator = ""
                    for i in range(len(OPERATORS)):
                        if idx_list[i] >= 0 and len(OPERATORS[i]) > len(operator):
                            operator = OPERATORS[i]
                    # Add spacing
                    idx = line.find(operator)
                    if idx != -1:
                        if line[idx + len(operator)] != ' ':
                            line = line[:idx] + operator + ' ' + line[idx + len(operator):]
                        if line[idx - 1] != ' ':
                            line = line[:idx] + ' ' + operator + line[idx + len(operator):]
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
                consec +=1
                if consec < 2:
                    out.append(line)
            else:
                consec = 0
                out.append(line)
        self.text = out

    def space_forward_slash(self):
        # Forward slashes cause issues in python, especially 12\n_months which creates a newline.
        out = []
        for line in self.text:
            if "\\" in line:
                line = line.replace("\\", " \\ ").replace("  ", " ")
                out.append(line)
            else:
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
        pmde_lengths = {'intro':0, 'prolog':0, 'metadata':0, 'data':0, 'epilog':0,'outro':0}
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
        self.space_forward_slash()
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