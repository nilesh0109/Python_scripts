import os
from helpers import helpers

input_file = 'input/input.txt'
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = current_dir+'/output'

def main():
    with open(current_dir+'/'+input_file, 'r') as file:
        try:
            file_content = file.read()
            paths = file_content.split('\n')
        except IOError:
            print('Could not read file:', input_file)

    for url in paths:
        if(helpers.is_a_valid_image(url)):
            r = helpers.get_url_content(url)
            if r:
                filename = helpers.get_file_name(r.headers.get('content-disposition'), url)

                if filename:
                    try:
                        open(output_dir+'/'+filename, 'wb').write(r.content)
                    except :
                        print('Could not write file:', filename)

if __name__== "__main__":
  main()




