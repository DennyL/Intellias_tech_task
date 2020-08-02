class Helpers:

    @staticmethod
    def get_content_of_text_file(path_to_text_file: str) -> str:
        """
            Returns content of a text file
            :param :path_to_text_file :str
            :return: content of the text file :str
        """
        with open(path_to_text_file) as file:
            file_content = file.read() + '\n'
        return file_content
