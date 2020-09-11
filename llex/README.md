# llex - lua lex

llex takes a format similar to GNU FLEX, but uses lua code instead of c code (and lua regexes instead of posix regexes), and can be embedded in existing lua code to generate new lua code from string input.

It is limited to implementing line-based formats (in other words, it cannot, by itself, support multi-line patterns).

llex input files are separated into three seconds (which are separated by lines beginning with the string "%%"):

* the PRELUDE: this consists of lines beginning with tabs (which are added to the beginning of the lua output, before the lex function) and lines where a pattern name is separated from a pattern definition by a tab. Any lines not including tabs are invalid in this section
* the RULES: this consists of lines beginning with patterns (which may contain embedded pattern names in braces) followed by an optional variable name list for captures (which is separated from the pattern by a tab) and definition lines, which are lua code blocks beginning with tabs.
* the POSTSCRIPT: these are lines consisting of lua code, and are copied into the output after the rules. In this section, you may override the main() function or insert your own calls to llex()


