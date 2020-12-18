import yaml


def get_yaml_data(yaml_file):
    with open(yaml_file, 'rb') as f:
        file_data = f.read()
    # print(file_data)
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data
