class fmt:
    # Single
    p = '\033[92m'  # PASS
    w = '\033[93m'  # WARNING
    f = '\033[91m'  # FAIL
    b = '\033[1m'   # BOLD
    u = '\033[4m'   # UNDERLINE
    # Background colors
    bg_black = '\033[40m'
    bg_red = '\033[41m'
    bg_green = '\033[42m'
    bg_yellow = '\033[43m'
    bg_blue = '\033[44m'
    bg_magenta = '\033[45m'
    bg_cyan = '\033[46m'
    bg_white = '\033[47m'
    n = ''
    # Combinations
    bu = '\033[1m\033[4m'  # BOLD_UNDERLINE
    pb = '\033[92m\033[1m'  # PASS_BOLD
    pu = '\033[92m\033[4m'  # PASS_UNDERLINE
    pbu = '\033[92m\033[1m\033[4m'  # PASS_BOLD_UNDERLINE
    wb = '\033[93m\033[1m'  # WARNING_BOLD
    wu = '\033[93m\033[4m'  # WARNING_UNDERLINE
    wbu = '\033[93m\033[1m\033[4m'  # WARNING_BOLD_UNDERLINE
    fb = '\033[91m\033[1m'  # FAIL_BOLD
    fu = '\033[91m\033[4m'  # FAIL_UNDERLINE
    fbu = '\033[91m\033[1m\033[4m'  # FAIL_BOLD_UNDERLINE
    # End
    e = '\033[0m'  # END
    
def fmt_str(string, format, bg_color=''):
    return f'{format}{bg_color}{string}{fmt.e}'

print(fmt_str('Hello World!', fmt.pb, fmt.bg_black))