from datetime import datetime as dt
import functools
import os


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
            try:
                with(open(log_file_path, "a")) as file:
                    file.write("Action {} executed on {} on {} \n".format(logged_action,
                                                                       path,
                                                                       dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            except FileNotFoundError as e:
                with(open(log_file_path, "w")) as file:
                    file.write("Action {} executed on {} on {} \n".format(logged_action,
                                                                          path,
                                                                          dt.now().strftime("%Y-%m-%d %H:%M:%S")))

            return func(path)
        return the_real_wrapper
    return wrapper_with_log_to_known_file


@wrapper_with_log_file("FILE_CREATE", r'C:\Users\mateu\Desktop\temp\file_create.txt')
def create_file(path):
    print("Creating file {}".format(path))
    open(path, "w+")


@wrapper_with_log_file("FILE_DELETE", r'C:\Users\mateu\Desktop\temp\file_delete.txt')
def delete_file(path):
    print("Deleting file {}".format(path))
    os.remove(path)