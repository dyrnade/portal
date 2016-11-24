# Social Sharing Platform #
## This project was for Comodo Programming Contest ## 
### Dependencies ###

- Django 1.9.4
- django-contrib-comments 1.6.2
- django-crispy-forms 1.6.0
- django-registration-redux 1.4
- djangorestframework 3.3.3
- Pillow 3.1.1

## Admin panel is an Android Application ##

It allows you to accept articles.
Django Rest Api is used for communication between django and android.

- Before building admin panel, below steps are need to be done
  - Open this with your favorite text editor. https://github.com/dyrnade/portal/blob/dev/SosyalYardimlasma/app/src/main/java/com/sosyalyardimlasma/adminpaneli/RESTClient.java
  - Change these fields with yours.
  - private static final String username = "admin_username";
  - private static final String password = "admin_password";
