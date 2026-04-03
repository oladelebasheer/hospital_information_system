def user_has_role(user, role_name):
    return user.groups.filter(name=role_name).exists()


def user_has_any_role(user, role_names):
    return user.groups.filter(name__in=role_names).exists()