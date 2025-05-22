from django.contrib.auth.decorators import user_passes_test

def solo_admin_roles(view_func):
    return user_passes_test(
        lambda u: u.is_authenticated and (u.is_superuser or u.has_perm("users.administrador_roles")),
        login_url='login',
        redirect_field_name=None
    )(view_func)