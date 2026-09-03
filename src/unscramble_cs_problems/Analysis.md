## Notation
Let $m$ be number of rows in the `texts.csv` file and 
let $n$ be the number of rows in the `calls.csv` file.

## Assumption
The project statement does not clearly indicate whether the time spent
by the given code on the loading of data from the text files should be 
included in the complexity analysis.
Given this ill-posedness of the problem I am assuming that the loading
of data from the text files is NOT included in the complexity analyses.

## Task0
#### A. Description:
This problem consists in printing two messages.
The first message requires data from the first row
of the file `texts.csv` whereas the second requires data from the 
last row of the file `calls.csv`.

#### B. Approach:
Information on the first text message and last call can be accessed using
sub-indexing on the lists `texts` and `calls`. 

#### C. Complexity Analysis:
**C.1. Algorithm**: constant time access to first row of `texts.csv`
and last row `calls.csv` - both are stored in variables loaded 
by the given code.

**C.2. Big O Notation**: $O(1)$ time complexity.

**C.3. Justification**: only fixed time operations that do not depend on the 
size of the inputs are needed in order to retrieve information needed 
to produce the message that is subsequently printed.

## Task1
#### A. Description:
In this problem it's required to find all the distinct telephone numbers
in the datasets `texts.csv` and `calls.csv`

#### B. Approach: 
Iterate through all the entries in the datasets.
Keep a set in which the unique telephone numbers are stored.
When processing each entry: update the set.
Note: set update is $O(1)$ due to set being a hash map.

#### C. Complexity Analysis:
**C.1. Algorithm**: iteration over $m + n$ entries in both data sets.

**C.2. Big O Notation**: $O(m+n)$

**C.3. Justification**: since $m + n$ entries have to be processed, and every entry takes $O(1)$
time to process (due to above-mentioned properties of the Python's `dict`), the final time complexity is $O(m+n)$

## Task2
#### A. Description:

#### B. Approach:

#### C. Complexity Analysis:
**C.1. Algorithm**:
**C.2. Big O Notation**:
**C.3. Justification**:

## Task3
#### A. Description:

#### B. Approach:

#### C. Complexity Analysis:
**C.1. Algorithm**:
**C.2. Big O Notation**:
**C.3. Justification**:


## Task4
#### A. Description:

#### B. Approach:

#### C. Complexity Analysis:
**C.1. Algorithm**:
**C.2. Big O Notation**:
**C.3. Justification**:
