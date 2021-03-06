import argparse
import logging

from .gcs_fake_file_creator import GCSFakeFileCreator


class GCSFakeFileCreatorCLI:

    @classmethod
    def run(cls):
        cls.__setup_logging()
        cls.__parse_args()

    @classmethod
    def __setup_logging(cls):
        logging.basicConfig(level=logging.INFO)

    @classmethod
    def __parse_args(cls):
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter
        )

        parser.add_argument('--project-id', help='Project id', required=True)
        parser.add_argument('--file-name',
                            help='If left blank a random name will be generated')        
        parser.add_argument('--num-rows',
                            help='If left blank a random number of rows will be generated')
        parser.add_argument('--num-cols',
                            help='If left blank a random number of columns will be generated (25 avaliable)')
        parser.add_argument('--num-files',
                            help='Number of files to be generated')
        parser.add_argument('--obfuscate-col-names',
                            help='If provided the column names will be obfuscated')

        parser.set_defaults(func=cls.__create_fake_file)

        args = parser.parse_args()
        args.func(args)

    @classmethod
    def __create_fake_file(cls, args):
        GCSFakeFileCreator(args.project_id,
                           args.file_name,
                           int(args.num_rows) if args.num_rows else None,
                           int(args.num_cols) if args.num_cols else None,
                           int(args.num_files) if args.num_files else 1,
                           args.obfuscate_col_names).create()
