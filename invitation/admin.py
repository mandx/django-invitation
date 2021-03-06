from django.contrib import admin
from invitation.models import InvitationKey, InvitationUser


class InvitationKeyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'from_user', 'recipient_email', 'date_invited',
                    'uses_left', 'key_expired', 'expiry_date',
                    'recipient_first_name', 'recipient_last_name',
                    'recipient_other', 'groups')
    filter_horizontal = ('registrant',)
    readonly_fields = ('registrant',)


class InvitationUserAdmin(admin.ModelAdmin):
    list_display = ('inviter', 'invites_remaining', 'invites_allocated',
                    'invites_sent', 'invites_accepted')

admin.site.register(InvitationKey, InvitationKeyAdmin)
admin.site.register(InvitationUser, InvitationUserAdmin)
