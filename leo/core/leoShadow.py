# -*- coding: utf-8 -*-
#@+leo-ver=4-thin
#@+node:ekr.20080708094444.1:@thin leoShadow.py
#@@first

#@<< docstring >>
#@+node:ekr.20080708094444.78:<< docstring >>
'''
leoShadow.py


The shadow plugin allows you to use Leo with files which contain no
Leo comments, and still have information flow in both directions:
from the file into Leo, and from Leo into the file.

Private files contain sentinels: they live in the Leo-shadow subdirectory.
Public files contain no sentinels: they live in the parent (main) directory.

When Leo first reads an @shadow we create a file without sentinels in the regular directory.

The slightly hard thing to do is to pick up changes from the file without
sentinels, and put them into the file with sentinels.

We have two invariants:
1. We NEVER delete any sentinels.
2. As a slighly weaker condition, insertions which could be put either
   at the end of a node, or the beginning of the next node, should be put
   at the end of the node.
   The exception to this rule is the last node. Insertions should *always*
   be done within sentinels.

Settings:
- @string shadow_subdir (default: LeoFolder): name of the shadow directory.

- @string shadow_prefix (default: x): prefix of shadow files.
  This prefix allows the shadow file and the original file to have different names.
  This is useful for name-based tools like py.test.
'''
#@-node:ekr.20080708094444.78:<< docstring >>
#@nl
#@<< notes >>
#@+node:ekr.20080708094444.51:<< notes >>
#@+at
# 
# 1. Not sure if I should do something about read-only files. Are they a 
# problem? Should I check for them?
# 
# 2. Introduced openForRead and openForWrite. Both are introduced only as a 
# hook for the mod_shadow plugin, and default to
# the predefined open.
# 
# 3. Changed replaceTargetFileIfDifferent to return True if the file has been 
# replaced (otherwise, it still returns None).
# 
# 4. In gotoLineNumber: encapsulated
#                 theFile=open(fileName)
#                 lines = theFile.readlines()
#                 theFile.close()
# into a new method "gotoLinenumberOpen"
# 
# 5. Introduced a new function "applyLineNumberMappingIfAny" in 
# gotoLineNumber. The default implementation returns the argument.
#@-at
#@-node:ekr.20080708094444.51:<< notes >>
#@nl
#@<< imports >>
#@+node:ekr.20080708094444.52:<< imports >>
import leo.core.leoGlobals as g

import leo.core.leoAtFile as leoAtFile
import leo.core.leoCommands as leoCommands
import leo.core.leoImport as leoImport 

import ConfigParser 
import difflib
import os
import sys

# import shutil
# import sys

# plugins_path = g.os_path_join(g.app.loadDir,"..","plugins")
#@-node:ekr.20080708094444.52:<< imports >>
#@nl

# Terminology:
# 'push' create a file without sentinels from a file with sentinels.
# 'pull' propagate changes from a file without sentinels to a file with sentinels.

#@@language python
#@@tabwidth -4
#@@pagewidth 80

#@+others
#@+node:ekr.20080708094444.80:class pluginController
class shadowController:

   '''A class to manage @shadow files'''

   #@   @+others
   #@+node:ekr.20080708094444.79: ctor (shadowConroller)
   def __init__ (self,c):

       self.c = c

       self.print_copy_operations = False   # True: tell when files are copied.
       self.do_backups = False              # True: always make backups of each file.
       self.print_all = False               # True: print intermediate files.

       # Configuration
       self.shadow_subdir_default = 'LeoFolder'
       self.shadow_prefix_default = ''

   #@-node:ekr.20080708094444.79: ctor (shadowConroller)
   #@+node:ekr.20080708094444.36:propagate_changes & helpers
   def propagate_changes(self, old_private_file, old_public_file, marker_from_extension):

       '''Propagate the changes from the public file (without_sentinels)
       to the private file (with_sentinels)'''

       old_public_lines  = file(old_public_file).readlines()
       old_private_lines = file(old_private_file).readlines()

       new_private_lines = self.propagate_changed_lines(
           old_public_lines,
           old_private_lines,
           marker = marker_from_extension(old_public_file))

       written = self.write_if_changed(
           new_private_lines,
           targetfilename=old_private_file,
           sourcefilename=old_public_file)

       return written
   #@nonl
   #@+node:ekr.20080708094444.35:check_the_final_output & helper
   def check_the_final_output(self, new_private_lines, new_public_lines, sentinel_lines, marker):
       """
       Check that we produced a valid output.

       Input:
           new_targetlines:   the lines with sentinels which produce changed_lines_without_sentinels.
           sentinels:         new_targetlines should include all the lines from sentinels.

       checks:
           1. new_targetlines without sentinels must equal changed_lines_without_sentinels.
           2. the sentinel lines of new_targetlines must match 'sentinels'
       """
       new_public_lines2, new_sentinel_lines2 = self.separate_sentinels (new_private_lines, marker)

       ok = True
       if new_public_lines2 != new_public_lines:
           ok = False
           self.show_error(
               lines1 = new_public_lines2,
               lines2 = new_public_lines,
               message = "Not all changes made!",
               lines1_message = "new public lines (derived from new private lines)",
               lines2_message = "new public lines")

       if new_sentinel_lines2 != sentinel_lines:
           ok = False
           self.show_error(
               lines1 = sentinel_lines,
               lines2 = new_sentinel_lines2,
               message = "Sentinals not preserved!",
               lines1_message = "old sentinels",
               lines2_message = "new sentinels")

       if ok: g.trace("***success!")
   #@+node:ekr.20080708094444.33:show_error
   def show_error (self, lines1, lines2, message, lines1_message, lines2_message):

       def p(s):
           sys.stdout.write(s)
           f1.write(s)
       print "================================="
       print message
       print "================================="
       print lines1_message 
       print "---------------------------------"
       f1 = file("mod_shadow.tmp1", "w")
       for line in lines1:
           p(line)
       f1.close()
       print
       print "=================================="
       print lines2_message 
       print "---------------------------------"
       f1 = file("mod_shadow.tmp2", "w")
       for line in lines2:
           p(line)
       f1.close()
       print
       g.es("@shadow did not pick up the external changes correctly; please check shadow.tmp1 and shadow.tmp2 for differences")
       assert 0, "Malfunction of @shadow"
   #@-node:ekr.20080708094444.33:show_error
   #@-node:ekr.20080708094444.35:check_the_final_output & helper
   #@+node:ekr.20080708094444.37:copy_sentinels
   def copy_sentinels(self, reader_lines_with_sentinels, writer_new_sourcelines, marker, upto):

       """
       Copy the sentinels from reader_lines_with_sentinels to writer_new_sourcelines upto,
       but not including, upto.
       """

       while reader_lines_with_sentinels.index() < upto:
           line = reader_lines_with_sentinels.get()
           if self.is_sentinel(line, marker):
               writer_new_sourcelines.put(line)
   #@-node:ekr.20080708094444.37:copy_sentinels
   #@+node:ekr.20080708094444.38:propagate_changed_lines
   def propagate_changed_lines(self,
       new_public_lines,  # new_lines_without_sentinels
       old_private_lines, # old_lines_with_sentinels, 
       marker):

       '''Propagate changes from 'new_public_lines' to 'old_private_lines.

       We compare the old and new public lines, create diffs and
       propagate the diffs to the new private lines, copying sentinels as well.
       '''

       # new_lines_without_sentinels = new_public_lines
       # lines_with_sentinels = old_private_lines
       # old_lines_without_sentinels, mapping = self.strip_sentinels_with_map(lines_with_sentinels, marker)

       trace = True
       old_public_lines, mapping = self.strip_sentinels_with_map(old_private_lines,marker)
       #@    << init vars >>
       #@+node:ekr.20080708094444.40:<< init vars >>
       writer_new_sourcelines = sourcewriter()
       # collects the contents of the new file.

       reader_new_lines_without_sentinels = sourcereader(new_public_lines) # new_lines_without_sentinels)
           # Contains the changed source code.

       reader_old_lines_without_sentinels = sourcereader(old_public_lines) # old_lines_without_sentinels)
           # this is compared to reader_new_lines_without_sentinels to find out the changes.

       reader_lines_with_sentinels = sourcereader(old_private_lines) # lines_with_sentinels)
           # This is the file which is currently produced by Leo, with sentinels.

       # Check that all ranges returned by get_opcodes() are contiguous
       old_i2_old_lines, old_i2_modified_lines = -1,-1

       tag = i1_old_lines = i2_old_lines = i1_new_lines = i2_new_lines = None
       #@nonl
       #@-node:ekr.20080708094444.40:<< init vars >>
       #@nl
       #@    << define print_tags >>
       #@+node:ekr.20080708094444.39:<< define print_tags >>
       def print_tags(tag, i1_old_lines, i2_old_lines, i1_new_lines, i2_new_lines, message):

           sep1 = '=' * 10 ; sep2 = '-' * 20

           print ; print ; sep1, message,sep1

           print ; print (
               "tag:", tag,
               "  i1_old_lines:", i1_old_lines,
               "  i2_old_lines:", i2_old_lines,
               "  i1_new_lines:", i1_new_lines,
               "  i2_new_lines:", i2_new_lines)
           print ; print sep2

           table = (
               (reader_lines_with_sentinels,'old private lines'),
               (reader_old_lines_without_sentinels,'old public lines'),
               (reader_new_lines_without_sentinels,'new public lines'),
               (writer_new_sourcelines,'new private lines'),
           )

           for f,tag in table:
               f.dump(tag)
               print sep2


       #@-node:ekr.20080708094444.39:<< define print_tags >>
       #@nl

       sm = difflib.SequenceMatcher(None, old_public_lines, new_public_lines)

       # Loop invariant: all 3 readers are in synch.
       for tag, i1_old_lines, i2_old_lines, i1_new_lines, i2_new_lines in sm.get_opcodes():
           if trace: print_tags(tag, i1_old_lines, i2_old_lines, i1_new_lines, i2_new_lines, "After a new tag")
           if tag == 'insert' and mapping[i1_old_lines] >= len(lines_with_sentinels):
               pass
           else:
               self.copy_sentinels(reader_lines_with_sentinels, writer_new_sourcelines, marker, upto = mapping[i1_old_lines])
           if tag=='equal':
               #@            << handle 'equal' op >>
               #@+node:ekr.20080708094444.41:<< handle 'equal' op >>
               # Copy the lines from the leo file to the new sourcefile.
               # This loop copies both text and sentinels.
               while reader_lines_with_sentinels.index() <= mapping[i2_old_lines-1]:
                  line = reader_lines_with_sentinels.get()
                  writer_new_sourcelines.put(line)

               reader_new_lines_without_sentinels.sync(i2_new_lines)
               #@-node:ekr.20080708094444.41:<< handle 'equal' op >>
               #@nl
           elif tag=='replace':
               #@            << handle 'replace' op >>
               #@+node:ekr.20080708094444.42:<< handle 'replace' op >>
               while reader_new_lines_without_sentinels.index() < i2_new_lines:
                  line = reader_new_lines_without_sentinels.get()
                  writer_new_sourcelines.put(line)
               #@-node:ekr.20080708094444.42:<< handle 'replace' op >>
               #@nl
           elif tag=='delete':
               #@            << handle 'delete' op >>
               #@+node:ekr.20080708094444.43:<< handle 'delete' op >>
               # No copy operation for a deletion!
               pass
               #@-node:ekr.20080708094444.43:<< handle 'delete' op >>
               #@nl
           elif tag=='insert':
               #@            << handle 'insert' op >>
               #@+node:ekr.20080708094444.44:<< handle 'insert' op >>
               while reader_new_lines_without_sentinels.index()<i2_new_lines:
                  line = reader_new_lines_without_sentinels.get()
                  writer_new_sourcelines.put(line)

               #@-node:ekr.20080708094444.44:<< handle 'insert' op >>
               #@nl
           else: assert 0

       if trace: print_tags(tag, i1_old_lines, i2_old_lines, i1_new_lines, i2_new_lines, "Before final copy")
       self.copy_sentinels(
           reader_lines_with_sentinels,
           writer_new_sourcelines, marker,
           upto = reader_lines_with_sentinels.size())
       if trace: print_tags(tag, i1_old_lines, i2_old_lines, i1_new_lines, i2_new_lines, "At the end")
       result = writer_new_sourcelines.getlines()
       if 1:
           #@        << do final correctness check>>
           #@+node:ekr.20080708094444.45:<< do final correctness check >>
           t_sourcelines, t_sentinel_lines = self.separate_sentinels(
               writer_new_sourcelines.lines, marker)

           self.check_the_final_output(
               new_private_lines   = result,
               new_public_lines    = new_public_lines,
               sentinel_lines      = t_sentinel_lines,
               marker              = marker)
           #@-node:ekr.20080708094444.45:<< do final correctness check >>
           #@nl
       return result
   #@-node:ekr.20080708094444.38:propagate_changed_lines
   #@+node:ekr.20080708094444.34:strip_sentinels_with_map
   def strip_sentinels_with_map (self, lines, marker):
      '''
      Strip sentinels from 'lines', a list of lines with sentinels.

      Return (results,mapping) where results is the lines stripped of sentinels and
      mapping is a list that maps each line in results to its original line.
      '''
      mapping = [] ; results = []

      si, l = 0, len(lines)
      while si < l:
         sline = lines[si]
         if not self.is_sentinel(sline,marker):
            results.append(sline)
            mapping.append(si)
         si+=1

      # Create an additional mapping entry for convenience.
      # This simplifies the programming of the copy_sentinels function below.
      mapping.append(si)
      return results, mapping 
   #@-node:ekr.20080708094444.34:strip_sentinels_with_map
   #@+node:ekr.20080708094444.10:write_if_changed & helpers
   def write_if_changed (self,lines, sourcefilename, targetfilename):

       '''Write lines to targetfilename if targetfilename's contents are not lines.

       Set targetfilename's modification date to that of sourcefilename.

       Produces a message, if wanted, about the overwrite, and optionally
       keeps the overwritten file with a backup name.'''

       if not os.path.exists(targetfilename):
           copy = True 
       else:
           copy = lines != file(targetfilename).readlines()

       if copy:
           if print_copy_operations:
               print "Copying ", sourcefilename, " to ", targetfilename, " without sentinals"
           if self.do_backups and os.path.exists(targetfilename):
               self.make_backup_file(backupname,targetfilename)
           outfile = open(targetfilename, "w")
           for line in lines:
               outfile.write(line)
           outfile.close()
           self.copy_modification_time(sourcefilename, targetfilename)

       return copy 
   #@+node:ekr.20080708094444.8:copy_modification_time
   def copy_modification_time(self,sourcefilename,targetfilename):

       """
       Set the target file's modification time to
       that of the source file.
       """

       st = os.stat(sourcefilename)

       # To avoid pychecker/pylint complaints.
       utime = getattr(os,'utime')
       mtime = getattr(os,'mtime')

       if utime:
           utime(targetfilename, (st.st_atime, st.st_mtime))
       elif mtime:
           mtime(targetfilename, st.st_mtime)
       else:
           self.error("Neither os.utime nor os.mtime exists: can't set modification time.")
   #@-node:ekr.20080708094444.8:copy_modification_time
   #@+node:ekr.20080708094444.84:make_backup_file
   def make_backup_file (self,backupname,targetfilename):

       # Keep the old file around while we are debugging.
       count = 0
       backupname = "%s.~%s~"%(targetfilename,count)

       while os.path.exists(backupname):
          count+=1
          backupname = "%s.~%s~"%(targetfilename,count)

       os.rename(targetfilename,backupname)

       if self.print_copy_operations:
          print "backup file in ", backupname 
   #@-node:ekr.20080708094444.84:make_backup_file
   #@-node:ekr.20080708094444.10:write_if_changed & helpers
   #@-node:ekr.20080708094444.36:propagate_changes & helpers
   #@+node:ekr.20080708094444.83:test_propagate_changes
   # This is the heart of @shadow.

   def test_propagate_changes (self,
       old_private_lines,      # with_sentinels
       new_public_lines,       # without sentinels
       expected_private_lines, # with sentinels
       marker):

       '''Check that propagate changed lines changes 'before_private_lines' to
       'expected_private_lines' based on changes to 'changed_public_lines'.'''

       results = self.propagate_changed_lines(
           new_public_lines,   # new_lines_without_sentinels
           old_private_lines,  # lines_with_sentinels, 
           marker = marker)

       assert results == expected_private_lines, 'results: %s\n\nexpected_private_lines: %s' % (
           results,expected_private_lines)
   #@-node:ekr.20080708094444.83:test_propagate_changes
   #@+node:ekr.20080708094444.89:Utils...
   #@+node:ekr.20080708094444.27:copy_file_removing_sentinels (helper for at.replaceTargetFileIfDifferent)
   # Called by updated version of atFile.replaceTargetFileIfDifferent

   def copy_file_removing_sentinels (self,sourcefilename,targetfilename,marker_from_extension):

       '''Copies sourcefilename to targetfilename, removing sentinel lines.'''

       # outlines, sentinel_lines = self.read_file_separating_out_sentinels(sourcefilename, marker_from_extension)

       lines = file(sourcefilename).readlines()
       marker = marker_from_extension(sourcefilename)
       regular_lines, sentinel_lines = self.separate_sentinels(lines,marker)
       self.write_if_changed(regular_lines, sourcefilename, targetfilename)
   #@-node:ekr.20080708094444.27:copy_file_removing_sentinels (helper for at.replaceTargetFileIfDifferent)
   #@+node:ekr.20080708094444.9:default_marker_from_extension
   def default_marker_from_extension (self,filename):

       '''Guess the sentinel delimiter comment from the filename's extension.

       This allows testing independent of Leo.'''

       root, ext = os.path.splitext(filename)

       if ext=='.tmp':
           root, ext = os.path.splitext(root)

       if ext in('.h', '.c'):
           marker = "//@"
       elif ext in(".py", ".cfg", ".ksh", ".txt"):
           marker = '#@'
       elif ext in (".bat",):
           marker = "REM@"
       else:
           self.error("extension %s not known" % ext)
           marker = '#'

       return marker 
   #@-node:ekr.20080708094444.9:default_marker_from_extension
   #@+node:ekr.20080708094444.85:error
   def error (self,s):

       g.es_print(s,color='red')
   #@-node:ekr.20080708094444.85:error
   #@+node:ekr.20080708094444.11:is_sentinel
   def is_sentinel (self, line, marker):

      '''Return true if the line is a sentinel.'''

      return line.lstrip().startswith(marker)
   #@-node:ekr.20080708094444.11:is_sentinel
   #@+node:ekr.20080708094444.30:push_filter_mapping
   def push_filter_mapping (self,filelines, marker):
      """
      Given the lines of a file, filter out all
      Leo sentinels, and return a mapping:

         stripped file -> original file

      Filtering should be the same as
      separate_sentinels
      """

      mapping =[None]

      for linecount, line in enumerate(filelines):
         if not self.is_sentinel(line,marker):
            mapping.append(linecount+1)

      return mapping 
   #@-node:ekr.20080708094444.30:push_filter_mapping
   #@+node:ekr.20080708094444.28:read_file_separating_out_sentinels (not used)
   # def read_file_separating_out_sentinels (sourcefilename, marker_from_extension):
      # """
      # Removes sentinels from the lines of 'sourcefilename'.

      # Returns (regular_lines, sentinel_lines)
      # """

      # return self.separate_sentinels(file(sourcefilename).readlines(), marker_from_extension(sourcefilename))
   #@-node:ekr.20080708094444.28:read_file_separating_out_sentinels (not used)
   #@+node:ekr.20080708094444.29:separate_sentinels
   def separate_sentinels (self, lines, marker):

       '''
       Separates regular lines from sentinel lines.

       Returns (regular_lines, sentinel_lines)
       '''

       regular_lines = [] ; sentinel_lines = []

       for line in lines:
         if self.is_sentinel(line,marker):
            sentinel_lines.append(line)
         else:
            regular_lines.append(line)

       return regular_lines, sentinel_lines 
   #@-node:ekr.20080708094444.29:separate_sentinels
   #@-node:ekr.20080708094444.89:Utils...
   #@-others
#@-node:ekr.20080708094444.80:class pluginController
#@+node:ekr.20080708094444.12:class sourcereader
class sourcereader:
    """
    A simple class to read lines sequentially.

    The class keeps an internal index, so that each
    call to get returns the next line.

    Index returns the internal index, and sync
    advances the index to the the desired line.

    The index is the *next* line to be returned.

    The line numbering starts from 0.

    The code might be expanded inline once the plugin
    is considered stable
    """
    #@	@+others
    #@+node:ekr.20080708094444.13:__init__
    def __init__ (self, lines):
       self.lines = lines 
       self.length = len(self.lines)
       self.i = 0
    #@-node:ekr.20080708094444.13:__init__
    #@+node:ekr.20080708094444.14:index
    def index (self):
       return self.i 
    #@-node:ekr.20080708094444.14:index
    #@+node:ekr.20080708094444.15:get
    def get (self):
       result = self.lines[self.i]
       self.i+=1
       return result 
    #@-node:ekr.20080708094444.15:get
    #@+node:ekr.20080708094444.16:sync
    def sync (self,i):
       self.i = i 
    #@-node:ekr.20080708094444.16:sync
    #@+node:ekr.20080708094444.17:size
    def size (self):
       return self.length 
    #@-node:ekr.20080708094444.17:size
    #@+node:ekr.20080708094444.18:atEnd
    def atEnd (self):
       return self.index>=self.length 
    #@-node:ekr.20080708094444.18:atEnd
    #@+node:ekr.20080708094444.19:clone
    def clone(self):
        sr = sourcereader(self.lines)
        sr.i = self.i
        return sr
    #@nonl
    #@-node:ekr.20080708094444.19:clone
    #@+node:ekr.20080708094444.20:dump
    def dump(self, title):
        """
        Little dump routine for easy debugging
        """
        print title
        print self.i
        for i, line in enumerate(self.lines):
            if i == self.i:
                marker = "===>"
            else:
                marker = ""
            print "%s%s:%s" % (marker, i, line),
    #@nonl
    #@-node:ekr.20080708094444.20:dump
    #@-others
#@-node:ekr.20080708094444.12:class sourcereader
#@+node:ekr.20080708094444.21:class sourcewriter
class sourcewriter:
    """
    Convenience class to capture output to a file.

    Similar to class sourcereader.
    """
    #@	@+others
    #@+node:ekr.20080708094444.22:__init__
    def __init__ (self):

       self.i = 0
       self.lines =[]
    #@-node:ekr.20080708094444.22:__init__
    #@+node:ekr.20080708094444.23:put
    def put(self, line):

       self.lines.append(line)
       self.i+=1
    #@-node:ekr.20080708094444.23:put
    #@+node:ekr.20080708094444.24:index
    def index (self):

       return self.i 
    #@-node:ekr.20080708094444.24:index
    #@+node:ekr.20080708094444.25:getlines
    def getlines (self):

       return self.lines 
    #@-node:ekr.20080708094444.25:getlines
    #@+node:ekr.20080708094444.26:dump
    def dump(self, title):

        '''Dump lines for debugging.'''

        print title
        for i, line in enumerate(self.lines):
            print "%s:%s" % (i, line),
    #@-node:ekr.20080708094444.26:dump
    #@-others
#@-node:ekr.20080708094444.21:class sourcewriter
#@-others
#@-node:ekr.20080708094444.1:@thin leoShadow.py
#@-leo
