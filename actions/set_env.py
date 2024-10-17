import os

def run():
    # variables = runner.get_inputs('variables')
    # for line in variables.splitlines():
        # key, value = line.split('=')
    with open(os.environ['GITHUB_ENV'],'a') as file:
        file.write(f"name=Avijit")

run()
        
      
