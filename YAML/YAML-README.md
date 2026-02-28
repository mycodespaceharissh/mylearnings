# YAML Ain't Markup Language

* YAML is case sensitive.
* The files should have **.yaml** as the extension.
* YAML does not allow the use of tabs while creating YAML files; spaces are allowed instead.

## Basic Components of YAML File

* The basic components of YAML are described below −

## Conventional Block Format

* This block format uses hyphen+space to begin a new item in a specified list. Observe the example shown below −

<prev>
--- # Favorite movies
 - Casablanca 
 - North by Northwest 
 - The Man Who Wasn't There 
</prev>

### Inline Format

* Inline format is delimited with comma and space and the items are enclosed in JSON. Observe the example shown below −

<prev>
--- # Shopping list
   [milk, groceries, eggs, juice, fruits]
</prev>

### Folded Text

* Folded text converts newlines to spaces and removes the leading whitespace. Observe the example shown below −

<prev>
- {name: John Smith, age: 33}
- name: Mary Smith
  age: 27
</prev>

* The structure which follows all the basic conventions of YAML is shown below −

<prev>
men: [John Smith, Bill Jones]
women:
  - Mary Smith
  - Susan Williams
<prev>

## Synopsis of YAML Basic Elements

* The synopsis of YAML basic elements is given here: Comments in YAML begins with the (#) character. 
* Comments must be separated from other tokens by whitespaces. 
* Indentation of whitespace is used to denote structure. 
* Tabs are not included as indentation for YAML files. 
* List members are denoted by a leading hyphen (-).
* List members are enclosed in square brackets and separated by commas.
* Associative arrays are represented using colon ( : ) in the format of key value pair. They are enclosed in curly braces {}. 
* Multiple documents with single streams are separated with 3 hyphens (---). 
* Repeated nodes in each file are initially denoted by an ampersand (&) and by an asterisk (*) mark later. 
* YAML always requires colons and commas used as list separators followed by space with scalar values. 
* Nodes should be labelled with an exclamation mark (!) or double exclamation mark (!!), followed by string which can be expanded into an URI or URL.

## Indentation of YAML

* YAML does not include any mandatory spaces. Further, there is no need to be consistent. The valid YAML indentation is shown below − 

<prev>
a:
   b:
      - c
      -  d
      - e
f:
      "ghi"
</prev>
