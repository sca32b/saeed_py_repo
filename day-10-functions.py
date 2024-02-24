
def format_name(f_name, l_name):
    fmt_f_name = f_name.lower()
    rest_f_name = fmt_f_name[1:]
    first_cap_ltr_f_name = fmt_f_name[0].upper()
    new_fmt_f_name = first_cap_ltr_f_name + rest_f_name
    fmt_l_name = l_name.lower()
    rest_l_name = fmt_l_name[1:]
    first_cap_ltr_l_name = fmt_l_name[0].upper()
    new_fmt_l_name = first_cap_ltr_l_name + rest_l_name
    print(f"{new_fmt_f_name} {new_fmt_l_name}")
    return [f_name.capitalize(),l_name.capitalize()]



print(format_name(input("Enter a first name: "), input("Enter a last name: ")))    