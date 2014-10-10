Requirements
============

A parent will log into the site and be able to register and pay for courses.
Children will be linked to parents, so parents can only buy courses for
registered children.  All children will have their own usernames for the
forums, but their parents will be able to see all the activity of the kid.

Parents should be able to buy multiple courses at once.

Payments should generate recipts and they should be stored, attached to the
account and emailed to the parent.

There should be a form that registered kids with a current server subscription
can use to vote for their next mod of the month.

For ongoing charges (server access), an invoice is generated and emailed to
the parent for the next billing cycle. The server generates a new whitelist
every day with the currently subscribed children, so if a parent doesn't pay
the invoice past the due date, the kid is automatically removed from the
whitelist. Need to find some way of passing this whitelist from the webserver
to the minecraft servers.

Courses should be the information about what the course is. There needs to be
a separate model for a running course - this has the dates and a relationship
to the location.

Courses should have different states that decide how they get displayed on the
navigation menu and in the courses list:

========= =========== ====
Status    Course List Menu
========= =========== ====
Running   Show        Show
Upcoming  Show        Show
Cancelled Hide        Hide
========= =========== ====

Courses the course page should be displayed in alphabetical order, but in two
groups: the courses with available RunningCourses, then the ones without. Each
course can have a small table with the available dates, or "this course will
return soon". Perhaps there should be a "Register Interest" button for courses
that are not running.

Staff Database
==============

Send out mass emails to staff: Running this course at this location with these
staff members with these students. An instance requires staff members, so we
can link who is working at a location for a course.

Staff need levels which decide access.

Approved staff should have posing access on the forums.

Username
Email
Password

Other emails
============

Automate the emailing of the welcome pack; these should be generated with
details about each location. Which means we need a location model as well.

We need a mailing list. God yes, we need a mailing list.

TO-DO list
==========

 * Accounts for Parents. Might need a way to link parent accounts so that
   multiple parents can access the same data.

 * Accounts for childers, which will be linked to the parent and created by
   the parent.

 * Add a proper full-blown cms
