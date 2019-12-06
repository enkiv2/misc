POX is a language inspired by Prolog and MUMPS.

POX is semi-functional. With the exception of global persistent variables (prefixed with a carat), all variables are scoped to the function.

Functions are declared and optionally defined. A function declaration consists of a determinacy notation (used for memoization), a function signature (function name followed by a list of args), and a set of constraints that determine correctness. A function definition is an expression that implements the function. If a definition is not provided, the simplest implementation that resolves the constraints in the declaration will be used; otherwise, the definition will be tested against those constraints at runtime (unless such checking is disabled in the interpreter).

Example code:

```
// line comment

/* bounded comment */

dec det fib(x) := x<=1, return 1; x>1, return x + fib(x-1). // fibonnacci is determinate. The generated implementation for this will be fast enough, so we do not need to define it.

dec nondet err(x) := isString(x). // err/1 can only be called on strings
def err(x) := print("Error: "), print(x), fail(). // this definition prints an error message and then forces backtracking
```

POX is processed in several passes:
* The first pass removes comments and resolves syntactic sugar like infix operators (simplepox).
* The second pass converts the new prefix-notation-format intermediate language into a forth-like suffix-notation stack language (reversepox) and builds in the standard library.
* The third pass converts this stack language into a binary format (packedpox).

Here is the above example code translated into simplepox:

```
dec(true, 'fib', ('x'), (_alt(_seq(_assertGTE(1,x), _return(1), _seq(_assertGT(x,1), _return(_add(x, fib(sub(x,1))))))))).

dec(false, 'err', ('x'), (isString(x))).
def(err, ('x'), (_seq(print("Error: "), _seq(print(x), fail())))).
```

Here it is in reversepox (without stdlib definitions):

```
:dect fib/1 '_ANONSEQ1/1' '_ANONSEQ2/1' _alt/2 ;;
:dect _ANONSEQ1/1 dup 1 _assertGTE/2 dup if 1 swap not if fail ;;
:dect _ANONSEQ2/1 dup 1 swap _assertGT/2 dup not if fail if _ANONSEQ3 ;;
:dect _ANONSEQ3/1 dup dup 1 swap sub fib add ;;

:decn err/1 isString/1 not if fail ;;
:defn err/1 _ANONSEQ4/1 ;;
:decn _ANONSEQ4/1 'Error: ' print _ANONSEQ5/1 ;;
:decn _ANONSEQ5/1 print fail ;;
```

Packedpox is a gzipped messagepack dictionary. Here is the JSON equivalent to that messagepack:
```
{
	"def":{
		"err/1":{"det":false, "code":["_ANONSEQ4/1"]}
	},
	"dec":{
		"fib/1":{"det":true, "mem":{}, "code":["'_ANONSEQ1/1'", "'_ANONSEQ2/1'", "_alt/2"]},
		"_ANONSEQ1/1":{"det":true, "mem":{}, "code":["dup", "1", "_assertGTE/2", "dup", "if", "1", "swap", "not", "if", "fail"]},
		"_ANONSEQ2/1":{"det":true, "mem":{}, "code":["dup", "1", "swap", "_assertGT/2", "dup", "not", "if", "fail", "if", "_ANONSEQ3"]},
		"_ANONSEQ3/1":{"det":true, "mem":{}, "code":["dup", "dup", "1", "swap", "sub", "fib", "add"]},
		"_ANONSEQ4/1":{"det":false, "code":["'Error: '", "print", "_ANONSEQ5/1"]},
		"_ANONSEQ5/1":{"det":false, "code":["print", "fail"]}
	},
	"persist":{}
}
```

The 'mem' attribute of definitions and declarations stores memoized values for determinate functions. The key is some hashed version of a serialized form of the args.


