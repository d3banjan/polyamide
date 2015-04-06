from django.db import models

class joblisting(models.Model):
    hiring_position_text=models.CharField(max_length=50) #"Which postion are you hiring for?"
    hiring_industry_text=models.CharField(max_length=50) #"Which industry do you belong to?"
    posting_publish_date=models.DateTimeField("date published")
    hiring_description_md=models.CharField(max_length=2000) #"Please give a short description of the position you are hiring for:"
    hiring_primary_location=models.CharField(max_length=2000) #"Where would the applicant be expected to work at primarily?"
    posting_id=models.PositiveIntegerField() #"Job Posting ID:"
    
    
