# Demo
There are two environment files: the test runs fine in ok-environment.yml, but fails in
error-environment.yml.

# Commands to try
Works fine:
```
conda deactivate && mamba env remove -n vcr_resrouce_warning && mamba env create -f ok-environment.yml && conda activate vcr_resrouce_warning && rm -f test_generate_resource_warning.yaml && python -m pytest
```

Fails:
```
conda deactivate && mamba env remove -n vcr_resrouce_warning && mamba env create -f error-environment.yml && conda activate vcr_resrouce_warning && rm -f test_generate_resource_warning.yaml && python -m pytest
```

# Non platform specific environment file
There is a non-platform-specific.yml -- it does not generate an error, but if you remove one of the
packages (see comment in the yml), the test fails.


# Observed failure
This is how the failure look like:
```
=========================================================================================================== test session starts ============================================================================================================
platform darwin -- Python 3.8.17, pytest-7.4.0, pluggy-1.2.0
rootdir: /Users/ant/t/vcr_resrouce_warning_from_original
configfile: pytest.ini
collected 2 items

test_resource_warning.py F.                                                                                                                                                                                                          [100%]

================================================================================================================= FAILURES =================================================================================================================
______________________________________________________________________________________________________ test_generate_resource_warning ______________________________________________________________________________________________________

cls = <class '_pytest.runner.CallInfo'>, func = <function call_runtest_hook.<locals>.<lambda> at 0x7fd4e01a4dc0>, when = 'call', reraise = (<class '_pytest.outcomes.Exit'>, <class 'KeyboardInterrupt'>)

    @classmethod
    def from_call(
        cls,
        func: "Callable[[], TResult]",
        when: "Literal['collect', 'setup', 'call', 'teardown']",
        reraise: Optional[
            Union[Type[BaseException], Tuple[Type[BaseException], ...]]
        ] = None,
    ) -> "CallInfo[TResult]":
        """Call func, wrapping the result in a CallInfo.

        :param func:
            The function to call. Called without arguments.
        :param when:
            The phase in which the function is called.
        :param reraise:
            Exception or exceptions that shall propagate if raised by the
            function, instead of being wrapped in the CallInfo.
        """
        excinfo = None
        start = timing.time()
        precise_start = timing.perf_counter()
        try:
>           result: Optional[TResult] = func()

../../opt/miniconda3/envs/vcr_resrouce_warning/lib/python3.8/site-packages/_pytest/runner.py:341:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
../../opt/miniconda3/envs/vcr_resrouce_warning/lib/python3.8/site-packages/_pytest/runner.py:262: in <lambda>
    lambda: ihook(item=item, **kwds), when=when, reraise=reraise
../../opt/miniconda3/envs/vcr_resrouce_warning/lib/python3.8/site-packages/pluggy/_hooks.py:433: in __call__
    return self._hookexec(self.name, self._hookimpls, kwargs, firstresult)
../../opt/miniconda3/envs/vcr_resrouce_warning/lib/python3.8/site-packages/pluggy/_manager.py:112: in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
../../opt/miniconda3/envs/vcr_resrouce_warning/lib/python3.8/site-packages/_pytest/unraisableexception.py:88: in pytest_runtest_call
    yield from unraisable_exception_runtest_hook()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    def unraisable_exception_runtest_hook() -> Generator[None, None, None]:
        with catch_unraisable_exception() as cm:
            yield
            if cm.unraisable:
                if cm.unraisable.err_msg is not None:
                    err_msg = cm.unraisable.err_msg
                else:
                    err_msg = "Exception ignored in"
                msg = f"{err_msg}: {cm.unraisable.object!r}\n\n"
                msg += "".join(
                    traceback.format_exception(
                        cm.unraisable.exc_type,
                        cm.unraisable.exc_value,
                        cm.unraisable.exc_traceback,
                    )
                )
>               warnings.warn(pytest.PytestUnraisableExceptionWarning(msg))
E               pytest.PytestUnraisableExceptionWarning: Exception ignored in: <ssl.SSLSocket fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>
E
E               Traceback (most recent call last):
E                 File "/Users/ant/opt/miniconda3/envs/vcr_resrouce_warning/lib/python3.8/site-packages/vcr/cassette.py", line 99, in __exit__
E                   next(self.__finish, None)
E               ResourceWarning: unclosed <ssl.SSLSocket fd=16, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.1.143', 49751), raddr=('172.217.23.100', 443)>

../../opt/miniconda3/envs/vcr_resrouce_warning/lib/python3.8/site-packages/_pytest/unraisableexception.py:78: PytestUnraisableExceptionWarning
========================================================================================================= short test summary info ==========================================================================================================
FAILED test_resource_warning.py::test_generate_resource_warning - pytest.PytestUnraisableExceptionWarning: Exception ignored in: <ssl.SSLSocket fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>
```

