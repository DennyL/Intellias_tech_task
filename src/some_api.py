class SomeApi:

    @staticmethod
    def get_last_lines(path_to_file: str, number_of_lines: int) -> print:
        """
            Prints a required number of last lines from a plain text (.txt) file into the console, and in correct order.
            If number of lines passed as a parameter exceeds the number of lines in the file, prints the whole content.
            If the file is empty, prints a warning saying that the file is empty.
            If the file was not found at the path provided, prints a message that file not found.
            If the file is not a plain text file, prints a message that file cannot be read.
            In case the number_of_lines parameter is NOT a positive integer, prints a warning about incorrect input.
            :param path_to_file: str: a path to a target text file
            :param number_of_lines: int: a positive number of last lines from the file to print
        """
        try:
            if type(number_of_lines) == int and number_of_lines > 0:
                with open(path_to_file) as file:
                    lines = file.readlines()
                    target_lines = lines[-number_of_lines:]
                print(''.join(target_lines) if len(target_lines) > 0 else '*** Warning! The file is empty ***')
            else:
                print('*** Warning! Incorrect input ***')
        except FileNotFoundError:
            print('*** Error! File not found ***')
        except UnicodeDecodeError:
            print('*** Error! Cannot read the file ***')
