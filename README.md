FeelingLucky
===================

FeelingLucky is Sublime Text Plugin which can open the related files of id or class of designation in html files.

![FeelingLucky](http://farm8.staticflickr.com/7293/8748074716_51763c0840_o.jpg)


## Installation

### Package Control
using [Sublime Package Control](http://wbond.net/sublime_packages/package_control), you can easily install the **FeelingLucky**.

````
Sublime Text 2 -> Preferences -> Package Control: Install Package
````  

### GitHub
Download the latest source from GitHub and copy the SublimeFeelingLucky folder to your Sublime Text `Packages` dir.

### Git
Clone the repository in your Sublime Text `Packages` dir

````
$ cd Packages
$ git clone git@github.com:azzip/SublimeFeelingLucky.git
````


## config.feelinglucky
`config.feelinglucky` is required.  
Designation of `.css`, `.sass`, `.js`, `.coffee` target file.

### Make
1. Context Menu `Make config.feelinglucky`  
2. Command short cut `super+ctrl+e`


### Example

````
{
    "css": [
        "style.css"
    ],
    "sass": [],
    "js": [
        "index.js"    
    ],    
    "coffee": []        
}
````

## Usage
Open Command Palette… `feeling lucky`

````
Tools -> Command Palette… -> feeling lucky
````  
or

use Default.sublime-keymap 

* css, sass : `ctrl+e`
* js, coffee : `ctrl+shift+e`
 



## Default.sublime-keymap

````
[
    { "keys": ["ctrl+e"], "command": "feeling_lucky_css" },
    { "keys": ["ctrl+shift+e"], "command": "feeling_lucky_js" },
    { "keys": ["super+ctrl+e"], "command": "make_config_dot_feeling_lucky" }
]
````

## What's New

v0.2.0 (2013/05/23) :  

* Open `.js`, `.coffee` files in new right panel.
