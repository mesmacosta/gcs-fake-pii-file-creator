from .csv_creator import CSVCreator
from .dataframe_creator import DFCreator
from .gcs_storage_client_helper import StorageClientHelper
from .uuid_helper import UUIDHelper


class GCSFakeFileCreator:

    def __init__(self,
                 project_id,
                 file_name,
                 num_rows=None,
                 num_cols=None,
                 obfuscate_col_names=None):
        self.__project_id = project_id
        self.__file_name = file_name        
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__obfuscate_col_names = obfuscate_col_names

    def create(self):
        print('Creating dataframe...')
        df_name, dataframe = DFCreator(self.__file_name,
                                       self.__num_rows,
                                       self.__num_cols,
                                       self.__obfuscate_col_names).create()
        print('Dataframe created')
        csv_name, csv_path = CSVCreator.create(df_name, dataframe)
        print('CSV created')
        storage_helper = StorageClientHelper(project_id=self.__project_id)
        generated_id = UUIDHelper.generate_uuid()
        bucket_name = f'bucket_{generated_id}'
        storage_helper.create_bucket(bucket_name)
        storage_helper.upload_file(bucket_name, csv_path, csv_name)
        print('File created: {} on bucket: {}'.format(csv_name, bucket_name))
