import argparse
import re
import tarfile
from os import listdir
from os.path import isfile, join


def get_number(string):
    number = re.findall('(\d*)server\.log\.tar\.gz', string)
    if number:
        return int(number[0])
    else:
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Logs archiver")
    parser.add_argument('-i', '--infile', help="Name of logfile")
    parser.add_argument('-l', '--logdir', help="Directory where logs should be stored")
    args = parser.parse_args()

    default_number = 0

    if args.infile and args.logdir:
        logfiles = [f for f in listdir(args.logdir) if isfile(join(args.logdir, f))]
        archive_numbers = filter(lambda x: x is not None, map(get_number, logfiles))
        print archive_numbers
        if archive_numbers:
            new_number = max(archive_numbers) + 1
        else:
            new_number = default_number

        with tarfile.open(join(args.logdir, '%dserver.log.tar.gz' % new_number), "w:gz") as tar:
            tar.add(join(args.logdir, args.infile))

        with open(join(args.logdir, args.infile), 'w'):
            pass
