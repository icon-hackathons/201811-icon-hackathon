from iconservice import *


def only_owner(func):

    if not isfunction(func):
        revert(f"{func} isn't function.")

    @wraps(func)
    def _wrapper(score: object, *args, **kwargs):
        if score.msg.sender.to_bytes() != score.wallet_owner.get():
            score.revert(
                f"{func} method only can be called by the owner wallet (address: {score.wallet_owner.get()})")
        return func(score, *args, **kwargs)
    return _wrapper
