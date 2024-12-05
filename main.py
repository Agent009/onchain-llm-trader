from lib.hl import get_user_state
from lib.spectral import test as spectral_test

# ---------- Main script
if __name__ == '__main__':
    # ---------- Run the spectral test
    spectral_test(get_user_state())

