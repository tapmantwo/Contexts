class PluginInterface(object):
    """
    Interface for a plugin
    """
    def test_run_started(self):
        """Called at the beginning of a test run"""
    def test_run_ended(self):
        """Called at the end of a test run"""

    def suite_started(self, name):
        """Called at the start of a test module"""
    def suite_ended(self, name):
        """Called at the end of a test module"""

    def context_started(self, name, example):
        """Called when a test context begins its run"""
    def context_ended(self, name, example):
        """Called when a test context completes its run"""
    def context_errored(self, name, example, exception):
        """Called when a test context (not an assertion) throws an exception"""

    def assertion_started(self, name):
        """Called when an assertion begins"""
    def assertion_passed(self, name):
        """Called when an assertion passes"""
    def assertion_errored(self, name, exception):
        """Called when an assertion throws an exception"""
    def assertion_failed(self, name, exception):
        """Called when an assertion throws an AssertionError"""

    def unexpected_error(self, exception):
        """Called when an error occurs outside of a Context or Assertion"""

    def identify_folder(self, folder):
        """
        Called when the test runner encounters a folder and wants to know if it should
        run the files in that folder.

        Arguments:
            folder - the full path of the folder which the test runner wants to be identified

        Plugins may return:
            contexts.plugins.TEST_FOLDER - plugin wishes the folder to be treated as a test folder
            None - plugin does not wish to identify the folder (though other plugins may still cause it to be run)
        """
    def identify_file(self, file):
        """
        Called when the test runner encounters a file and wants to know if it should
        run the files in that file.

        Arguments:
            file - the full path of the file which the test runner wants to be identified

        Plugins may return:
            contexts.plugins.TEST_FILE - plugin wishes the file to be imported and run as a test file
            None - plugin does not wish to identify the file (though other plugins may still cause it to be run)
        """
    def identify_class(self, cls):
        """
        Called when the test runner encounters a class and wants to know if it should
        treat it as a test class.

        Arguments:
            cls - the class object which the test runner wants to be identified.

        Plugins may return:
            contexts.plugins.CONTEXT - plugin wishes the class to be treated as a test class
            None - plugin does not wish to identify the class (though other plugins may still cause it to be run)
        """
    def identify_method(self, func):
        """
        Called when the test runner encounters a method on a test class and wants to
        know if it should run the method.

        When a test class has a superclass, all the superclass's methods will be passed in first.

        Arguments:
            func - the unbound method (or bound classmethod) which the test runner wants to be identified

        Plugins may return:
            contexts.plugins.EXAMPLES - plugin wishes the method to be treated as an 'examples' method
            contexts.plugins.SETUP - plugin wishes the method to be treated as an 'establish' method
            contexts.plugins.ACTION - plugin wishes the method to be treated as a 'because'
            contexts.plugins.ASSERTION - plugin wishes the method to be treated as an assertion method
            contexts.plugins.TEARDOWN - plugin wishes the method to be treated as a teardown method
            None - plugin does not wish to identify the method (though other plugins may still cause it to be run)
        """

    def process_module_list(self, modules):
        """Called with the full list of found modules. Plugins may modify the list in-place."""
    def process_class_list(self, modules):
        """Called with the list of classes found in a module. Plugins may modify the list in-place."""
    def process_assertion_list(self, modules):
        """Called with the list of assertion methods found in a class. Plugins may modify the list in-place."""

    def import_module(self, location, name):
        """
        Called when the test runner wants a module imported.
        Plugins may return an imported module object, or None if they do not want to import the module.

        Arguments:
            location: string. Path to the folder containing the module or package.
            name: string. Full name of the module, including dot-separated package names.
        """

    def get_exit_code(self):
        """
        Called at the end of the test runner to obtain the exit code for the process.
        Plugins may return an integer, or None if they do not want to override the default behaviour.
        """


TEST_FOLDER = "test folder - DO NOT RELY ON THE VALUE OF THIS CONSTANT"
TEST_FILE = "test file - DO NOT RELY ON THE VALUE OF THIS CONSTANT"
CONTEXT = "context - DO NOT RELY ON THE VALUE OF THIS CONSTANT"
EXAMPLES = "examples - DO NOT RELY ON THE VALUE OF THIS CONSTANT"
SETUP = "setup - DO NOT RELY ON THE VALUE OF THIS CONSTANT"
ACTION = "action - DO NOT RELY ON THE VALUE OF THIS CONSTANT"
ASSERTION = "assertion - DO NOT RELY ON THE VALUE OF THIS CONSTANT"
TEARDOWN = "teardown - DO NOT RELY ON THE VALUE OF THIS CONSTANT"


class _NoExample(object):
    """Singleton representing the absence of an Example"""
NO_EXAMPLE = _NoExample()
del _NoExample