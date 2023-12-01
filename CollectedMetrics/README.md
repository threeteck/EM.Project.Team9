# CollectedMetrics

## Overview
The `CollectedMetrics` folder contains data files for various software repositories. Each subfolder represents a different repository, and the files within these subfolders contain metrics data at both class and method levels.

## Structure
- Each subfolder is named after a specific software repository.
- Within each subfolder, there are two CSV files:
  - `{RepositoryName}-Class.csv`: Contains class-level metrics for the respective repository.
  - `{RepositoryName}-Method.csv`: Contains method-level metrics for the respective repository.

For example, in the `AlbertMN_AssistantComputerControl` subfolder, you will find:
- `AlbertMN_AssistantComputerControl-Class.csv`
- `AlbertMN_AssistantComputerControl-Method.csv`

## Metrics

In total, we have collected 54 metrics, comprising 40 class-level metrics and 14 method-level metrics across 118 repositories. We included only those metrics that produced at least one non-zero result for either a class or method during testing of SourceMeter on one of the repositories. Here are the metrics and their descriptions. You can find more information about them in the [SourceMeter downloadable documantaion](https://sourcemeter.com/download). 

## **Class-level metrics:**
Abbr. | Name | Description
---|---|---
AD | API Documentation | Ratio of the number of documented public methods in the class +1 if the class itself is documented to the number of all public methods in the class + 1 (the class itself); however, the nested and anonymous classes are not included.
CBO | Coupling Between Object classes | Number of directly used other classes (e.g. by inheritance, function call, type reference, attribute reference). Classes using many other classes highly depend on their environment, so it is difficult to test or reuse them; furthermore, they are very sensitive to the changes in the system.
CC | Clone Coverage | Ratio of code covered by code duplications in the source code element to the size of the source code element, expressed in terms of the number of syntactic entities (statements, expressions, etc.).
CLOC | Comment Lines of Code | Number of comment and documentation code lines of the class, including its local methods and attributes; however, its nested and anonymous classes are not included.
DIT | Depth of Inheritance Tree | Length of the path that leads from the class to its farthest ancestor in the inheritance tree.
DLOC | Documentation Lines of Code | Number of documentation code lines of the class, including its local methods and attributes; however, its nested and anonymous classes are not included.
LCOM5 | Lack of Cohesion in Methods 5 | Number of functionalities of the class. One of the basic principles of object-oriented programming is encapsulation, meaning that attributes belonging together and the operations that use them should be organized into one class, and one class shall implement only one functionality, i.e. its attributes and methods should be coherent. This metric measures the lack of cohesion and computes into how many coherent classes the class could be split. It is calculated by taking a non-directed graph, where the nodes are the implemented local methods of the class and there is an edge between the two nodes if and only if a common (local or inherited) attribute or abstract method is used or a method invokes another. The value of the metric is the number of connected components in the graph except the ones that contain only constructors, destructors, getters or setters – as they are integral parts of the class.
LLDC | Logical Lines of Duplicated Code | Number of logical code lines (non-empty, non-comment lines) covered by code duplications in the source code element.
LLOC | Logical Lines of Code | Number of non-empty and non-comment code lines of the class, including the non-empty and non-comment lines of its local methods; however, its nested and anonymous classes are not included.
LOC | Lines of Code | Number of code lines of the class, including empty and comment lines, as well as its local methods; however, its nested and anonymous classes are not included.
NG | Number of Getters | Number of getter methods in the class, including the inherited ones; however, the getter methods of its nested and anonymous classes are not included. Methods that override abstract methods are not counted.
NLG | Number of Local Getters | Number of local (i.e. not inherited) getter methods in the class; however, the getter methods of its nested and anonymous classes are not included. Methods that override abstract methods are not counted.
NLM | Number of Local Methods | Number of local (i.e. not inherited) methods in the class; however, the methods of nested and anonymous classes are not included.
NLPM | Number of Local Public Methods | Number of local (i.e. not inherited) public methods in the class; however, the methods of nested and anonymous classes are not included.
NLS | Number of Local Setters | Number of local (i.e. not inherited) setter methods in the class; however, the setter methods of its nested and anonymous classes are not included. Methods that override abstract methods are not counted.
NM | Number of Methods | Number of methods in the class, including the inherited ones; however, the methods of its nested and anonymous classes are not included. Methods that override abstract methods are not counted.
NOA | Number of Ancestors | Number of classes and interfaces from which the class is directly or indirectly inherited.
NOC | Number of Children | Number of classes and interfaces which are directly derived from the class.
NOD | Number of Descendants | Number of classes and interfaces which are directly or indirectly derived from the class.
NOI | Number of Outgoing Invocations | Number of directly called methods of other classes, including method invocations from attribute initializations. If a method is invoked several times, it is counted only once.
NOP | Number of Parents | Number of classes and interfaces from which the class is directly inherited.
NOS | Number of Statements | Number of statements in the class; however, the statements of its nested and anonymous classes are not included.
NPM | Number of Public Methods | Number of public methods in the class, including the inherited ones; however, the public methods of nested and anonymous classes are not included. Methods that override abstract methods are not counted.
NS | Number of Setters | Number of setter methods in the class, including the inherited ones; however, the setter methods of its nested and anonymous classes are not included. Methods that override abstract methods are not counted.
PDA | Public Documented API | The number of the documented public methods of the class (+1 if the class itself is documented). When calculating the metrics the nested, anonymous or local classes found in the class and their methods are not calculated.
PUA | Public Undocumented API | The number of the undocumented public methods of the class (+1 if the class itself is undocumented). When calculating the metrics the nested, anonymous or local classes to be found in the class and their methods are not calculated.
RFC | Response set For Class | Number of local (i.e. not inherited) methods in the class (NLM) plus the number of directly invoked other methods by its methods or attribute initializations (NOI).
TCLOC | Total Comment Lines of Code | Number of comment and documentation code lines of the class, including its local methods and attributes, as well as its nested and anonymous classes.
TLLOC | Total Logical Lines of Code | Number of non-empty and non-comment code lines of the class, including the non-empty and non-comment code lines of its local methods, anonymous and nested classes.
TLOC | Total Lines of Code | Number of code lines of the class, including empty and comment lines, as well as its local methods, anonymous and nested classes.
TNG | Total Number of Getters | Number of getter methods in the class, including the inherited ones, as well as the inherited and local getter methods of its nested and anonymous classes.
TNLG | Total Number of Local Getters | Number of local (i.e. not inherited) getter methods in the class, including the local getter methods of its nested and anonymous classes.
TNLM | Total Number of Local Methods | Number of local (i.e. not inherited) methods in the class, including the local methods of its nested and anonymous classes.
TNLPM | Total Number of Local Public Methods | Number of local (i.e. not inherited) public methods in the class, including the local methods of its nested and anonymous classes.
TNLS | Total Number of Local Setters | Number of local (i.e. not inherited) setter methods in the class, including the local setter methods of its nested and anonymous classes.
TNM | Total Number of Methods | Number of methods in the class, including the inherited ones, as well as the inherited and local methods of its nested and anonymous classes. Methods that override abstract methods are not counted.
TNOS | Total Number of Statements | Number of statements in the class, including the statements of its nested and anonymous classes.
TNPM | Total Number of Public Methods | Number of public methods in the class, including the inherited ones, as well as the inherited and local public methods of its nested and anonymous classes.
TNS | Total Number of Setters | Number of setter methods in the class, including the inherited ones, as well as the inherited and local setter methods of its nested and anonymous classes.
WMC | Weighted Methods per Class | Complexity of the class expressed as the number of independent control flow paths in it. It is calculated as the sum of the McCabe’s Cyclomatic Complexity (McCC) values of its local methods.


## **Method-level metrics:**
Abbr. | Name | Description
---|---|---
CC | Clone Coverage | Ratio of code covered by code duplications in the source code element to the size of the source code element, expressed in terms of the number of syntactic entities (statements, expressions, etc.).
CLOC | Comment Lines of Code | Number of comment and documentation code lines of the method; however, its anonymous classes are not included.
DLOC | Documentation Lines of Code | Number of documentation code lines of the method.
LLDC | Logical Lines of Duplicated Code | Number of logical code lines (non-empty, non-comment lines) covered by code duplications in the source code element.
LLOC | Logical Lines of Code | Number of non-empty and non-comment code lines of the method; however, its anonymous classes are not included.
LOC | Lines of Code | Number of code lines of the method, including empty and comment lines; however, its anonymous classes are not included.
McCC | McCabe’s Cyclomatic Complexity | Complexity of the method expressed as the number of independent control flow paths in it. It represents a lower bound for the number of possible execution paths in the source code and at the same time it is an upper bound for the minimum number of test cases needed for achieving full branch test coverage. The value of the metric is initially 1 which increases by 1 for each occurence of the following instructions: if, for, foreach, while, do-while, case label (label that belongs to a switch instruction), catch (handler that belongs to a try block), conditional statement (?:) and conditional access operators (?. and ?[]). Moreover, logical and (\|\|), logical or ($||$) and null coalescing (??) expressions also add to the final value because their short-circuit evalutaion can cause branching depending on the first operand. The following language elements do not increase the value: else, try, switch, default label (default label that belongs to a switch instruction), finally.
NOI | Number of Outgoing Invocations | Number of directly called methods. If a method is invoked several times, it is counted only once.
NOS | Number of Statements | Number of statements in the method; however, the statements of its anonymous classes are not included.
NUMPAR | Number of Parameters | Number of the parameters of the method. The varargs parameter counts as one.
TCLOC | Total Comment Lines of Code | Number of comment and documentation code lines of the method, including its anonymous classes.
TLLOC | Total Logical Lines of Code | Number of non-empty and non-comment code lines of the method, including the non-empty and non-comment lines of its anonymous classes.
TLOC | Total Lines of Code | Number of code lines of the method, including empty and comment lines, as well as its anonymous classes.
TNOS | Total Number of Statements | Number of statements in the method, including the statements of its anonymous classes.