# crawling an user`s album from Weibo


## how to use:


## task breakdown:
+ login
+ the target users, switch to his/her album page
+ target the album
+ download the images
+ store images


## files description:
+ weibo.py: the main function
+ getPage.py: login and switch to the album page, decide which album for downloading; mainly use selenium
+ download.py: download the images from that album; mainly use urllib and bs4
