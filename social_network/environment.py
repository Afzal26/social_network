# ENVIRONMENT = 'local'
ENVIRONMENT = 'development'
# ENVIRONMENT = 'production'

SETTINGS_MODULE = 'social_network.settings.local'

if ENVIRONMENT == 'local':
    SETTINGS_MODULE = 'social_network.settings.local'
if ENVIRONMENT == 'development':
    SETTINGS_MODULE = 'social_network.settings.development'
if ENVIRONMENT == 'production':
    SETTINGS_MODULE = 'social_network.settings.production'
