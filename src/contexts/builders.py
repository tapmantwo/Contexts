import itertools
from .core import Suite, Context, Assertion
from . import finders
from . import errors


def build_suite_from_iterable(iterable):
    contexts = [build_context(x) for x in iterable]
    return Suite(contexts)


def build_suite_from_module(module):
    specs = finders.get_contexts_from_module(module)
    contexts = [build_context(spec) for spec in specs]
    return Suite(contexts)


def build_suite_from_class(cls):
    return build_suite_from_instance(cls())


def build_suite_from_instance(spec):
    contexts = [build_context(spec)]
    return Suite(contexts)


def build_context(spec):
    setups = finders.find_setups(spec)
    actions = finders.find_actions(spec)
    assertions = finders.find_assertions(spec)
    teardowns = finders.find_teardowns(spec)

    assert_no_ambiguous_methods(setups, actions, assertions, teardowns)

    wrapped_assertions = [Assertion(f, build_assertion_name(f)) for f in assertions]
    return Context(setups, actions, wrapped_assertions, teardowns, spec.__class__.__name__)


def build_assertion_name(func):
    module_name = func.__self__.__class__.__module__
    method_name = func.__func__.__qualname__
    return '{}.{}'.format(module_name, method_name)


def assert_no_ambiguous_methods(*iterables):
    for a, b in itertools.combinations((set(i) for i in iterables), 2):
        overlap = a & b
        if overlap:
            msg = "The following methods are ambiguously named:\n"
            msg += '\n'.join([func.__qualname__ for func in overlap])
            raise errors.MethodNamingError(msg)