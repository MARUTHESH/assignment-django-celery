# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
from celery import shared_task
from .models import DataModel
from bs4 import BeautifulSoup
from django.core.mail import EmailMessage
import ast
import urllib.request
import os

logger = get_task_logger(__name__)


@shared_task
def fetch_and_trigger(object_id):
    '''
        Fetching the object from the DataModel
    '''
    data_objects = DataModel.objects.get(id=object_id)
    '''
        Convrting string list to list
    '''
    urls = ast.literal_eval(data_objects.website_urls)
    try:
        os.mkdir("html_folder")
    except FileExistsError as e:
        '''
        Resolves the exception when same folder already exsist
        '''
        os.system("rm -rf html_folder/")
        os.mkdir("html_folder")
    '''
        For each url in the urls list it would fetch the html content using
        BeautifulSoup  and strips http:// or https:// in the url and creates
        the file in write mode with striped of http:// because folder with //
        cannot be created and writes all the content retirved from BeautifulSoup
        and at last closes the file
    '''
    for url in urls:
        opener = urllib.request.FancyURLopener({})
        f = opener.open(url)
        content = f.read()
        soup = BeautifulSoup(content)
        prettify_data = soup.prettify()
        url = str(url)
        filename = url.replace("https://", "")
        filename = url.replace("http://", "")
        filename = url.replace("/", "")
        file1 = open("html_folder/"+filename+".html", "w")
        file1.writelines(prettify_data)
        file1.close()
    '''
        zips and removes the zipped_folder and ordinary folder
    '''
    os.system("zip -r zipped_folder.zip html_folder")
    os.system("rm -rf html_folder/")
    '''
     At last triggers the email with zipped file
    '''
    email_object = EmailMessage(subject='assignment',
                                from_email="develop.t123@gmail.com",
                                to=[data_objects.email])
    email_object.attach_file('zipped_folder.zip')
    email_object.send()
    os.system("rm -rf zipped_folder.zip")
    return object_id
