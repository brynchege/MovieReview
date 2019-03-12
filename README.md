# MovieReview

Django Review
=============

A reusable Django app that lets users write reviews for any model

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install django-review


Add the ``moviereviews`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r"^addmovie/$",views.AddMovie, name="add_movie"),
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate


Usage
-----

The only step you'll have to take is to link to the movie review views. For example,
you created a ``movieinfo`` model, which should be reviewed by users.

Create a link and add some markup like:

.. code-block:: html

<li> <a href="/all_movie">All Movie</a></li>
    


get_reviews
+++++++++++

An assignment tag, that simply returns the reviews made for the given object.
An example usage would look like this:

.. code-block:: html

   <table>
        <thead>
        <th>Movie Name</th>
        <th>Details</th>
        <th>Review</th>
        </thead>
        <tbody>
        {% for movie in Movies %}
        <tr>
        <td>{{ movie.movie_name }}</td>
        <td>{{ movie.movie_detail }}</td>
        <td>{{ movie.movie_review }}</td>
        </tr>
        {% endfor %}
        </tbody>
        </table>


user_has_reviewed
+++++++++++++++++

To quickly check if a user has already reviewed the given object, you can use
the admin panel.



Settings
--------

Default behaviour:


* Users can post multiple reviews on one object
* Users can always update their posted reviews

# Coming Soon
--------

REVIEW_RATING_CHOICES
+++++++++++++++++++++

If you want other rating choices than 0-5, you can define a new tuple, like:

.. code-block:: python

    REVIEW_RATING_CHOICES = (
        ('1', 'bad'),
        ('2', 'average'),
        ('3', 'excellent'),
    )


REVIEW_ALLOW_ANONYMOUS
++++++++++++++++++++++

Allows anonymous review postings, if set to ``True``.


REVIEW_DELETION_SUCCESS_URL
+++++++++++++++++++++++++++

Name of the URL to redirect to after deleting a review instance. This could
be your review listing, for example.


REVIEW_UPDATE_SUCCESS_URL (optional)
++++++++++++++++++++++++++++++++++++

Default: DetailView of the instance.

Name of the URL to redirect to after creating/updating a review instance.
This could be your review listing, for example.

.. code-block:: python

    REVIEW_UPDATE_SUCCESS_URL = 'my_view_name'


Or you can also specify a function, that returns the full path. The function
then takes the review as parameter, so you can also access the reviewed item
like follows

.. code-block:: python

    REVIEW_UPDATE_SUCCESS_URL = lambda review: review.reviewed_item.get_absolute_url()



REVIEW_AVOID_MULTIPLE_REVIEWS
+++++++++++++++++++++++++++++

Avoids multiple reviews by one user, if set to ``True``.
Doesn't work with anonymous users.


REVIEW_PERMISSION_FUNCTION
++++++++++++++++++++++++++

Custom function to check the user's permission. Use a function and note that
the user and the reviewed item are only parameters.

.. code-block:: python

    REVIEW_PERMISSION_FUNCTION = lambda u, item: u.get_profile().has_permission(item)


REVIEW_UPDATE_PERIOD
++++++++++++++++++++

You can limit the period, in which a user is able to update old reviews.
Make sure to use minutes, e.g. 2880 for 48 hours.


REVIEW_CUSTOM_FORM
++++++++++++++++++

You can create your own review form (e.g. if you want to make use of the review
extra info). Just name it.


You can also use a custom form to add another content object to the review
instance.




Contribute
----------

If you want to contribute to this project,

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    
    # Implement your feature and tests
    
    # Send us a pull request for your feature branch
