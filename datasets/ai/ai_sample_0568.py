import re

def contains_tensorflow_code(docstring):
    """
    Detects if the given docstring contains Tensorflow code
    :param docstring: The docstring to check
    :type docstring: string
    """
    # check if there are any TensorFlow import statements
    has_import_tf = False
    lines = docstring.split('\n')
    for line in lines:
        if re.search('^import\s+tensorflow', line):
            has_import_tf = True

    # check for the presence of any TensorFlow related strings
    has_tf_string = False
    for line in lines:
        if re.search('^tf.', line):
            has_tf_string = True

    return has_import_tf or has_tf_string