# https://www.hillelwayne.com/post/contract-examples/
# dpcontracts enforces preconditions
from dpcontracts import require


@require("l must not be empty", lambda args: len(args.l) > 0)
def mode(l):
    # Some algorithm to calculate the mode
    return l  # Return the list itself for test purposes


if __name__ == '__main__':
    mode([])  # dpcontracts.PreconditionError: l must not be empty

