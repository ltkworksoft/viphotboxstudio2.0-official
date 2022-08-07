import json
import random
import string
from urllib.parse import urljoin, urlparse
from flask import request, make_response, jsonify
from config import configurations
from datetime import datetime as dt
import pycountry


class Settings:
    def __init__(self):
        self.result = ''
        self.all_countries = []
        self.path = ''
        self.current_year = dt.now().year

    @staticmethod
    def select_environment_config(app, environment):
        if environment in configurations.keys():
            current_config = app.config.from_object(configurations[environment])
            return current_config
        raise ValueError("Your environment is not in basic configurations!")

    @staticmethod
    def is_safe_url(target):
        ref_url = urlparse(request.host_url)
        test_url = urlparse(urljoin(request.host_url, target))
        return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

    @staticmethod
    def allowed_files(app, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

    @staticmethod
    def select_request_json_mimetype():
        if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
            return True
        return False

    @staticmethod
    def make_json_response(**kwargs):
        return make_response(jsonify(kwargs))

    @staticmethod
    def cut_string_on_delimiter(data, delimiter):
        return data.split(delimiter)

    def cut_and_title_string(self, words, delimiter, titling=False):
        self.result = self.cut_string_on_delimiter(words, delimiter)
        if titling:
            return " ".join(self.result).title()
        return " ".join(self.result)

    @staticmethod
    def get_random_alphanumeric_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits) for _ in range(length)))
        return result_str

    def countries(self):
        for country in pycountry.countries:
            self.all_countries.append(country.name)
        return self.all_countries

    @staticmethod
    def find_country_numeric(country):
        num = pycountry.countries.get(name=country)
        return num.numeric

    @staticmethod
    def generate_slides(first_path, last_path, folder, image_name, descriptions, links, links_names):
        s = []
        for i in range(first_path, last_path):
            s.append((f'img/{folder}/{image_name}{i + 1}.jpg', descriptions[i], links[i], links_names[i]))
        return {
            'paths': s,
            'paths_length': len(s)
        }

    @staticmethod
    def generate_gallery_slides(first_path, last_path, folder, image_name):
        s = []
        for i in range(first_path, last_path):
            s.append(f'img/{folder}/{image_name}{i + 1}.jpg')
        return {
            'paths': s,
            'paths_length': len(s)
        }

    @staticmethod
    def get_length(data):
        return len(data)

    @staticmethod
    def get_from_json_file(filename):
        with open(filename, 'r') as openfile:
            return json.load(openfile)


settings = Settings()
