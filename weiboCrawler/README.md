# 2n version for weibo crawler

use session library.

## task breakdown:
+ login in: create and maintain headers/cookies to keep login; several link redirections are needed as the traffic monitor shows.
+ download: match the user with his/her user ID, and then goes to his/her album url  


login;
get album info and then album list;
create repository for each album if count > 0;

for album in album_list:
    get how many pages
    in each pages:
      get all urls of images from this [age];
      for each url inside an page:
        write down urls;
        download pics;
