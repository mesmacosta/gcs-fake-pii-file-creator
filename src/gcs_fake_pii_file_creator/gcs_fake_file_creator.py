import os
import concurrent.futures
from more_itertools import grouper

from .csv_creator import CSVCreator
from .dataframe_creator import DFCreator
from .gcs_storage_client_helper import StorageClientHelper
from .uuid_helper import UUIDHelper

THREAD_POOL_SIZE = 10


class GCSFakeFileCreator:

    def __init__(self,
                 project_id,
                 file_name,
                 num_rows=None,
                 num_cols=None,
                 num_files=None,
                 obfuscate_col_names=None):
        self.__project_id = project_id
        self.__file_name = file_name        
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__num_files = num_files
        self.__obfuscate_col_names = obfuscate_col_names
        self.__storage_helper = StorageClientHelper(project_id=self.__project_id)

    def create(self):
        generated_id = UUIDHelper.generate_uuid()
        bucket_name = f'bucket_{generated_id}'
        self.__storage_helper.create_bucket(bucket_name)

        chunks = int(self.__num_files / THREAD_POOL_SIZE)

        if chunks < 1:
            chunks = 1

        pool = concurrent.futures.ThreadPoolExecutor(THREAD_POOL_SIZE)
        futures = [pool.submit(self.__create_and_upload_random_file, group, bucket_name)
                   for group in grouper(range(self.__num_files), chunks)]
        concurrent.futures.wait(futures)

    def __create_and_upload_random_file(self, group, bucket_name):
        for i in group:
            try:
                print('Creating dataframe number:{}...'.format(i))
                df_name, dataframe = DFCreator(self.__file_name,
                                               self.__num_rows,
                                               self.__num_cols,
                                               self.__obfuscate_col_names).create()
                print('Dataframe created')
                csv_name, csv_path = CSVCreator.create(df_name, dataframe)
                print('CSV created')

                self.__storage_helper.upload_file(bucket_name, csv_path, csv_name)
                print('File created: {} on bucket: {}'.format(csv_name, bucket_name))
                os.remove(csv_path)
                print('File removed: {}'.format(csv_path))
            except:
                print('error with item {}'.format(i))


