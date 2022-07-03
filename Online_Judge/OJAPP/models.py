from tkinter import CASCADE
from django.db import models
from django.forms import CharField, DateTimeField
from numpy import maximum
from paramiko import AutoAddPolicy
from requests import delete

class Problems(models.Model):
    statement = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=10)

class Solution(models.Model):
    verdict = models.CharField(max_length=100)
    submittedAt = models.DateTimeField(auto_add_now=True)
    submittedCode = models.CharField(max_length=10000)
    problems = models.ForeignKey(Problems)

class TestCases(models.Model):
    input = models.CharField(max_length=1000)
    output = models.CharField(max_length=10000)
    problems = models.ForeignKey(Problems, on_delete = models.CASCADE)
