import csv
from typing import List, Dict
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders.csv_loader import CSVLoader

class CSVLoaderCustom:
    def __init__(self, path_file: str, delimiter: str = ",", quotechar: str = '"') -> None:
        self._path = path_file
        self._delimiter = delimiter
        self._quotechar = quotechar

    def loader(self) -> List[dict]:
        with open(self._path, mode='r', newline='') as file:
            loader = CSVLoader(
            file_path=self._path,
            csv_args={
                "delimiter": self._delimiter,
                "quotechar": self._quotechar,
            }
        )
            data = loader.load()
            return data 

    def split_load(self, chunk_size: int = 1000, chunk_overlap: int = 50):
        loader = self.loader()

        text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,)

        texts = text_splitter.split_documents(loader)
        return texts