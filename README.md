DoctorPi
========

#### Want to know which of your friends are sick? The Raspberry Pi can help!

This is an ongoing project for my [Introduction to Programming](http://silshack.github.io/fall2013/announcement/2013/08/07/welcome-to-560.html) course at UNC-Chapel Hill, where your Raspberry Pi will be able to tell you which of your friends are sick by using existing social media APIs. 

Feel free to add to or borrow any of the code you find in this repository, but it would be awesome if you mentioned the project in your code if you do borrow anything.


#### Purpose & Vision:

The purpose of this project is to give both new and experienced python programmers and Raspberry Pi users a fun way to expand on their skills. This project will show potential users how they can use simple code to instruct a piece of hardware to display specific information. The vision is to create some easy to use and hacker friendly code to create a program that can retrieve specific information and display it using a Raspberry Pi computer.

#### Milestones:

* Program connects to Twitter API
* Program searches the Twitter API home_timeline for friend's tweets
* Program prints friend's tweets to terminal
* Program scrapes Twitter data into a text file
* Program connects to term database
* Program returns a value associated with a user after crawling database
* Usernames of users fitting given criteria are displayed on the screen

#### What You Will Need:

For this project, we will be using Tweepy, a twitter library for python. To get the latest version of Tweepy, you can do a pip install like so:

    pip install tweepy

Or, you can clone the latest version from their Git repository and install it manually like so:

    git clone https://github.com/tweepy/tweepy.git
    python setup.py install

#### Ways for Others to Contribute Now or in the Future:

There are truly no limits to the ways in which people can contribute to this project. Using the tools described in the GETTING STARTED document, participation in the present and future outcomes of the DoctorPi can be easy. This project is a work in progress, which means the program can only do about half of what I hope it will do someday. So, please feel free to open new issues, make a pull request, or even just leave a comment! 
