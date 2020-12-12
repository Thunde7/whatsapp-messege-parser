#########
#IMPORTS#
#########
import argparse

from file_utils import messages_generator_from_file, write_messages_to_json

######
#ARGS#
######
parser = argparse.ArgumentParser(
    description='Generate Pasta json from exported chat',
    usage='python gen_json.py INPUT OUTPUT [-d]'
)

parser.add_argument('src',
                    metavar='INPUT',
                    help='the exported file from whatsapp'
                    )

parser.add_argument('out',
                    metavar='OUTPUT',
                    help='file to write results to'
                    )

parser.add_argument(
    "-d",
    "--debug",
    required=False,
    action="store_true",
    help="DEBUG mode, Enables prints"
)

if __name__ == "__main__":
    args = parser.parse_args()

    pasta_set = set()
    lost = 0

    for message in messages_generator_from_file(args.src, args.debug):
        if message.is_readable():
            if message.is_copypasta():
                pasta_set.add(message.text)
        else:
            lost += 1

    if args.debug:
        print(
            f"we didn't read {lost} of the messagesand {len(pasta_set)} of them were copypastas")

    write_messages_to_json(args.out, pasta_set)
