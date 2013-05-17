SublimeFeelingLucky
===================

SublimeFeelingLucky is Sublime Text Plugin which can open the related files of id or class of designation in html files.

![SublimeFeelingLucky](http://farm8.staticflickr.com/7293/8748074716_51763c0840_o.jpg)

## Installation

### Package Control

using [Sublime Package Control](http://wbond.net/sublime_packages/package_control), you can easily install the SublimeFeelingLucky.

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
Designation of `.css` and `.sass` target file.

### Make
1) Context Menu `Make config.feelinglucky`  
2) Command short cut `super+ctrl+e`


### Example

````
{
    "css": [
        "style.css"
    ],
    "sass": []
}

````

## Usage
Open Command Palette… `feeling lucky`

````
Tools -> Command Palette… -> feeling lucky
````  


## Default.sublime-keymap

````
[
	{ "keys": ["ctrl+e"], "command": "feeling_lucky" },
	{ "keys": ["super+ctrl+e"], "command": "make_config_dot_feeling_lucky" }
]
````

## License

MIT
