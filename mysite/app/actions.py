from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.hashers import make_password, identify_hasher
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .ui import ContentTypeUI, UserUI, PermissionsUI, PermissionAddUI, UserAddUI, GroupsUI


class ContentTypeActionPack(ObjectPack):
    model = ContentType
    list_window = ContentTypeUI
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)
    add_to_menu = add_to_desktop = True


class UserActionPack(ObjectPack):
    model = User
    list_window = UserUI
    add_window = edit_window = UserAddUI
    add_to_menu = add_to_desktop = True

    columns = [
        {'header': 'username', 'data_index': 'username', 'searchable': True, 'sortable': True},
        {'header': 'email', 'data_index': 'email'},
        {'header': 'first name', 'data_index': 'first_name'},
        {'header': 'last name', 'data_index': 'last_name'},
        {'header': 'active', 'data_index': 'is_active'},
        {'header': 'staff', 'data_index': 'is_staff'},
        {'header': 'superuser', 'data_index': 'is_superuser'},
        {'header': 'date joined', 'data_index': 'date_joined'},
        {'header': 'date last login', 'data_index': 'last_login'},
        {'header': 'password', 'data_index': 'password'},
    ]

    def save_row(self, obj, create_new, request, context, *args, **kwargs):
        try:
            identify_hasher(obj.password)
        except ValueError:
            obj.password = make_password(obj.password)

        super().save_row(obj, create_new, request, context, *args, **kwargs)


# Пакет действий для прав доступа
class PermissionsActionPack(ObjectPack):
    model = Permission
    list_window = PermissionsUI
    add_window = edit_window = PermissionAddUI
    add_to_menu = add_to_desktop = True

    columns = [
        {'header': 'name', 'data_index': 'name', 'sortable': True},
        {'header': 'codename', 'data_index': 'codename', 'sortable': True},
        {'header': 'content_type', 'data_index': 'content_type', 'sortable': True}
    ]


class GroupsActionPack(ObjectPack):
    model = Group
    list_window = GroupsUI
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)
    add_to_menu = add_to_desktop = True

    columns = [
        {'header': 'name', 'data_index': 'name', 'sortable': True}
    ]
    