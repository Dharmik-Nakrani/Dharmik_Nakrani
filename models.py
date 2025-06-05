class Profile(models.Model):
    name = models.CharField(max_length=100)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    teams_url = models.URLField(blank=True, null=True)  # Changed from skype_url
    linkedin_url = models.URLField(blank=True, null=True)
    # ... other fields