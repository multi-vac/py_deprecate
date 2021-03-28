class DeprecationIntroduced(RuntimeError):
    """
    Raised When a deprecated callable is called by something that's
    not allowed to call it.
    """
