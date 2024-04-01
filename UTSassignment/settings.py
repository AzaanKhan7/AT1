# settings.py

# Specification 1: User Authentication Settings
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/home/'

# Specification 2: Initial Category Selection Settings
FIRST_TIME_CATEGORY_CHOICES = [
    ('Sports', 'Sports'),
    ('Gaming', 'Gaming'),
    ('Art', 'Art'),
    ('Music', 'Music'),
]

# Specification 3: Category Selection Limits
MIN_CATEGORY_SELECTION = 1
MAX_CATEGORY_SELECTION = 4

# Specification 4: Grouping Settings
MAX_USERS_PER_GROUP = 5
MIN_USERS_PER_GROUP = 2

# Specification 5: Messaging Settings
# Assuming no additional settings needed in settings.py for regular messaging functionality

# Specification 6: Leave Group Button Settings
LEAVE_GROUP_BUTTON_LOCATION = ('top', 'left')

# Specification 7: Mute Notification Button Settings
MUTE_NOTIFICATION_BUTTON_LOCATION = ('top', 'left')
MUTE_NOTIFICATION_BUTTON_DISTANCE_FROM_LEAVE_GROUP = 10  # in pixels

# Specification 8: Close App Settings
MOBILE_CLOSE_APP_GESTURE = 'swipe up'
PC_CLOSE_APP_BUTTON_LOCATION = ('top', 'right')
PC_CLOSE_APP_BUTTON_COLOR = 'red'
