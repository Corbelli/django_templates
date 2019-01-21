import logging
from djangoanalytics.querytool import QueryTool
from .models import UserMeta

app_users = QueryTool('app_db', 'users')


def handler(get_user_hit):
    user, hit = get_user_hit()
    logging.info(hit.page_url_text)
    if user.user_id is not "":
        create_user_meta(user)
    pass


def create_user_meta(user):
    _id = user.user_id
    if UserMeta.objects.filter(user_id=_id).count() != 0:
        return
    app_user = app_users.select('*').where('user_id={}'.format(_id)).first()
    UserMeta.objects.create(user_id=app_user.user_id, name=app_user.name)
