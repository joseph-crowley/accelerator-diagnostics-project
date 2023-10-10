### Core App

1. **Initialization**: Ensure that `core` is in your `INSTALLED_APPS` list inside `settings.py`.

    ```python
    # DiRPi_Website/settings.py

    INSTALLED_APPS = [
        ...
        'core',
        ...
    ]
    ```

2. **Models**: Check if your `models` in `core/models/user.py` are as you expect. Don't forget to add them to `core/models/__init__.py`.

    ```python
    # core/models/__init__.py

    from .user import YourUserModel
    ```

    Then run:

    ```bash
    python manage.py makemigrations core
    python manage.py migrate
    ```

    NOTE: The setup.sh script needs to have `python manage.py makemigrations core` and `python manage.py migrate` run in order to work properly. If you are using a different app name, you will need to change the setup.sh script accordingly.

3. **Admin**: Make sure you have registered your models in `core/admin.py`.

    ```python
    # core/admin.py

    from django.contrib import admin
    from .models import YourUserModel

    admin.site.register(YourUserModel)
    ```

4. **Views**: Examine the views in `core/views/user_views.py`. Make sure you import them in `core/views/__init__.py`.

    ```python
    # core/views/__init__.py

    from .user_views import *
    ```

5. **Forms**: If you have forms, ensure they are correctly defined in `core/forms/user_registration_form.py`.

6. **URLs**: Check `core/urls.py`. Make sure it imports the views correctly and defines the URL patterns.

    ```python
    # core/urls.py

    from django.urls import path
    from .views import YourUserView

    urlpatterns = [
        path('some_path/', YourUserView.as_view(), name='some_name'),
    ]
    ```

    Don't forget to include `core/urls.py` in your project-level `urls.py`.

    ```python
    # DiRPi_Website/urls.py

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('core/', include('core.urls')),
        ...
    ]
    ```

7. **Templates**: Confirm that your templates like `core/templates/registration.html` are correct. Also add the `core/templates` directory to your project-level `settings.py`.
    ```python
    import os  # Make sure you have this import at the top of your file

    # ...

    TEMPLATES = [
        {
            # ...
            'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'core/templates')],  # Add your project's templates directory here
            # ...
        },
    ]
    ```


8. **Testing**: Once all of these are confirmed, try running your application.

    ```bash
    python manage.py runserver
    ```

9. **Debugging**: Look for errors in the terminal or Django debug page. Fix them accordingly.

Repeat this procedure for each new app, and you should end up with a fully functional project. I recommend sending this to chatGPT and explaining where you're at in the process, and what you don't understand or what's not working
