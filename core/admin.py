def activate(modeladmin, request, queryset):
    """Activates multiple rows at once
    """
    rows_updated = queryset.update(active=True)
    if rows_updated == 1:
        count_bit = "1 row was"
    else:
        count_bit = "%s rows were" % rows_updated
    modeladmin.message_user(request, "%s successfully activated." % count_bit)

def deactivate(modeladmin, request, queryset):
    """Dectivates multiple rows at once
    """
    rows_updated = queryset.update(active=False)
    if rows_updated == 1:
        count_bit = "1 row was"
    else:
        count_bit = "%s rows were"
    modeladmin.message_user(request, "%s successfully deactivated." % count_bit)
