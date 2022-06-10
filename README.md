# Three Lions
Live deployment for the app here https://pp4-three-lions.herokuapp.com/

## About

The main objective of the Three Lions blog is to provide a user-friendly platform for people to discuss the England National Football team and their progress at the World Cup in 2022. The target end user is anyone and everyone who is interested in football, and who has a desire to follow and discuss the progress of England’s progress at the World Cup.

The blog provides functionality that allows the user to create a personal user account. This access thereby permits the user to interact with the forum platform and take part in discussions. End users are able to: 

	- Create posts.
	- Read posts.
	- Update posts - either their own, using the edit post option, or others’, by commenting and/or liking their posts.
	- Delete posts (only those which they have created themselves).

When users decide to create a post, they are prompted to provide a unique title of their choosing, their post content, and an excerpt to contextualise their post.

Once the post has been created, it will be sent for approval by the admin so as to prevent any unsuitable content being published on the forum. Once the posts have been approved, the user will be able to see them on the main post list page. Whilst the post is awaiting approval the user will be made aware by a message in their personal post page.

Three Lions is a Django framework app. The user's post data is stored in a database with PostgreSql, and the app is hosted on Heroku. The Django administration site was utilised to provide admin control in order to monitor forum content, as well as super user control of CRUD operations - including the ability to delete other users’ posts and comments.

Below is the link to the live website:


## Project Planning

The main goal for this project was to create a simple, user-friendly application that provides an accessible and interactive platform for people to discuss the England National Football Team, and their progress at the 2022 World Cup. Features include the ability for users to:

1. Create a personal user account.
	- Permission based activity allows for controlled interactivity with the forum, cultivating a more positive and user-friendly environment.

2. Create their own posts under the name of their user account.
	- The ability to create their own posts gives users a platform to express their views, and promotes healthy discussion.

3. Manage their posted content, with the option to edit and delete their posts.
	- The ability to edit and delete content gives users control over what they post.

4. Have access to read other users’ posts, and the ability to like and comment on these posts.
	- The ability to read and interact with other users’ posts creates a platform for discussion and the building blocks for a community.

5. Admin access to all forum content, controlling what is posted and the ability to delete content after publication.
	- Admin access allows content to be monitored, promoting a positive and safe environment.


The user stories for this project can be viewed [here](https://github.com/ConRdav/pp4-three-lions/projects/1)

## Project Management
I used GitHub's KanBan board to manage my workflow. [Three Lions Workflow](https://github.com/ConRdav/pp4-three-lions/projects/2)

## Features

### Welcome to Three Lions
Upon opening the app users are met with a page full of blog posts which even without an account they can view. 
IMAGE
The navbar for users without an account will have a sign up option allowing them to create their own account.
IMAGE

### Create A Blog Post
Once a user has their account set up they are then given more options on the navbar including 'create a post' and 'My posts'. 
IMAGE

### View Your Own Posts
When a user clicks on my posts they will have a similar screen as the home page but with only their posts on it and it will show if they have been approved by admin or if its pending.
IMAGE


### Delete Your Post
Users will need to confirm they wish to delete their post.
IMAGE


### Edit Your Post
Similar to create your own post form users can alter their previous posts and resubmit them for approval.
IMAGE

## Features left to implement


## Testing

### Automated Testing
I used Django to run automated testing however, sqlite3 was used as a local database to achieve this testing.

* I used Django TestCase to test my forms.py, urls.py and views.py within test_forms.py, test_urls.py and test_views.py.

#### test_forms.py
![testing forms.py](assets/images/test_forms.png)

#### test_urls.py
![testing urls.py](assets/images/test_urls.png)

#### test_views.py
![testing views.py](assets/images/test_views.png)

![Test result](assets/images/test_result.png)

* I attempted to test models.py but didn't have a great understanding of what to test for so decided to continue with manual testing for the rest of my app.

#### Django Coverage report
![Coverage report](assets/images/coverage_report.png)
* Using Django Coverage I realised that I hadn't covered enough testing with Django TestCase so manual testing was the next step to cover more testing.

### Manual Testing
* I used a KanBan board to help plan my manual testing and the points I needed to hit. [Here](https://github.com/ConRdav/pp4-three-lions/projects/3)
* Post Model blog posts were ordered by creation date, the blog title is returned and that the like count is returned. ![Post Model](assets/images/post_model.png).

* Comment model comments being ordered by creation date, and commenter name was returned along with the comment. ![Comment Model](assets/images/comment_model.png)

* The paths from url.py that I didn't cover in my automated tested which were users_post, edit_post and delete_post. These links are working.

* If the user isn't logged in they can't create,edit or delete a post and the user can't comment or like a post. The user can view a post and signup or login.![Unregistered User](assets/images/index_page.png) ![Unregistered User](assets/images/view_post_non_user.png) ![Unregistered User](assets/images/sign_up.png) ![Unregistered User](assets/images/sign_in.png)

* Logged in users can create, edit and delete their posts. Can comment and like on posts aswell as the ability to sign out.
![Logged in user](assets/images/index_page_user.png) ![Logged in user](assets/images/user_posts.png) ![Logged in user](assets/images/create_post.png) ![Logged in user](assets/images/edit_post.png) ![Logged in user](assets/images/logout.png) 

* Django Admin user can create, edit and delete posts from the Django admin panel, and can approve posts and comments from there too.
![Django Admin](assets/images/admin_index.png) ![Django Admin](assets/images/admin_comments.png) ![Django Admin](assets/images/admin_posts.png) ![Django Admin](assets/images/admin_add_post.png) ![Django Admin](assets/images/admin_add_comment.png) 

### Pep8 and Pylint Python Validators
* admin.py
![admin.py](assets/images/admin_py.png) 
* apps.py
![apps.py](assets/images/app_py.png) 
* forms.py 
![forms.py](assets/images/forms.png) 
* models.py 
![models.py](assets/images/models_py.png) 
* urls.py
![urls.py](assets/images/blog_url.png) 
* views.py 
![views.py](assets/images/views.png) 
* test_forms.py
![test_forms.py](assets/images/test_forms_pep8.png)
* test_urls.py 
![test_urls.py](assets/images/test_urls_pep8.png)
* test_views.py 
![test_views.py](assets/images/test_views_pep8.png)

### HTML Validation with Official W3C Validator
## base.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## index.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## create_post.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## edit_posts.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## post_detail.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## user_posts.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## django-all_auth's login.html edited for uniformity
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## django-all_auth's logout.html edited for uniformity
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## django-all_auth's signup.html edited for uniformity
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality

## LightHouse testing
![lighthouse1](assets/images/light_house1.png)
![lighthouse2](assets/images/light_house2.png)
![lighthouse3](assets/images/light_house3.png)
![lighthouse4](assets/images/light_house4.png)
![lighthouse5](assets/images/light_house5.png)

## Responsive testing
This app has been tested on mobile and tablet devices and is responsive.
![mobile1](assets/images/mobile_1.png)
![mobile2](assets/images/mobile_2.png)
![mobile3](assets/images/mobile_3.png)
![mobile4](assets/images/mobile_4.png)
![mobile5](assets/images/mobile_5.png)

## Bugs
- During the final deployment, I encountered a ProgrammingError relating to data in my database model.
	- To resolve this issue I leveraged the following stackoverflow thread: https://stackoverflow.com/questions/55117984/relation-does-not-exist-django-postgres.


## Existing Bugs

## Deployment

Deployment procedure (using Heroku):

1. First, after logging in to the Heroku dashboard, navigate to ‘Create New App’.
2. Give your project a unique name and choose an appropriate region, before creating your app.
3. Navigate to the Resources tab. Using the Add Ons section, add ‘Heroku Postgres’ as the app’s database.
4. Create an env.py file in your root directory and import the os library within this file.
5. Within your env.py file, create environment variables for your DATABASE_URL and SECRET_KEY. They should appear as follows:

	__*os.environ[“DATABASE_URL”] = “___”__

	__*os.environ[“SECRET_KEY”] = “___”__

6. Assign a value to your DATABASE_URL and SECRET_KEY and within the Heroku settings tab, create corresponding Config Variables.
7. In your settings.py file, assign your Heroku app as a localhost in your ALLOWED_HOSTS variable, using the appropriate format:

	__app_name.herokuapp.com__

8. After updating all of the necessary environment and configuration variables in the settings.py and env.py files, create a new file at the top level directory called ‘Procfile’. 
9. Within Procfile, add the following code:


	__web: guincorn PROJECT_NAME.wsgi__

10. Using the Command Line interface: add, commit and push your files. 
11. Finally, navigate to the Deployment tab in Heroku and deploy your branch manually, observing the build logs for errors.
12. Heroku will build the app for you. If the build is successful, Heroku will provide a link to your live app.





## Used Technologies
* HTML
* CSS
* Python
* JavaScript

## Frameworks and Libraries used
* Django with;
    * gunicorn
    * psycopg2
    * postgresql
    * AllAuth
    * Crispy Forms
    * colorfield
* Bootstrap



## Credits
- Code Institutes I Think Therefore I Blog was a guide to help set up the enviroment and the final deployment details. (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/)
- Codemy youtube page was used for the create_post method. (https://www.youtube.com/watch?v=CnaB4Nb0-R8)
- W3 Schools was used to help with bootstrap styling (https://www.w3schools.com/)
- Django docs helped with Django testing (https://docs.djangoproject.com/en/4.0/topics/testing/)

