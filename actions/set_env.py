import os

def run(runner):
    variables = runner.get_inputs('variables')
    for line in variables.splitlines():
        key, value = line.split('=')
        os.environ[key] = value
