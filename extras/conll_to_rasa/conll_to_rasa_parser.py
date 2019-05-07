import os
import json
import argparse
from lazyme import per_section

def convert_data(args):
    out_data = {}
    in_data = list(per_section(open(args['data'])))
    
    with open(args['labels_data'], 'r') as f:
        labels = f.readlines()

    for i, d in enumerate(in_data):
        example = {}
        text = ''
        ent_text = ''
        prev_ent = None
        for n, token in enumerate(d):
            split = token.split("\t")
            if split[1] == 'O':
                if prev_ent != None:
                    text = text + '[{}]({})'.format(ent_text.strip(), prev_ent.strip()) + ' '
                    prev_ent = None
                    ent_text = ''
                text = text + split[0] + ' '
            else:
                ent_name = split[1].split('-')[1]
                # first entity encountered
                if prev_ent == ent_name or prev_ent is None:
                    prev_ent = ent_name
                    ent_text = ent_text + split[0] + ' '
                    if n == len(d) - 1:
                        # end of the sentence with an entity
                        text = text + '[{}]({})'.format(ent_text.strip(), prev_ent.strip()) + ' '
                else:
                    # another different entity encountered
                    text = text + '[{}]({})'.format(ent_text.strip(), prev_ent.strip()) + ' '
                    ent_text = ''
                    prev_ent = ent_name
                    ent_text = ent_text + split[0] + ' '
        

        if labels[i] in out_data:
            out_data[labels[i]].append(text.strip())
        else:
            out_data[labels[i]] = []
            out_data[labels[i]].append(text.strip())
    
    with open(args['output'], 'w') as f:
        for idx, k in enumerate(out_data.keys()):
            if idx == 0:
                f.write('## intent:'+str(k))
            else:
                f.write('\n## intent:'+str(k))
            for s in out_data[k]:
                f.write('- '+str(s)+'\n')


if __name__ == "__main__":
    fmt_class = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=fmt_class)

    group = parser.add_argument_group("Paramenters")
    group.add_argument("-d", "--data", type=str, required=True)
    group.add_argument("-l", "--labels-data", type=str, required=True)
    group.add_argument("-o", "--output", type=str, required=True)
    
    args = parser.parse_args()
    data = convert_data(vars(args)) 

