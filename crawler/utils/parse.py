import os
import random

env = os.environ


def parse_env(key_name, default_value):
    return env[key_name] if key_name in env else default_value


def parse_env_int(key_name, default_value):
    return int(env[key_name]) if key_name in env else default_value


def parse_env_boolean(key_name, default_value):
    if key_name not in env:
        return default_value

    value = env[key_name]
    if value == 'True' or value == 'true':
        return True
    if value == 'False' or value == 'false':
        return False
    return default_value


# generate data for post_fraud_model_request. Based on multipart request
def generate_post_fraud_model_request(model_version, is_active, file_name):
    boundary = str(random.randint(0, 10000))

    headers = {
        'Content-Type': 'multipart/form-data; boundary=%s' % boundary,
    }

    body = ''
    body += __generate_data_field(boundary, 'model_version', model_version)
    body += __generate_data_field(boundary, 'is_active', is_active)
    body += __generate_file_field(boundary, file_name)

    # the closing boundary
    body += "--%s--\r\n" % boundary

    return headers, body


def __generate_data_field(boundary, field_name, field_value):
    if field_value is None:
        return ''

    # separator boundary
    body = '--%s\r\n' % boundary

    body += 'Content-Disposition: form-data; name="%s"\r\n' % field_name
    body += '\r\n'
    body += '%s\r\n' % field_value

    return body


def __generate_file_field(boundary, file_name):
    if file_name is None:
        return ''

    # separator boundary
    body = '--%s\r\n' % boundary

    # data for file_name
    body += 'Content-Disposition: form-data; name="data"; filename="%s"\r\n' % file_name
    body += '\r\n'
    # now read file and add that data to the body
    with open(file_name, 'rb') as f:
        body += '%s\r\n' % f.read()

    return body
