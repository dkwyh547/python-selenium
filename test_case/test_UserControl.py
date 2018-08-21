from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from modules.modules_test import *
import unittest, time, re

class UserControl(unittest,TestCase):
    def setUp(self):
        self.HTS_http('http://39.106.240.149/')
        self.HTS_login(driver, 'wushixin', 'wushixin')
