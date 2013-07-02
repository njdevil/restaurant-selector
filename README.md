restaurant-selector
===================

Overview
========
This is a basic system for selecting which restaurant to choose based on reviews and comments from your friends.
System pulls a list of all restaurants ranked highest by the following calculation:

Vote_Yes / (Vote_Yes + Vote_No)

This will give the Percentage of YES votes compared to Total Votes.
This RANK value is saved to the DB as "rank_pct" for faster retrieval of Restaurant records.


Random
======
As an alternative to ranking by Rank_pct above, a "Random" option is also available.


Voting
======
Voting is available on each page and the page immediately refreshes the Votes, Rank and Ranking order after each Vote.


Restaurant Detail Page
======================
More details of each restaurant is available by clicking on the Restaurant Name from the main listing.  This page also displays Comments by users, identifies which Comments you have added, and allows logged-in users to post new Comments.


Administration
=============
Django Admin can be used, but created some ADD pages so you wont have to use it.
/add/restaurant -- to add a new restaurant
/add/user -- to add a new user
/add/group -- to add a new user group


Google Maps
===========
As part of the Add Restaurant module, the provided address is Geocoded through Google Maps.  If the address returns the top level of accuracy/precision, the address is permitted and saved into the DB.  If any other accuracy/precision is returned, the record will not save and will return an error.  Permitted addresses will have their Lat & Long saved to the DB.  This can be used in future releases for displaying a Google Map for each location.
