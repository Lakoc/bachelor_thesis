from argparse import ArgumentParser
from os import listdir
from os.path import isfile, join
from shutil import copyfile
from progress.bar import Bar
from helpers.load_files import load_transcription, load_vad_from_rttm, load_energy, load_texts, load_stats
from helpers.create_html_output import create_output
from outputs.statistics import get_stats
from helpers.dir_exist import create_if_not_exist, create_new_dir

if __name__ == '__main__':
    parser = ArgumentParser(
        description='Module for creating html statistic')
    parser.add_argument('src', type=str,
                        help='source path of wav, rttm and txt files')
    parser.add_argument('dest', type=str,
                        help='destination path for html files')
    parser.add_argument('template', type=str,
                        help='template for html file')
    parser.add_argument('stats', type=str,
                        help='path of file containing overall stats')
    parser.add_argument('text', type=str,
                        help='path of file containing texts')
    parser.add_argument('--stats_only', action="store_true",
                        help='boolean param for only stats creating')

    args = parser.parse_args()

    create_if_not_exist(args.dest)

    files = [f for f in listdir(args.src) if isfile(join(args.src, f)) and f.endswith(f'.rttm')]

    if len(files) < 1:
        raise FileNotFoundError(f'No rttm files found in {args.src}')

    if not args.stats_only:
        create_new_dir(join(args.dest, 'plots'), 'output plots')

    create_new_dir(join(args.dest, 'stats'), 'output stats')

    copyfile(f'{args.template.split(".html")[0]}.css', join(args.dest, 'style.css'))
    print(f'File {join(args.dest, "style.css")} was created')

    with Bar(f'Processing files in {args.src}', max=len(files)) as bar:
        for file in files:
            file_name = file.split('.rttm')[0]
            energy = load_energy(f'{join(args.src, file_name)}.energy')
            vad = load_vad_from_rttm(f'{join(args.src, file_name)}.rttm', energy.shape[0])
            transcription = load_transcription(f'{join(args.src, file_name)}.txt')
            texts = load_texts(args.text)
            stats = get_stats(vad, transcription, energy)
            stats_overall = load_stats(args.stats)
            create_output(stats, stats_overall, texts, args.template, args.dest, file_name, args.stats_only)
            bar.next()
