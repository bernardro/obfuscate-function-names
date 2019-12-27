# obfuscate-function-names
A simple python program used to go beyond what uglify.js does by obfuscating function and variable names

If your aim is to make your javascript code inaccessible to script kiddies or just to thwart amateur hacking attempts 
you may find that after using uglify.js, your function names - usually very indicative of intended logic, are still very 
much available in browser developer tools. Clicking the *pretty print* button then pretty much reproduces your 
original code with varying degrees of success  

This python program obfuscates such artifacts before they ever get deployed to production and adds a layer of 
complexity that will discourage most script kiddies  

## How to use
Place your javascript project files in the `ORIGIFILES` folder. Only `*.js` files will be targeted  

Set up your development environment with three run configurations:  
1. find_identifiers - parses your code files recursively and extracts all the actionable (read obfuscatable) identifiers in your code  
2. pre_process_replacers - creates `before:after` (or `key:value` pairs if you like) maps showing how the names will change in `before:after` fashion  
 See `DATA/processed_replacers.json` for an example of this  
3. process_code_files - takes DATA/processed_replacers.json as input and runs it against your code files  

Run each of these stages in order. After each stage, check the output file of that stage in the `DATA` folder*  

Once you have run all three stages:  
- back up your unobfuscated project files  
- do a diff with your unprocessed project files and update them with the obfuscated content  
- your tests should all still run  
- your application should run in exactly the same way  
- your original function names should not be visible in your browser *developer tools*  

## Developer notes
*The separation of these three stages allows you to customize the output of each stage 
(which is the input to the next stage) so the logic and functionality of your code does 
not change in any way after obfuscation  

The `DATA` folder contains samples of input and output data