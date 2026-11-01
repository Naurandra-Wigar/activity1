def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


my_profile = build_profile(
    "Naurandra",
    "(wigar)",         # ganti
    city="(boyolali)",           # ganti
    hobby="(membaca)",          # ganti
    field="(teknik industri)",  # ganti
)
print(my_profile)