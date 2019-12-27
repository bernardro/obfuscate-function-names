# obfuscate-function-names
A simple python program used to go beyond what uglify.js does by obfuscating function and variable names  

Place your javascript project files in the `ORIGIFILES` folder. Only `*.js` files will be targeted  

Set up your development environment with three run configurations  
- find_identifiers - parses your code files recursively and extracts all the actionable (read obfuscatable) identifiers in your code
- pre_process_replacers - creates `before:after` (or `key:value` pairs if you like) maps showing how the names will change in `before:after` fashion.  
 See `DATA/processed_replacers.json` for an example of this  
- process_code_files - takes DATA/processed_replacers.json as input and runs it against your code files

The separation of these three stages allows you to customize the output of each stage 
(which is the input to the next stage) so the logic and funcionality of your code does not change in any way after obfuscation.
