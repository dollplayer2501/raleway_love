#! /usr/bin/env python3

import os
import sys
import glob
import yaml
import json
import textwrap

if __name__ == "__main__":

    FILE__BASE_CONFIG = './_configuration/conf/raleway_love___base_config.conf'
    FILE__GRAPH_COLOR = './_configuration/json/raleway_love___graph_color.json'
    PATH__PARTS       = './_configuration/yaml/raleway_love__*.yaml'
    FILE__BASE_TEMPLATE = './_configuration/template/raleway_love___template.conf'
    PATH__OUTPUT = './conky/'
    PATH__PYTHON_SCRIPT = '/python/'


    with open(FILE__BASE_CONFIG) as fp:
        base_config = fp.read()

    with open(FILE__GRAPH_COLOR) as fp:
        graph_color = json.load(fp)

    with open(FILE__BASE_TEMPLATE) as fp:
        base_template = fp.read()


    for file in glob.glob(PATH__PARTS):
        with open(file) as fp:

            module_config = yaml.safe_load(fp)

            conky_config = textwrap.dedent(base_config).format(
                gap_x = module_config['gap_x'],
                gap_y = module_config['gap_y'],
                update_interval = module_config['update_interval'],
            ).strip()

            conky_text_pre = module_config['conky_text'].replace(
                '[graph_color_from]', graph_color['graph_color']['from']).replace(
                '[graph_color_to]', graph_color['graph_color']['to']).replace(
                '[python_full_path]', os.getcwd() + PATH__PYTHON_SCRIPT)

            conky_body_all = textwrap.dedent(base_template).format(
                comment = module_config['comment'],
                conky_config = conky_config,
                conky_text = conky_text_pre,
            ).strip()


            fp = open(PATH__OUTPUT + module_config['file_name'], 'w')
            fp.write(conky_body_all)
            fp.close()


    sys.exit()
