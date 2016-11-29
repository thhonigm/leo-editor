#@+leo-ver=5-thin
#@+node:ekr.20140723122936.18147: * @file importers/pascal.py
'''The @auto importer for the pascal language.'''
import re
import leo.core.leoGlobals as g
import leo.plugins.importers.linescanner as linescanner
Importer = linescanner.Importer
#@+others
#@+node:ekr.20161126171035.2: ** class Pascal_Importer
class Pascal_Importer(Importer):
    '''The importer for the pascal lanuage.'''

    def __init__(self, importCommands, atAuto):
        '''Pascal_Importer.__init__'''
        # Init the base class.
        Importer.__init__(self,
            importCommands,
            atAuto = atAuto,
            language = 'pascal',
            state_class = Pascal_ScanState,
            strict = False,
        )
        
    #@+others
    #@+node:ekr.20161126171035.4: *3* pascal_i.clean_headline
    pascal_clean_pattern = re.compile(r'^(function|procedure)\s+([\w_.]+)')

    def clean_headline(self, headline):
        '''Return a cleaned up headline s.'''
        m = self.pascal_clean_pattern.match(headline)
        if m:
            return '%s %s' % (m.group(1), m.group(2))
        else:
            return headline.strip()

    #@+node:ekr.20161127115120.1: *3* pascal_i.cut_stack
    def cut_stack(self, new_state, stack):
        '''Cut back the stack until stack[-1] matches new_state.'''
        trace = False and g.unitTesting
        if trace:
            g.trace(new_state)
            g.printList(stack)
        # This underflow could happen as the result of extra 'end' statement in user code.
        if len(stack) > 1:
            stack.pop()
        
        ###
        # assert len(stack) > 1 # Fail on entry.
        # while stack:
            # top_state = stack[-1].state
            # if new_state.level() < top_state.level():
                # if trace: g.trace('new_state < top_state', top_state)
                # assert len(stack) > 1, stack # <
                # stack.pop()
            # elif top_state.level() == new_state.level():
                # if trace: g.trace('new_state == top_state', top_state)
                # assert len(stack) > 1, stack # ==
                # # This is the only difference between i.cut_stack and python/cs.cut_stack
                # # stack.pop()
                # break
            # else:
                # # This happens often in valid Python programs.
                # if trace: g.trace('new_state > top_state', top_state)
                # break
        # # Restore the guard entry if necessary.
        # if len(stack) == 1:
            # if trace: g.trace('RECOPY:', stack)
            # stack.append(stack[-1])
        # assert len(stack) > 1 # Fail on exit.
        # if trace: g.trace('new target.p:', stack[-1].p.h)
    #@+node:ekr.20161127104208.1: *3* pascal_i.ends_block
    def ends_block(self, line, new_state, prev_state, stack):
        '''True if line ends a function or procedure.'''
        trace = False and g.unitTesting
        if prev_state.context:
            if trace: g.trace('in context', repr(prev_state.context))
            return False
        else:
            ls = line.lstrip()
            val = g.match_word(ls, 0, 'end')
            if trace and val: g.trace('  ', val, repr(line))
            return val
    #@+node:ekr.20161129024448.1: *3* pascal_i.get_new_dict (TO DO)
    #@@nobeautify

    def get_new_dict(self, context):
        '''
        Return a *general* state dictionary for the given context.
        Subclasses may override...
        '''
        trace = False and g.unitTesting
        comment, block1, block2 = self.single_comment, self.block1, self.block2
        
        def add_key(d, key, data):
            aList = d.get(key,[])
            aList.append(data)
            d[key] = aList

        if context:
            d = {
                # key    kind   pattern  ends?
                '\\':   [('len+1', '\\', None),],
                '"':    [('len', '"',    context == '"'),],
                "'":    [('len', "'",    context == "'"),],
            }
            if block1 and block2:
                add_key(d, block2[0], ('len', block1, True))
        else:
            # Not in any context.
            d = {
                # key    kind pattern new-ctx  deltas
                '\\':[('len+1', '\\', context, None),],
                '"':    [('len', '"', '"',     None),],
                "'":    [('len', "'", "'",     None),],
                '{':    [('len', '{', context, (1,0,0)),],
                '}':    [('len', '}', context, (-1,0,0)),],
                '(':    [('len', '(', context, (0,1,0)),],
                ')':    [('len', ')', context, (0,-1,0)),],
                '[':    [('len', '[', context, (0,0,1)),],
                ']':    [('len', ']', context, (0,0,-1)),],
            }
            if comment:
                add_key(d, comment[0], ('all', comment, '', None))
            if block1 and block2:
                add_key(d, block1[0], ('len', block1, block1, None))
        if trace: g.trace('created %s dict for %r state ' % (self.name, context))
        return d
    #@+node:ekr.20161127105609.1: *3* pascal_i.get_new_table (converted)
    #@@nobeautify

    def get_new_table(self, context):
        '''
        Return a **general** state table for the given context.
        
        This will do for some languages. Subclasses may override...
        '''
        trace = False and g.unitTesting
        
        def d(n):
            return 0 if context else n

        comment, block1, block2 = self.single_comment, self.block1, self.block2
            
        table = [
            # in-ctx: the next context when the pattern matches the line *and* the context.
            # out-ctx:the next context when the pattern matches the line *outside* any context.
            # deltas: the change to the indicated counts.  Always zero when inside a context.

            # kind,   pattern, out-ctx,  in-ctx, delta{}, delta(), delta[]
            ('len+1', '\\',    context,   context,  0,       0,       0),
            ('all',   '//',    '',        '',       0,       0,       0),
            ('len',   '"',     '"',       '',       0,       0,       0),
            ('len',   "'",     "'",       '',       0,       0,       0),
            ('len',   block1,  block1,    context,  0,       0,       0),
            ('end{',  block2,  context,   '',       0,       0,       0),
            # These interfere with comments.
            # ('len',   '{',     context,   context,  d(1),    0,       0),
            # ('len',   '}',     context,   context,  d(-1),   0,       0),
            # These are not needed.
            # ('len',   '(',     context,   context,  0,       d(1),    0),
            # ('len',   ')',     context,   context,  0,       d(-1),   0),
            # ('len',   '[',     context,   context,  0,       0,       d(1)),
            # ('len',   ']',     context,   context,  0,       0,       d(-1)),
        ]
        if trace:
            g.trace('created table for pascal state', repr(context))
            g.trace('comments', repr(comment), repr(block1), repr(block2))
        return table
    #@+node:ekr.20161126182009.1: *3* pascal_i.starts_block
    pascal_pattern_table = (
        re.compile(r'^(function|procedure)\s+([\w_.]+)\s*\((.*)\)\s*\;\s*\n'),
        re.compile(r'^(interface)\s*\n')
    )

    def starts_block(self, line, new_state, prev_state):
        '''True if the line starts a block.'''
        trace = False and g.unitTesting
        if prev_state.context:
            if trace: g.trace('in context', repr(prev_state.context))
            return False
        else:
            for pattern in self.pascal_pattern_table:
                m = pattern.match(line)
                if trace and m: g.trace('%5s %s' % (bool(m), repr(line)))
                if m: return True
            return False
    #@-others
#@+node:ekr.20161126171035.6: ** class class Pascal_ScanState
class Pascal_ScanState:
    '''A class representing the state of the pascal line-oriented scan.'''
    
    def __init__(self, d=None):
        '''Pascal_ScanState.__init__'''
        if d:
            prev = d.get('prev')
            self.context = prev.context
        else:
            self.context = ''

    def __repr__(self):
        '''Pascal_ScanState.__repr__'''
        return "Pascal_ScanState context: %r" % (self.context)

    __str__ = __repr__

    #@+others
    #@+node:ekr.20161126171035.7: *3* pascal_state.level
    def level(self):
        '''Pascal_ScanState.level.'''
        return 0 # Not used

    #@+node:ekr.20161126171035.8: *3* pascal_state.update
    def update(self, data):
        '''
        Pascal_ScanState.update

        Update the state using the 6-tuple returned by v2_scan_line.
        Return i = data[1]
        '''
        context, i, delta_c, delta_p, delta_s, bs_nl = data
        # All ScanState classes must have a context ivar.
        self.context = context
        return i
    #@-others
#@-others
importer_dict = {
    'class': Pascal_Importer,
    'extensions': ['.pas'],
}
#@@language python
#@@tabwidth -4


#@-leo
