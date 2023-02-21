from django.http import Http404


def moderator_queryset(Model, user):
    if user.groups.filter(name='Moderator').exists():
        return Model.objects.all()

    try:
        return Model.objects.filter(user=user)
    except:
        raise Http404
