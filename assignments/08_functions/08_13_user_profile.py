def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Build a profile using my name and three descriptive key-value pairs
my_profile = build_profile(
    'gemini', 
    'ai',
    role='personal collaborator',
    specialty='multimodal reasoning',
    origin='google'
)

print(my_profile)